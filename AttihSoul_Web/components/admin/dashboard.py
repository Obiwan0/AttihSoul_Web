import reflex as rx
from ...state.admin_state import AdminState

GOLD = "#D4AF37"


def stat_card(title: str, value):
    return rx.box(
        rx.vstack(
            rx.text(title, color="#BBBBBB", font_size="0.9rem"),
            rx.heading(value, color=GOLD, size="8"),
            spacing="1",
            align="center",
        ),
        width="100%",
        background="#1A1A1A",
        border="1px solid #222222",
        border_radius="12px",
        padding="25px",
        text_align="center",
    )


def dashboard_component():
    """Main dashboard overview with live stats and quick actions."""
    from ...state.review_state import ReviewState
    from ...state.blog_state import BlogState
    from ...state.music_state import MusicState
    from ...state.booking_state import BookingState
    from ...state.gallery_state import GalleryState

    return rx.vstack(
        rx.heading("Dashboard Overview", color=GOLD, size="6"),
        rx.text("Welcome to the Attih Soul CMS.", color="#AAAAAA"),
        rx.divider(),
        rx.grid(
            stat_card("Blog Posts", BlogState.posts.length()),
            stat_card("Pending Reviews", ReviewState.pending_reviews.length()),
            stat_card("Approved Reviews", ReviewState.approved_reviews.length()),
            stat_card("Total Bookings", BookingState.bookings.length()),
            stat_card("Music Tracks", MusicState.songs.length()),
            stat_card("Gallery Items", GalleryState.items.length()),
            columns={"base": "1", "sm": "2", "lg": "3"},
            spacing="5",
            width="100%",
        ),
        rx.divider(),
        rx.box(
            rx.heading("Quick Actions", color=GOLD, size="5"),
            rx.hstack(
                rx.button(
                    "New Blog Post",
                    on_click=AdminState.go_blog,
                    background=GOLD,
                    color="black",
                    _hover={"background": "#c99a3e"},
                ),
                rx.button(
                    "Moderate Reviews",
                    on_click=AdminState.go_reviews,
                    background=GOLD,
                    color="black",
                    _hover={"background": "#c99a3e"},
                ),
                rx.button(
                    "View Bookings",
                    on_click=AdminState.go_bookings,
                    background=GOLD,
                    color="black",
                    _hover={"background": "#c99a3e"},
                ),
                wrap="wrap",
                spacing="4",
            ),
            width="100%",
        ),
        spacing="6",
        width="100%",
    )