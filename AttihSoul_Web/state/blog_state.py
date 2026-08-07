import reflex as rx
from psycopg.rows import dict_row

from ..database.postgres import get_connection

# Canonical schema for the blog_posts table (order matters for CREATE TABLE).
BLOG_SCHEMA = [
    ("id", "SERIAL PRIMARY KEY"),
    ("title", "TEXT NOT NULL"),
    ("content", "TEXT NOT NULL"),
    ("category", "TEXT DEFAULT 'general'"),
    ("status", "TEXT DEFAULT 'draft'"),
    ("featured_image", "TEXT DEFAULT ''"),
    ("created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP"),
]

# Defaults used to backfill pre-existing rows for columns added via migration.
BACKFILL_DEFAULTS = {
    "category": "general",
    "status": "draft",
    "featured_image": "",
}


def _table_columns(conn) -> set[str]:
    """Return the set of column names currently present in blog_posts."""
    cur = conn.cursor()
    cur.execute(
        """
        SELECT column_name
        FROM information_schema.columns
        WHERE table_name = 'blog_posts'
        """
    )
    return {row[0] for row in cur.fetchall()}


def init_db():
    """Create the blog_posts table and migrate it to the current schema.

    Safe and idempotent:
      * Never drops the table or any rows.
      * Only adds columns that are missing.
      * Backfills sensible defaults for pre-existing rows.
    """
    conn = get_connection()
    try:
        # 1. Create the table with the full canonical schema if it doesn't exist.
        cols_sql = ", ".join(f"{name} {ctype}" for name, ctype in BLOG_SCHEMA)
        conn.execute(f"CREATE TABLE IF NOT EXISTS blog_posts({cols_sql})")

        # 2. Migrate: add any columns the existing table is missing.
        existing = _table_columns(conn)
        for name, ctype in BLOG_SCHEMA:
            if name in existing:
                continue
            # PostgreSQL ALTER TABLE ADD COLUMN IF NOT EXISTS is safe.
            conn.execute(f"ALTER TABLE blog_posts ADD COLUMN IF NOT EXISTS {name} {ctype}")

        # 3. Backfill defaults for pre-existing rows that are still NULL.
        for col, default in BACKFILL_DEFAULTS.items():
            conn.execute(
                f"UPDATE blog_posts SET {col} = %s WHERE {col} IS NULL",
                (default,),
            )
        conn.execute(
            "UPDATE blog_posts SET created_at = CURRENT_TIMESTAMP WHERE created_at IS NULL"
        )

        conn.commit()
    finally:
        conn.close()


init_db()


class BlogState(rx.State):

    title: str = ""
    content: str = ""
    category: str = "general"
    status: str = "draft"
    featured_image: str = ""
    editing_id: int | None = None

    posts: list[dict] = []

    @rx.event
    def set_title(self, value: str):
        self.title = value

    @rx.event
    def set_content(self, value: str):
        self.content = value

    @rx.event
    def set_category(self, value: str):
        self.category = value

    @rx.event
    def set_status(self, value: str):
        self.status = value

    @rx.event
    def set_featured_image(self, value: str):
        self.featured_image = value

    @rx.event
    def load_posts(self):
        conn = get_connection()
        cur = conn.cursor(row_factory=dict_row)
        cur.execute("SELECT * FROM blog_posts ORDER BY id DESC")
        self.posts = [dict(r) for r in cur.fetchall()]
        conn.close()

    @rx.event
    def publish_post(self):
        if not self.title.strip() or not self.content.strip():
            return
        conn = get_connection()
        conn.execute(
            "INSERT INTO blog_posts(title, content, category, status, featured_image, created_at) "
            "VALUES(%s, %s, %s, %s, %s, CURRENT_TIMESTAMP)",
            (
                self.title.strip(),
                self.content.strip(),
                self.category.strip(),
                self.status.strip(),
                self.featured_image.strip(),
            ),
        )
        conn.commit()
        conn.close()
        self.title = ""
        self.content = ""
        self.category = "general"
        self.status = "draft"
        self.featured_image = ""
        self.load_posts()

    @rx.event
    def start_edit(self, post_id: int):
        self.editing_id = post_id
        for post in self.posts:
            if post["id"] == post_id:
                self.title = post["title"]
                self.content = post["content"]
                self.category = post.get("category", "general")
                self.status = post.get("status", "draft")
                self.featured_image = post.get("featured_image", "")
                break

    @rx.event
    def cancel_edit(self):
        self.editing_id = None
        self.title = ""
        self.content = ""
        self.category = "general"
        self.status = "draft"
        self.featured_image = ""

    @rx.event
    def save_edit(self):
        if self.editing_id is None:
            return
        conn = get_connection()
        conn.execute(
            "UPDATE blog_posts SET title=%s, content=%s, category=%s, status=%s, featured_image=%s WHERE id=%s",
            (
                self.title.strip(),
                self.content.strip(),
                self.category.strip(),
                self.status.strip(),
                self.featured_image.strip(),
                self.editing_id,
            ),
        )
        conn.commit()
        conn.close()
        self.cancel_edit()
        self.load_posts()

    @rx.event
    def delete_post(self, post_id: int):
        conn = get_connection()
        conn.execute("DELETE FROM blog_posts WHERE id=%s", (post_id,))
        conn.commit()
        conn.close()
        self.load_posts()

    @rx.var
    def draft_posts(self) -> list[dict]:
        return [p for p in self.posts if p.get("status") == "draft"]

    @rx.var
    def published_posts(self) -> list[dict]:
        return [p for p in self.posts if p.get("status") == "published"]