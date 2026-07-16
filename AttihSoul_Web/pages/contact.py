import reflex as rx

from .navbar import navbar
from ..components.footer import footer
from .helpers import (
    overlay,
    GOLD,
    DARK_BG,
)


def contact_page() -> rx.Component:
    return rx.box(

        # -------------------------
        # Navbar
        # -------------------------
        navbar(),

        # -------------------------
        # Hero Section
        # -------------------------
        rx.box(

            rx.image(
                src="/conpic.jpg",
                width="100%",
                height="100%",
                object_fit="cover",
                position="absolute",
                top="0",
                left="0",
            ),

            overlay("rgba(0,0,0,0.55)"),

            rx.center(

                rx.vstack(

                    rx.heading(
                        "",
                        color="white",
                        font_weight="800",
                        text_align="center",
                        font_size={
                            "base": "1.8rem",
                            "md": "4rem",
                        },
                        line_height="1.1",
                        width="100%",
                    ),

                    rx.text(
                        "",
                        color="white",
                        text_align="center",
                        font_size={
                            "base": "0.9rem",
                            "md": "1.15rem",
                        },
                        max_width={
                            "base": "85%",
                            "md": "500px",
                        },
                        margin="0 auto",
                        line_height="1.5",
                    ),

                    spacing="3",
                    align_items="center",
                    justify_content="center",
                    width="100%",
                    padding_x={
                        "base": "1.5rem",
                        "md": "1rem",
                    },
                    height="100%",
                    display="flex",
                    flex_direction="column",
                ),

                width="100%",
                height="100%",
                position="relative",
                z_index="10",
            ),

            position="relative",
            width="100%",
            height={
                "base": "55vh",
                "md": "60vh",
            },
            min_height="320px",
            overflow="hidden",
        ),

        # -------------------------
        # Contact Form
        # -------------------------
        rx.box(

            rx.form(

                rx.vstack(

                    rx.heading(
                        "Send a Booking Request",
                        color=GOLD,
                        text_align="center",
                        font_size={
                            "base": "1.6rem",
                            "md": "2rem",
                        },
                        width="100%",
                    ),

                    rx.input(
                        name="name",
                        placeholder="Full Name",
                        width="100%",
                        size="3",
                    ),

                    rx.input(
                        name="email",
                        placeholder="Email Address",
                        type="email",
                        width="100%",
                        size="3",
                    ),

                    rx.input(
                        name="phone",
                        placeholder="Phone Number",
                        width="100%",
                        size="3",
                    ),

                    rx.input(
                        name="subject",
                        placeholder="Subject",
                        width="100%",
                        size="3",
                    ),

                    rx.text_area(
                        name="body",
                        placeholder="Tell us about your event...",
                        width="100%",
                        min_height="180px",
                    ),

                    rx.button(
                        "Send Booking Request",
                        type="submit",
                        background=GOLD,
                        color="black",
                        width="100%",
                        size="3",
                    ),

                    spacing="5",
                    width="100%",
                ),

                action="mailto:info@attihsoul.com",
                method="post",
                enc_type="text/plain",

                width="100%",
            ),

            width="100%",
            max_width="650px",

            margin="0 auto",

            padding={
                "base": "20px",
                "md": "40px",
            },

            background="#111111",

            border="1px solid #222222",

            border_radius="16px",

            margin_top={
                "base": "30px",
                "md": "60px",
            },

            margin_bottom={
                "base": "40px",
                "md": "70px",
            },
        ),

        # -------------------------
        # Footer
        # -------------------------
        footer(),

        background=DARK_BG,
        min_height="100vh",
    )