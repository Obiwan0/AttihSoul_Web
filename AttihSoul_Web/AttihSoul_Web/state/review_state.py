import sqlite3
import reflex as rx
import os

DB_NAME = "reviews.db"
ADMIN_PASSWORD = "AttihSoulAdmin2026"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
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
    admin_password: str = ""
    is_admin: bool = False
    name: str = ""
    review: str = ""
    reviews: list[dict] = []

    @rx.event
    def set_name(self, value: str):
        self.name = value

    @rx.event
    def set_review(self, value: str):
        self.review = value

    @rx.event
    def set_admin_password(self, value: str):
        self.admin_password = value

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
    def login_admin(self):
        if self.admin_password == ADMIN_PASSWORD:
            self.is_admin = True
            self.admin_password = ""
            self.load_reviews()

    @rx.event
    def logout_admin(self):
        self.is_admin = False
        self.admin_password = ""
        self.reviews = []

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

    @rx.var
    def approved_reviews(self) -> list[dict]:
        return [r for r in self.reviews if r["status"] == "approved"]

    @rx.var
    def pending_reviews(self) -> list[dict]:
        return [r for r in self.reviews if r["status"] == "pending"]