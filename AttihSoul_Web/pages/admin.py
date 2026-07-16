import reflex as rx
from typing import Any
from ..pages.navbar import navbar
from ..components.footer import footer
from ..components.admin.music import music_page
# later we'll also have:
# from ..components.admin.gallery import gallery_page
# from ..components.admin.bookings import bookings_page
# from ..components.admin.settings import settings_page
# from ..components.admin.blog import blog_manager
from ..state.review_state import ReviewState
from ..state.blog_state import BlogState
from ..state.admin_state import AdminState

# -------------------------------------------------
# Dashboard Card
# -------------------------------------------------
def dashboard_card(title: str, description: str, on_click):
    return rx.box(
        rx.vstack(
            rx.heading(title, color="#D4AF37", size="5"),
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
        _hover={"border": "1px solid #D4AF37"}
    )

# -------------------------------------------------
# Statistics Card
# -------------------------------------------------
def stat_card(title: str, value: Any):
    return rx.box(
        rx.vstack(
            rx.text(
                title,
                color="#BBBBBB",
                font_size="0.9rem",
            ),
            rx.heading(
                value,
                color="#D4AF37",
                size="8",
            ),
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

# -------------------------------------------------
# Review Card
# -------------------------------------------------
def review_card(review):
    return rx.box(
        rx.vstack(
            rx.text(review["name"], font_weight="bold", color="#D4AF37", font_size="1.1rem"),
            rx.text(review["review"], color="white"),
            rx.hstack(
                rx.button("Approve", color_scheme="green", on_click=lambda: ReviewState.approve_review(review["id"])),
                rx.button("Reject", color_scheme="red", on_click=lambda: ReviewState.reject_review(review["id"])),
                spacing="3",
            ),
            spacing="4",
            align="start",
        ),
        width="100%",
        background="#1A1A1A",
        border="1px solid #222222",
        border_radius="12px",
        padding="20px",
    )

def admin_page():
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading("Attih Soul Admin", color="#D4AF37", size="8", text_align="center", width="100%"),
                rx.text("Manage site content from the dashboard.", color="#AAAAAA", text_align="center"),
                rx.divider(),

                # Dashboard Navigation
                rx.grid(
                    dashboard_card("Dashboard", "CMS Overview", AdminState.go_dashboard),
                    dashboard_card("Blog", "Manage blog posts", AdminState.go_blog),
                    dashboard_card("Reviews", "Approve reviews", AdminState.go_reviews),
                    dashboard_card("Bookings", "Booking requests", AdminState.go_bookings),
                    dashboard_card("Music", "Songs & Spotify", AdminState.go_music),
                    dashboard_card("Gallery", "Photos & Videos", AdminState.go_gallery),
                    dashboard_card("Settings", "Website settings", AdminState.go_settings),
                    columns={"base": "1", "sm": "2", "md": "3"},
                    spacing="5",
                    width="100%",
                ),
                
                rx.divider(),

                # Dynamic Content based on AdminState.current_page
                rx.box(
                    rx.cond(
                        AdminState.current_page == "dashboard",
                        rx.vstack(
                            rx.heading("Dashboard Overview", color="#D4AF37", size="6"),
                            rx.grid(
                                stat_card("Blog Posts", "0"),
                                stat_card(
                                    "Pending Reviews",
                                    ReviewState.pending_reviews.length(),
                                ),
                                stat_card(
                                    "Approved Reviews",
                                    ReviewState.approved_reviews.length(),
                                ),
                                stat_card("Bookings", "0"),
                                stat_card("Songs", "0"),
                                stat_card("Gallery", "0"),
                                columns={"base": "1", "sm": "2", "lg": "3"},
                                spacing="5",
                                width="100%",
                            ),
                            rx.box(
                                rx.heading("Quick Actions", color="#D4AF37", size="5"),
                                rx.hstack(
                                    rx.button("New Blog", on_click=AdminState.go_blog, background="#D4AF37", color="black"),
                                    rx.button("Moderate Reviews", on_click=AdminState.go_reviews, background="#D4AF37", color="black"),
                                    rx.button("Bookings", on_click=AdminState.go_bookings, background="#D4AF37", color="black"),
                                    wrap="wrap",
                                    spacing="4",
                                ),
                                width="100%",
                            ),
                            spacing="6",
                            width="100%",
                        ),
                    ),
                    rx.cond(
                        AdminState.current_page == "reviews",
                        rx.vstack(
                            rx.heading("Pending Reviews", color="#D4AF37", size="5"),
                            rx.foreach(ReviewState.pending_reviews, review_card),
                            width="100%"
                        ),
                    ),
                    rx.cond(
                        AdminState.current_page == "blog",
                        rx.vstack(
                            rx.heading("Blog Manager", color="#D4AF37", size="5"),
                            rx.input(placeholder="Blog Title", value=BlogState.title, on_change=BlogState.set_title, width="100%"),
                            rx.text_area(placeholder="Write your blog...", value=BlogState.content, on_change=BlogState.set_content, width="100%", min_height="220px"),
                            rx.button("Publish Post", background="#D4AF37", color="black", on_click=BlogState.publish_post),
                            width="100%"
                        ),
                    ),
                    rx.cond(
                        AdminState.current_page == "bookings",
                        rx.text("Booking requests will appear here.", color="white"),
                    ),
                    rx.cond(
                        AdminState.current_page == "music",
                        music_page(),
                    ),
                    rx.cond(
                        AdminState.current_page == "gallery",
                        rx.text("Gallery manager coming next...", color="white"),
                    ),
                    rx.cond(
                        AdminState.current_page == "settings",
                        rx.text("Settings page coming next...", color="white"),
                    ),
                    width="100%", background="#111111", border="1px solid #222222", border_radius="12px", padding="20px"
                ),

                rx.button(
                    "Logout", 
                    color_scheme="red", 
                    on_click=AdminState.logout,
                    width={"base": "100%", "sm": "220px"},
                ),
                spacing="8", width="100%", align="stretch",
            ),
            max_width="1100px", width="100%", padding_top="110px", padding_bottom="60px",
        ),
        footer(),
        background="black",
        min_height="100vh",
        on_mount=ReviewState.load_reviews,
    )