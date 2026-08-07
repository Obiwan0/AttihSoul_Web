import reflex as rx
from psycopg.rows import dict_row

from ..database.postgres import get_connection


def init_db():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS bookings(
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT,
            event_type TEXT,
            event_date TEXT,
            location TEXT,
            message TEXT,
            status TEXT DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


init_db()


class BookingState(rx.State):
    """Manages booking requests from the contact form and admin."""

    # Form fields
    name: str = ""
    email: str = ""
    phone: str = ""
    event_type: str = ""
    event_date: str = ""
    location: str = ""
    message: str = ""

    # Data
    bookings: list[dict] = []
    search_query: str = ""
    submitted: bool = False

    @rx.event
    def set_name(self, value: str):
        self.name = value
        self.submitted = False

    @rx.event
    def set_email(self, value: str):
        self.email = value
        self.submitted = False

    @rx.event
    def set_phone(self, value: str):
        self.phone = value
        self.submitted = False

    @rx.event
    def set_event_type(self, value: str):
        self.event_type = value
        self.submitted = False

    @rx.event
    def set_event_date(self, value: str):
        self.event_date = value
        self.submitted = False

    @rx.event
    def set_location(self, value: str):
        self.location = value
        self.submitted = False

    @rx.event
    def set_message(self, value: str):
        self.message = value
        self.submitted = False

    @rx.event
    def set_search_query(self, value: str):
        self.search_query = value

    @rx.event
    def load_bookings(self):
        conn = get_connection()
        cur = conn.cursor(row_factory=dict_row)
        cur.execute("SELECT * FROM bookings ORDER BY id DESC")
        self.bookings = [dict(r) for r in cur.fetchall()]
        conn.close()

    @rx.event
    def submit_booking(self):
        if not self.name.strip() or not self.email.strip():
            return
        conn = get_connection()
        conn.execute(
            """INSERT INTO bookings(name, email, phone, event_type, event_date, location, message, status)
               VALUES(%s, %s, %s, %s, %s, %s, %s, 'pending')""",
            (
                self.name.strip(),
                self.email.strip(),
                self.phone.strip(),
                self.event_type.strip(),
                self.event_date.strip(),
                self.location.strip(),
                self.message.strip(),
            ),
        )
        conn.commit()
        conn.close()
        self.name = ""
        self.email = ""
        self.phone = ""
        self.event_type = ""
        self.event_date = ""
        self.location = ""
        self.message = ""
        self.submitted = True
        self.load_bookings()

    @rx.event
    def approve_booking(self, booking_id: int):
        conn = get_connection()
        conn.execute("UPDATE bookings SET status='approved' WHERE id=%s", (booking_id,))
        conn.commit()
        conn.close()
        self.load_bookings()

    @rx.event
    def reject_booking(self, booking_id: int):
        conn = get_connection()
        conn.execute("UPDATE bookings SET status='rejected' WHERE id=%s", (booking_id,))
        conn.commit()
        conn.close()
        self.load_bookings()

    @rx.event
    def delete_booking(self, booking_id: int):
        conn = get_connection()
        conn.execute("DELETE FROM bookings WHERE id=%s", (booking_id,))
        conn.commit()
        conn.close()
        self.load_bookings()

    @rx.var
    def pending_bookings(self) -> list[dict]:
        return [b for b in self.bookings if b["status"] == "pending"]

    @rx.var
    def approved_bookings(self) -> list[dict]:
        return [b for b in self.bookings if b["status"] == "approved"]

    @rx.var
    def rejected_bookings(self) -> list[dict]:
        return [b for b in self.bookings if b["status"] == "rejected"]

    @rx.var
    def filtered_bookings(self) -> list[dict]:
        if not self.search_query.strip():
            return self.bookings
        q = self.search_query.lower()
        return [
            b
            for b in self.bookings
            if q in b.get("name", "").lower()
            or q in b.get("email", "").lower()
            or q in b.get("message", "").lower()
        ]