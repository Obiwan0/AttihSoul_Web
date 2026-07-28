import reflex as rx
from ..state.settings_state import SettingsState
from ..state.booking_state import BookingState

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
                        "Get in Touch",
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
                        "Let's make your event unforgettable.",
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
                    placeholder="Full Name",
                    value=BookingState.name,
                    on_change=BookingState.set_name,
                    width="100%",
                    size="3",
                ),

                rx.input(
                    placeholder="Email Address",
                    type="email",
                    value=BookingState.email,
                    on_change=BookingState.set_email,
                    width="100%",
                    size="3",
                ),

                rx.input(
                    placeholder="Phone Number",
                    value=BookingState.phone,
                    on_change=BookingState.set_phone,
                    width="100%",
                    size="3",
                ),

                rx.input(
                    placeholder="Event Type (e.g. Wedding, Concert, Corporate)",
                    value=BookingState.event_type,
                    on_change=BookingState.set_event_type,
                    width="100%",
                    size="3",
                ),

                rx.input(
                    placeholder="Event Date",
                    value=BookingState.event_date,
                    on_change=BookingState.set_event_date,
                    width="100%",
                    size="3",
                ),

                rx.input(
                    placeholder="Location",
                    value=BookingState.location,
                    on_change=BookingState.set_location,
                    width="100%",
                    size="3",
                ),

                rx.text_area(
                    placeholder="Tell us about your event...",
                    value=BookingState.message,
                    on_change=BookingState.set_message,
                    width="100%",
                    min_height="180px",
                ),

                rx.button(
                    "Send Booking Request",
                    on_click=BookingState.submit_booking,
                    background=GOLD,
                    color="black",
                    width="100%",
                    size="3",
                ),

                rx.cond(
                    BookingState.submitted,
                    rx.text("Booking request sent successfully!", color="#4CAF50", font_weight="600"),
                ),

                spacing="5",
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
