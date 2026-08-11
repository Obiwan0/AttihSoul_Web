import reflex as rx
from ..state.settings_state import SettingsState
from ..pages.helpers import bp

# =========================
# COLORS
# =========================

BACKGROUND = "#050505"
CARD = "#111111"
BORDER = "#1B1B1B"

GOLD = "#D4AF37"
TEXT = "#FFFFFF"
TEXT_LIGHT = "#B3B3B3"


def footer_link(text: str, href: str = "#") -> rx.Component:
    return rx.link(
        text,
        href=href,
        color=TEXT_LIGHT,
        text_decoration="none",
        font_size="0.95rem",
        _hover={
            "color": GOLD,
        },
    )


def footer():

    return rx.box(

        rx.divider(border_color=BORDER),

        rx.container(

            rx.vstack(

            rx.grid(

                # ---------------------------
                # Brand
                # ---------------------------

                rx.vstack(

                    rx.heading(
                        SettingsState.settings.get("hero_title", "AttihSoul"),
                        color=GOLD,
                        size="6",
                    ),

                    rx.text(
                        SettingsState.settings.get("hero_subtitle", "Music that inspires. Performances that connect."),
                        color=TEXT_LIGHT,
                        max_width="280px",
                    ),

                    spacing="3",
                    align_items=bp(initial="center", md="start"),
                    width="100%",
                ),

                # ---------------------------
                # Quick Links
                # ---------------------------

                rx.vstack(

                    rx.heading(
                        "Quick Links",
                        size="4",
                        color=TEXT,
                    ),

                    footer_link("Home", "/"),
                    footer_link("Artist", "/artist"),
                    footer_link("Performer", "/performer"),
                    footer_link("Blog", "/blog"),

                    spacing="2",
                    align_items=bp(initial="center", md="start"),
                    width="100%",
                ),

                # ---------------------------
                # Connect
                # ---------------------------

                rx.vstack(

                    rx.heading(
                        "Connect",
                        size="4",
                        color=TEXT,
                    ),

                    footer_link("Instagram", SettingsState.settings.get("instagram", "https://instagram.com")),
                    footer_link("YouTube", SettingsState.settings.get("youtube", "https://youtube.com")),
                    footer_link("Spotify", SettingsState.settings.get("spotify", "https://open.spotify.com")),
                    footer_link(
                        "VEVO",
                        "https://youtube.com/@attihsoulvevo200?si=zPlwBTiER-7TJ5Oe",
                    ),
                    footer_link("Contact", "/contact"),

                    spacing="2",
                    align_items=bp(initial="center", md="start"),
                    width="100%",
                ),

                columns=bp(initial="1", md="3"),
                spacing="9",
                width="100%",

            ),

                rx.divider(border_color=BORDER),

                rx.hstack(

                    rx.text(
                        "© 2026 AttihSoul. All Rights Reserved.",
                        color=TEXT_LIGHT,
                        font_size="0.9rem",
                    ),

                    rx.spacer(),

                    width="100%",

                ),

                spacing="8",

                width="100%",

            ),

            max_width="1400px",

            padding_y="4rem",

            padding_x="2rem",

        ),

        bg=BACKGROUND,

        width="100%",

        margin_top="5rem",

    )