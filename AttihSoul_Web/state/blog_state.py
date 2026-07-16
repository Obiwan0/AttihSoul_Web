import sqlite3
import reflex as rx

DB_NAME = "blog.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS blog_posts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


init_db()


class BlogState(rx.State):

    title: str = ""
    content: str = ""

    posts: list[dict] = []

    @rx.event
    def set_title(self, value: str):
        self.title = value

    @rx.event
    def set_content(self, value: str):
        self.content = value

    @rx.event
    def publish_post(self):

        if not self.title.strip() or not self.content.strip():
            return

        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO blog_posts(title, content) VALUES(?, ?)",
            (
                self.title,
                self.content,
            ),
        )

        conn.commit()
        conn.close()

        self.title = ""
        self.content = ""
        self.load_posts()

    @rx.event
    def load_posts(self):

        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()

        cur.execute(
            "SELECT id, title, content FROM blog_posts ORDER BY id DESC"
        )

        self.posts = [
            {
                "id": row[0],
                "title": row[1],
                "content": row[2],
            }
            for row in cur.fetchall()
        ]

        conn.close()