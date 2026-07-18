import reflex as rx


class AdminState(rx.State):
    """Controls navigation inside the admin dashboard."""

    current_page: str = "dashboard"

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

    @rx.event
    def logout(self):
        self.current_page = "dashboard"