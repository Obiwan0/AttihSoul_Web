import reflex as rx

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

                rx.hstack(

                    # ---------------------------
                    # Brand
                    # ---------------------------

                    rx.vstack(

                        rx.heading(
                            "AttihSoul",
                            color=GOLD,
                            size="6",
                        ),

                        rx.text(
                            "Music that inspires. Performances that connect.",
                            color=TEXT_LIGHT,
                            max_width="280px",
                        ),

                        spacing="3",
                        align_items="start",
                    ),

                    rx.spacer(),

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

                        footer_link("Artists", "/artists"),

                        footer_link("Albums", "/albums"),
                        footer_link(
                            "Playlists",
                            "https://open.spotify.com/playlist/7JHI3s5MRSdEOyT5uFpFXt?si=tGjmAvQORmSqyms9P_qxqg",
                        ),

                        spacing="2",
                        align_items="start",
                    ),

                    rx.spacer(),

                    # ---------------------------
                    # Support
                    # ---------------------------

                    rx.vstack(

                        rx.heading(
                            "Support",
                            size="4",
                            color=TEXT,
                        ),

                        footer_link("Help Center"),

                        footer_link("Privacy"),

                        footer_link("Contact"),

                        spacing="2",
                        align_items="start",
                    ),

                    width="100%",
                    align_items="start",

                    flex_wrap="wrap",

                    spacing="9",

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