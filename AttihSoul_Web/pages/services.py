import reflex as rx
from .navbar import navbar
from ..components.footer import footer

# ============ THEME (self-contained) ============
GOLD = "#d4a85a"
TEXT_WHITE = "#ffffff"
TEXT_GRAY = "#a1a1a1"
DARK_BG = "#0a0a0a"
CARD_BG = "#111111"

def bp(initial=None, sm=None, md=None, lg=None, xl=None):
    return rx.breakpoints(initial=initial, sm=sm, md=md, lg=lg, xl=xl)

# ============ HELPERS (self-contained) ============
def video_bg(src: str) -> rx.Component:
    return rx.el.video(
        rx.el.source(src=src, type="video/mp4"),
        auto_play=True,
        loop=True,
        muted=True,
        plays_inline=True,
        style={
            "position": "absolute",
            "top": "0",
            "left": "0",
            "width": "100%",
            "height": "100%",
            "objectFit": "cover",
            "zIndex": "0",
        },
    )

def overlay(color: str) -> rx.Component:
    return rx.box(
        position="absolute",
        top="0",
        left="0",
        width="100%",
        height="100%",
        background=color,
        z_index="1",
    )

def brand_logo() -> rx.Component:
    return rx.box(
        rx.text("", font_size=bp(initial="1.8rem", md="4.5rem"), color=GOLD,
                font_style="italic", font_weight="500", line_height="1"),
        position="absolute",
        top=bp(initial="1rem", md="1rem"),
        right=bp(initial="1rem", md="auto"),
        left=bp(initial="auto", md="50%"),
        transform=bp(initial="none", md="translateX(-50%)"),
        z_index="40",
    )

def gold_button(text: str, href: str = "#") -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.text(text, color="white", font_weight="600", font_size=bp(initial="12px", md="16px")),
            rx.box("→", color="white", background=GOLD, border_radius="50%",
                   width=bp(initial="20px", md="32px"), height=bp(initial="20px", md="32px"),
                   display="flex", align_items="center", justify_content="center",
                   font_size=bp(initial="10px", md="14px")),
            spacing="3", align="center",
            padding=bp(initial="4px 8px", md="0.75rem 1rem"),
        ),
        href=href,
        display="inline-block",
        border=f"1px solid {GOLD}",
        border_radius="9999px",
        background="rgba(0,0,0,0.25)",
        text_decoration="none",
        _hover={"background": "rgba(212,168,90,0.15)"},
    )

# ============ SERVICES PAGE ============
def services_page() -> rx.Component:
    return rx.box(
        navbar(),

        # HERO
        rx.box(
            video_bg("/hero_bg.mp4"),
            overlay("rgba(0,0,0,0.55)"),
            rx.center(
                rx.vstack(
                    rx.text("SERVICES", color=GOLD, font_size="0.9rem", letter_spacing="4px", font_weight="500"),
                    rx.heading(
                        "Music for Concerts, Festivals and Events",
                        font_size=bp(initial="2.4rem", md="4rem", lg="4.6rem"),
                        font_weight="700",
                        color=TEXT_WHITE,
                        text_align="center",
                        line_height="1.05",
                    ),
                    rx.text(
                        "Attih Soul is a brand synonymous with musical excellence, and its essence is captured in the services rendered.",
                        color=TEXT_WHITE,
                        font_size=bp(initial="1rem", md="1.15rem"),
                        text_align="center",
                        max_width="620px",
                    ),
                    rx.box(height="1.5rem"),
                    gold_button("BOOK ATTIH SOUL", "/contact"),
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
            height=bp(initial="90vh", md="100vh"),
            min_height="500px",
            overflow="hidden",
        ),

        brand_logo(),

        # SERVICES INTRO
        rx.box(
            rx.vstack(
                rx.text("WHAT WE OFFER", color=GOLD, font_size="0.85rem", letter_spacing="3px"),
                rx.heading("Our Services", color=TEXT_WHITE, font_size="2.5rem", font_weight="700"),
                rx.text(
                    "Attih Soul delivers premium live music experiences and professional music services "
                    "tailored for individuals, couples, and organizations who value excellence.",
                    color=TEXT_GRAY,
                    font_size="1.05rem",
                    max_width="680px",
                ),
                spacing="4",
                align_items="start",
            ),
            padding=bp(initial="3rem 1.25rem", md="5rem 3rem"),
            background=DARK_BG,
        ),

        # CONCERTS & EVENTS
        rx.box(
            rx.vstack(
                rx.text("LIVE PERFORMANCES", color=GOLD, font_size="0.85rem", letter_spacing="3px"),
                rx.heading("Concerts & Events", color=TEXT_WHITE, font_size="2.3rem", font_weight="600"),
                rx.text(
                    "Attih Soul is available for high-quality live performances across a wide range of events.",
                    color=TEXT_GRAY,
                    font_size="1.05rem",
                    max_width="680px",
                ),
                rx.box(height="1.5rem"),
                rx.grid(
                    rx.box(
                        rx.vstack(
                            rx.text("Weddings & Parties", color=GOLD, font_size="1.1rem", font_weight="600"),
                            rx.text("Create unforgettable memories with soulful live music for your special day.", color=TEXT_GRAY, font_size="0.95rem"),
                            spacing="2",
                        ),
                        bg=CARD_BG, padding="1.5rem", border_radius="12px",
                    ),
                    rx.box(
                        rx.vstack(
                            rx.text("Private Events", color=GOLD, font_size="1.1rem", font_weight="600"),
                            rx.text("Intimate performances for birthdays, anniversaries, and private gatherings.", color=TEXT_GRAY, font_size="0.95rem"),
                            spacing="2",
                        ),
                        bg=CARD_BG, padding="1.5rem", border_radius="12px",
                    ),
                    rx.box(
                        rx.vstack(
                            rx.text("Corporate Events", color=GOLD, font_size="1.1rem", font_weight="600"),
                            rx.text("Professional entertainment for galas, conferences, product launches and more.", color=TEXT_GRAY, font_size="0.95rem"),
                            spacing="2",
                        ),
                        bg=CARD_BG, padding="1.5rem", border_radius="12px",
                    ),
                    rx.box(
                        rx.vstack(
                            rx.text("Festivals & Concerts", color=GOLD, font_size="1.1rem", font_weight="600"),
                            rx.text("Powerful stage presence for festivals, concerts and large public events.", color=TEXT_GRAY, font_size="0.95rem"),
                            spacing="2",
                        ),
                        bg=CARD_BG, padding="1.5rem", border_radius="12px",
                    ),
                    columns={"base": "1", "md": "2"},
                    spacing="6",
                    width="100%",
                ),
                spacing="4",
                align_items="start",
            ),
            padding=bp(initial="3rem 1.25rem", md="5rem 3rem"),
            background="#0f0f0f",
        ),

        # VOCAL COACHING
        rx.box(
            rx.vstack(
                rx.text("DEVELOPMENT", color=GOLD, font_size="0.85rem", letter_spacing="3px"),
                rx.heading("Vocal Coaching", color=TEXT_WHITE, font_size="2.3rem", font_weight="600"),
                rx.text(
                    "Attih Soul offers professional vocal coaching and studio services for singers at all levels.",
                    color=TEXT_GRAY,
                    font_size="1.05rem",
                    max_width="680px",
                ),
                rx.box(height="1.5rem"),
                rx.grid(
                    rx.box(
                        rx.vstack(
                            rx.text("Voice Classes", color=GOLD, font_size="1.1rem", font_weight="600"),
                            rx.text("Personalized vocal training for amateur, intermediate and advanced singers.", color=TEXT_GRAY, font_size="0.95rem"),
                            spacing="2",
                        ),
                        bg=CARD_BG, padding="1.5rem", border_radius="12px",
                    ),
                    rx.box(
                        rx.vstack(
                            rx.text("Vocal Arrangement", color=GOLD, font_size="1.1rem", font_weight="600"),
                            rx.text("Harmonies and in-studio vocal directing for recording artists.", color=TEXT_GRAY, font_size="0.95rem"),
                            spacing="2",
                        ),
                        bg=CARD_BG, padding="1.5rem", border_radius="12px",
                    ),
                    columns={"base": "1", "md": "2"},
                    spacing="6",
                    width="100%",
                ),
                spacing="4",
                align_items="start",
            ),
            padding=bp(initial="3rem 1.25rem", md="5rem 3rem"),
            background=DARK_BG,
        ),

        # SONGWRITING
        rx.box(
            rx.vstack(
                rx.text("CREATIVE SERVICES", color=GOLD, font_size="0.85rem", letter_spacing="3px"),
                rx.heading("Songwriting", color=TEXT_WHITE, font_size="2.3rem", font_weight="600"),
                rx.text(
                    "Transform ideas and emotions into compelling lyrics and melodies with our professional songwriting services.",
                    color=TEXT_GRAY,
                    font_size="1.05rem",
                    max_width="680px",
                ),
                rx.box(height="1.5rem"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Whether you're an artist looking for original material, a brand needing a custom song, "
                            "or simply want to bring your story to life through music — Attih Soul crafts songs that connect.",
                            color=TEXT_GRAY,
                            font_size="1.05rem",
                            line_height="1.7",
                        ),
                        spacing="2",
                    ),
                    bg=CARD_BG, padding="2rem", border_radius="12px",
                ),
                spacing="4",
                align_items="start",
            ),
            padding=bp(initial="3rem 1.25rem", md="5rem 3rem"),
            background="#0f0f0f",
        ),

        # FINAL CTA
        rx.box(
            rx.vstack(
                rx.heading("Ready to work with Attih Soul?", color=TEXT_WHITE, font_size="2.3rem", font_weight="600"),
                rx.text(
                    "Let us create an unforgettable musical experience for your next event or project.",
                    color=TEXT_GRAY,
                ),
                rx.box(height="1.25rem"),
                gold_button("MAKE A BOOKING", "/contact"),
                spacing="3",
                align="center",
            ),
            padding=bp(initial="3rem 1.25rem", md="5rem 3rem"),
            background=DARK_BG,
            text_align="center",
        ),

        # FOOTER
        footer(),
    )