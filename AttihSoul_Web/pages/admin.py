import reflex as rx
from ..state.music_state import MusicState
from ..state.gallery_state import GalleryState
from ..state.blog_state import BlogState
from ..state.review_state import ReviewState
from ..state.booking_state import BookingState
from ..state.settings_state import SettingsState
from .navbar import navbar
from ..components.footer import footer
from ..components.admin.dashboard import dashboard_component
from ..components.admin.blog import blog_manager
from ..components.admin.reviews import reviews_manager
from ..components.admin.bookings import bookings_manager
from ..components.admin.music import music_page
from ..components.admin.gallery import gallery_manager
from ..components.admin.settings import settings_page
from ..state.admin_state import AdminState

GOLD = "#D4AF37"


# -------------------------------------------------
# Dashboard Card (navigation)
# -------------------------------------------------
def dashboard_card(title: str, description: str, on_click):
    return rx.box(
        rx.vstack(
            rx.heading(title, color=GOLD, size="5"),
            rx.text(description, color="#BBBBBB"),
            spacing="2",
            align="start",
        ),
        width="100%",
        background="#111111",
        border="1px solid #222222",
        border_radius="12px",
        padding="20px",
        cursor="pointer",
        on_click=on_click,
        _hover={"border": f"1px solid {GOLD}"},
    )


# -------------------------------------------------
# Login Screen
# -------------------------------------------------
def login_screen():
    return rx.center(
        rx.vstack(
            rx.box(
                rx.text("Attih Soul", color=GOLD, font_size="2.5rem", font_weight="700", font_style="italic", text_align="center"),
                width="100%",
            ),
            rx.text("Admin Dashboard", color="white", font_size="1.5rem", font_weight="600"),
            rx.box(height="2rem"),
            rx.input(
                placeholder="Enter Admin Password",
                type="password",
                value=AdminState.password,
                on_change=AdminState.set_password,
                width="100%",
                max_width="350px",
                background="#1A1A1A",
                border="1px solid #333333",
                color="white",
                padding="1rem",
            ),
            rx.button(
                "Login",
                on_click=AdminState.login,
                background=GOLD,
                color="black",
                width="100%",
                max_width="350px",
                _hover={"background": "#c99a3e"},
            ),
            spacing="3",
            align="center",
            padding="3rem",
            background="#111111",
            border="1px solid #222222",
            border_radius="16px",
            max_width="450px",
            width="100%",
        ),
        width="100%",
        min_height="100vh",
        background="black",
        padding="1rem",
    )


# -------------------------------------------------
# Admin Dashboard (authenticated)
# -------------------------------------------------
def admin_dashboard():
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading("Attih Soul Admin", color=GOLD, size="8", text_align="center", width="100%"),
                rx.text("Manage site content from the dashboard.", color="#AAAAAA", text_align="center"),
                rx.divider(),
                # Navigation cards
                rx.grid(
                    dashboard_card("Dashboard", "CMS Overview", AdminState.go_dashboard),
                    dashboard_card("Blog", "Manage blog posts", AdminState.go_blog),
                    dashboard_card("Reviews", "Approve reviews", AdminState.go_reviews),
                    dashboard_card("Bookings", "Booking requests", AdminState.go_bookings),
                    dashboard_card("Music", "Songs & Spotify", AdminState.go_music),
                    dashboard_card("Gallery", "Photos & Videos", AdminState.go_gallery),
                    dashboard_card("Settings", "Website settings", AdminState.go_settings),
                    columns={"base": "1", "sm": "2", "md": "3", "lg": "4"},
                    spacing="5",
                    width="100%",
                ),
                rx.divider(),
                # Dynamic content area
                rx.box(
                    rx.cond(AdminState.current_page == "dashboard", dashboard_component()),
                    rx.cond(AdminState.current_page == "reviews", reviews_manager()),
                    rx.cond(AdminState.current_page == "blog", blog_manager()),
                    rx.cond(AdminState.current_page == "bookings", bookings_manager()),
                    rx.cond(AdminState.current_page == "music", music_page()),
                    rx.cond(AdminState.current_page == "gallery", gallery_manager()),
                    rx.cond(AdminState.current_page == "settings", settings_page()),
                    width="100%",
                    background="#111111",
                    border="1px solid #222222",
                    border_radius="12px",
                    padding="20px",
                ),
                rx.button(
                    "Logout",
                    on_click=AdminState.logout,
                    color_scheme="red",
                    width={"base": "100%", "sm": "220px"},
                ),
                spacing="8",
                width="100%",
                align="stretch",
            ),
            max_width="1100px",
            width="100%",
            padding_top="110px",
            padding_bottom="60px",
        ),
        footer(),
        background="black",
        min_height="100vh",
    )


# -------------------------------------------------
# Admin page entry point
# -------------------------------------------------
def admin_page():
    return rx.cond(
        AdminState.is_authenticated,
        rx.box(
            admin_dashboard(),
            on_mount=[
                MusicState.load_songs,
                GalleryState.load_items,
                BlogState.load_posts,
                ReviewState.load_reviews,
                BookingState.load_bookings,
                SettingsState.load_settings,
            ],
        ),
        login_screen(),
    )
