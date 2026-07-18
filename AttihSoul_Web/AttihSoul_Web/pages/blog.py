import reflex as rx

from .helpers import (
    video_bg,
    overlay,
    gold_button,
    bp,
    GOLD,
    TEXT_WHITE,
    TEXT_GRAY,
    DARK_BG,
    CARD_BG,
)

from .navbar import navbar
from ..state.blog_state import BlogState


def blog_card(post):
    return rx.box(

        rx.vstack(

            rx.image(
                src="https://picsum.photos/600/350",
                width="100%",
                height="220px",
                object_fit="cover",
                border_radius="10px",
            ),

            rx.heading(
                post["title"],
                color=TEXT_WHITE,
                font_size="1.35rem",
                font_weight="700",
            ),

            rx.text(
                post["content"],
                color=TEXT_WHITE,
                font_size="0.95rem",
            ),

            spacing="3",
            align="start",
            width="100%",
        ),

        background=CARD_BG,
        padding="20px",
        border_radius="14px",
        border="1px solid #222222",
        width="100%",
    )


def blog_page() -> rx.Component:

    return rx.box(

        navbar(),

        # ----------------------------------------
        # HERO
        # ----------------------------------------

        rx.box(

            video_bg("/blog_bg.mp4"),

            overlay("rgba(0,0,0,0.45)"),

            rx.center(

                rx.vstack(

                    rx.heading(
                        "INSIGHTS & STORIES",
                        color="white",
                        font_size=bp(
                            initial="28px",
                            md="4.5rem",
                        ),
                        font_weight="800",
                        text_align="center",
                    ),

                    rx.divider(
                        border_color=GOLD,
                        width="60%",
                    ),

                    rx.text(
                        "Discover thoughts, updates and behind-the-scenes stories.",
                        color="white",
                        text_align="center",
                        font_size=bp(
                            initial="14px",
                            md="1.1rem",
                        ),
                        max_width="550px",
                    ),

                    gold_button(
                        "Latest Posts",
                        "#posts",
                    ),

                    spacing="4",
                    align="center",
                    padding_x="1rem",
                ),

                width="100%",
                height="100%",
                position="relative",
                z_index="10",
            ),

            position="relative",
            width="100%",
            height="70vh",
            overflow="hidden",
        ),

        # ----------------------------------------
        # POSTS
        # ----------------------------------------

        rx.box(

            rx.vstack(

                rx.heading(
                    "Latest Articles",
                    color=TEXT_WHITE,
                    font_size={
                        "base": "2rem",
                        "md": "3rem",
                    },
                    id="posts",
                ),

                rx.cond(

                    BlogState.posts.length() > 0,

                    rx.grid(

                        rx.foreach(
                            BlogState.posts,
                            blog_card,
                        ),

                        columns={
                            "base": "1",
                            "md": "2",
                        },

                        spacing="6",

                        width="100%",
                    ),

                    rx.center(

                        rx.vstack(

                            rx.heading(
                                "No Blog Posts Yet",
                                color="#D4AF37",
                            ),

                            rx.text(
                                "The first article published from the Admin Dashboard will appear here.",
                                color=TEXT_GRAY,
                                text_align="center",
                            ),

                            spacing="3",
                        ),

                        width="100%",
                        padding_y="80px",
                    ),
                ),

                spacing="8",
                width="100%",
            ),

            width="100%",
            max_width="1200px",
            margin="0 auto",
            padding={
                "base": "25px",
                "md": "50px",
            },

            background=DARK_BG,
        ),

        # ----------------------------------------
        # FOOTER
        # ----------------------------------------

        rx.box(

            rx.text(
                "© 2026 Attih Soul Blog",
                color=TEXT_WHITE,
                font_size="0.75rem",
            ),

            padding="2rem",

            text_align="center",

            border_top="1px solid #222222",

            background=DARK_BG,
        ),
    )