import reflex as rx
from ..state.settings_state import SettingsState
from .navbar import navbar

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

def social_icons() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.image(src="/instagram.svg", width=bp(initial="18px", md="24px"), height=bp(initial="18px", md="24px"),
                     style={"filter": "brightness(0) invert(1)"}, _hover={"transform": "scale(1.1)"}),
            href="https://instagram.com/attih_soul", is_external=True),
        rx.link(
            rx.image(src="/youtube.svg", width=bp(initial="18px", md="24px"), height=bp(initial="18px", md="24px"),
                     style={"filter": "brightness(0) invert(1)"}, _hover={"transform": "scale(1.1)"}),
            href="https://youtube.com/@attihsoul", is_external=True),
        rx.link(
            rx.image(src="/spotify.svg", width=bp(initial="18px", md="24px"), height=bp(initial="18px", md="24px"),
                     style={"filter": "brightness(0) invert(1)"}, _hover={"transform": "scale(1.1)"}),
            href="https://open.spotify.com/artist/5kL7MUEVmuucYk2LsJlrLC", is_external=True),
        spacing="3",
        position="absolute",
        top=bp(initial="12px", md="1.5rem"),
        left=bp(initial="12px", md="1.5rem"),
        z_index="40",
    )

def brand_logo() -> rx.Component:
    return rx.box(
        rx.text("AttihSoul", font_size=bp(initial="1.8rem", md="4.5rem"), color=GOLD,
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

# ============ ABOUT PAGE (SEO content from https://attihsoul.com/about/) ============
def about_page() -> rx.Component:
    return rx.box(
        navbar(),

        # HERO
        rx.box(
            video_bg("/hero_bg.mp4"),
            overlay("rgba(0,0,0,0.55)"),

            rx.center(
                rx.vstack(
                    rx.heading(
                        "About Attih Soul",
                        font_size=bp(initial="2.8rem", md="4.5rem", lg="5.2rem"),
                        font_weight="700",
                        color=TEXT_WHITE,
                        text_align="center",
                        line_height="1.05",
                    ),
                    rx.cond(
                        SettingsState.about_intro != "",
                        rx.text(
                            SettingsState.about_intro,
                            color=TEXT_WHITE,
                            font_size=bp(initial="1rem", md="1.15rem"),
                            text_align="center",
                            max_width="620px",
                        ),
                        rx.text(
                            "Barcelona based Soul and R&B Artist available for bookings for Concerts, Festivals, Weddings, Galas and Parties worldwide",
                            color=TEXT_WHITE,
                            font_size=bp(initial="1rem", md="1.15rem"),
                            text_align="center",
                            max_width="620px",
                        ),
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
            height="100vh",
            overflow="hidden",
        ),

        # BIOGRAPHY
        rx.box(
            rx.vstack(
                rx.text("BIOGRAPHY", color=GOLD, font_size="0.85rem", letter_spacing="3px"),
                rx.heading("ABOUT ATTIH SOUL", color=TEXT_WHITE, font_size="2.6rem", font_weight="700", line_height="1.1"),
                rx.text("Soul. Story. Connection.", color=TEXT_WHITE, font_size="1.25rem", font_weight="500"),
                rx.text(
                    "Attih Soul is a Barcelona-based Soul & R&B artist, songwriter and live performer known for powerful vocals, emotional storytelling and sophisticated live entertainment.",
                    color=TEXT_GRAY, font_size="1.05rem", line_height="1.7", max_width="720px",
                ),
                rx.text(
                    "Blending the warmth of classic soul with contemporary R&B, his music and performances are built around one thing: creating a genuine connection with the audience.",
                    color=TEXT_GRAY, font_size="1.05rem", line_height="1.7", max_width="720px",
                ),
                rx.text(
                    "Originally from Nigeria and now based in Barcelona, Attih Soul performs across Europe and internationally, bringing his distinctive sound to concerts, music festivals, weddings, luxury events and private celebrations.",
                    color=TEXT_GRAY, font_size="1.05rem", line_height="1.7", max_width="720px",
                ),
                spacing="5", align_items="start",
            ),
            padding="5rem 3rem", background=DARK_BG,
        ),

        # CAREER HIGHLIGHTS
        rx.box(
            rx.vstack(
                rx.text("CAREER HIGHLIGHTS", color=GOLD, font_size="0.85rem", letter_spacing="3px"),
                rx.box(height="2rem"),
                rx.grid(
                    rx.box(
                        rx.vstack(
                            rx.text("Road to Yalta International Music Festival", color=GOLD, font_size="1.1rem", font_weight="600"),
                            rx.text("Award for Outstanding Stage Performance", color=TEXT_WHITE, font_size="1rem"),
                            spacing="2",
                        ),
                        bg=CARD_BG, padding="1.75rem", border_radius="12px",
                    ),
                    rx.box(
                        rx.vstack(
                            rx.text("National Recognition", color=GOLD, font_size="1.1rem", font_weight="600"),
                            rx.text("Creator of Nigeria's Democracy Day Theme Song (2017)", color=TEXT_WHITE, font_size="1rem"),
                            spacing="2",
                        ),
                        bg=CARD_BG, padding="1.75rem", border_radius="12px",
                    ),
                    rx.box(
                        rx.vstack(
                            rx.text("High-Profile Performances", color=GOLD, font_size="1.1rem", font_weight="600"),
                            rx.text("For elite clients and audiences, including FC Barcelona star Lamine Yamal.", color=TEXT_WHITE, font_size="1rem"),
                            spacing="2",
                        ),
                        bg=CARD_BG, padding="1.75rem", border_radius="12px",
                    ),
                    columns={"base": "1", "md": "3"}, spacing="6", width="100%",
                ),
                spacing="4", align_items="start",
            ),
            padding="5rem 3rem", background="#0f0f0f",
        ),


        
        rx.box(
            rx.vstack(
                rx.heading("", color=TEXT_WHITE, font_size="2.4rem", font_weight="600"),
                rx.text(
                    " "
                    " ",
                    color=TEXT_GRAY, font_size="1.05rem", max_width="620px",
                ),
                rx.box(height="1.5rem"),
                rx.image(
                    src="yamal.jpeg",
                    width="100%", max_width="820px", border_radius="12px",
                    style={"boxShadow": "0 10px 30px rgba(0,0,0,0.4)"},
                ),
                rx.text("Attih Soul with Lamine Yamal", color=TEXT_GRAY, font_size="0.9rem", font_style="italic", margin_top="0.75rem"),
                spacing="4", align="center",
            ),
            padding="5rem 3rem", background=DARK_BG, text_align="center",
        ),

        # APPROACH
        rx.box(
            rx.vstack(
                rx.text("THE APPROACH", color=GOLD, font_size="0.85rem", letter_spacing="3px"),
                rx.heading("Authenticity. Reliability. Excellence.", color=TEXT_WHITE, font_size="2.3rem", font_weight="600", line_height="1.15"),
                rx.text(
                    "With a background in leadership and talent development, Attih Soul brings a refined and intentional "
                    "approach to his artistry. His brand is built on authenticity, reliability, and excellence — qualities "
                    "that ensure every performance meets the highest standard.",
                    color=TEXT_GRAY, font_size="1.05rem", line_height="1.7", max_width="720px",
                ),
                rx.box(height="1rem"),
                rx.text(
                    "His projects, including Shades of Emotions and The Acoustic Experiment, showcase a signature fusion of "
                    "soul, R&B, and modern influences, continuing to captivate audiences worldwide.",
                    color=TEXT_GRAY, font_size="1.05rem", line_height="1.7", max_width="720px",
                ),
                spacing="4", align_items="start",
            ),
            padding="5rem 3rem", background="#0f0f0f",
        ),

        # CTA
        rx.box(
            rx.vstack(
                rx.heading("Ready to experience Attih Soul?", color=TEXT_WHITE, font_size="2.3rem", font_weight="600"),
                rx.text("Available for concerts, festivals, weddings, galas, and private events worldwide.", color=TEXT_GRAY, font_size="1.05rem"),
                rx.box(height="1.25rem"),
                gold_button("INQUIRE NOW", "/contact"),
                spacing="3", align="center",
            ),
            padding="5rem 3rem", background=DARK_BG, text_align="center",
        ),

        # FOOTER
        rx.box(
            rx.text("TWO SIDES. ONE VOICE.", color=TEXT_WHITE, font_size="0.75rem", letter_spacing="0.15em"),
            padding="2rem", text_align="center", border_top="1px solid #222", background=DARK_BG,
        ),
        on_mount=SettingsState.load_settings,
    )