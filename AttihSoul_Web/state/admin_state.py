import reflex as rx

ADMIN_PASSWORD = "BigCeasar2026#"


class AdminState(rx.State):
    """Controls navigation and authentication inside the admin dashboard."""

    current_page: str = "dashboard"
    password: str = ""
    is_authenticated: bool = False

    @rx.event
    def set_password(self, value: str):
        self.password = value

    @rx.event
    def login(self):
        if self.password == ADMIN_PASSWORD:
            self.is_authenticated = True
            self.password = ""
        else:
            self.password = ""

    @rx.event
    def logout(self):
        self.is_authenticated = False
        self.current_page = "dashboard"
        self.password = ""

    @rx.event
    def go_dashboard(self):
        self.current_page = "dashboard"

    @rx.event
    def go_blog(self):
        self.current_page = "blog"

    @rx.event
    def go_reviews(self):
        self.current_page = "reviews"

    @rx.event
    def go_bookings(self):
        self.current_page = "bookings"

    @rx.event
    def go_music(self):
        self.current_page = "music"

    @rx.event
    def go_gallery(self):
        self.current_page = "gallery"

    @rx.event
    def go_settings(self):
        self.current_page = "settings"