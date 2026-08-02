import sqlite3
from pathlib import Path
import reflex as rx

BASE_DIR = Path(__file__).resolve().parent.parent

DB_NAME = BASE_DIR / "database" / "reviews.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS reviews(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        review TEXT,
        status TEXT DEFAULT 'pending'
    )
    """)
    conn.commit()
    conn.close()


init_db()


def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


class ReviewState(rx.State):
    name: str = ""
    review: str = ""
    reviews: list[dict] = []
    search_query: str = ""

    @rx.event
    def set_name(self, value: str):
        self.name = value

    @rx.event
    def set_review(self, value: str):
        self.review = value

    @rx.event
    def set_search_query(self, value: str):
        self.search_query = value

    @rx.event
    def load_reviews(self):
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT id, name, review, status FROM reviews ORDER BY id DESC")
        self.reviews = [dict(r) for r in cur.fetchall()]
        conn.close()

    @rx.event
    def submit_review(self):
        if not self.name.strip() or not self.review.strip():
            return
        conn = get_db()
        conn.execute("INSERT INTO reviews(name, review, status) VALUES(?, ?, 'pending')",
                     (self.name.strip(), self.review.strip()))
        conn.commit()
        conn.close()
        self.name, self.review = "", ""
        self.load_reviews()

    @rx.event
    def approve_review(self, review_id: int):
        conn = get_db()
        conn.execute("UPDATE reviews SET status='approved' WHERE id=?", (review_id,))
        conn.commit()
        conn.close()
        self.load_reviews()

    @rx.event
    def reject_review(self, review_id: int):
        conn = get_db()
        conn.execute("UPDATE reviews SET status='rejected' WHERE id=?", (review_id,))
        conn.commit()
        conn.close()
        self.load_reviews()

    @rx.event
    def delete_review(self, review_id: int):
        conn = get_db()
        conn.execute("DELETE FROM reviews WHERE id=?", (review_id,))
        conn.commit()
        conn.close()
        self.load_reviews()

    @rx.var
    def approved_reviews(self) -> list[dict]:
        return [r for r in self.reviews if r["status"] == "approved"]

    @rx.var
    def pending_reviews(self) -> list[dict]:
        return [r for r in self.reviews if r["status"] == "pending"]

    @rx.var
    def rejected_reviews(self) -> list[dict]:
        return [r for r in self.reviews if r["status"] == "rejected"]

    @rx.var
    def filtered_reviews(self) -> list[dict]:
        if not self.search_query.strip():
            return self.reviews
        q = self.search_query.lower()
        return [
            r
            for r in self.reviews
            if q in r.get("name", "").lower()
            or q in r.get("review", "").lower()
        ]