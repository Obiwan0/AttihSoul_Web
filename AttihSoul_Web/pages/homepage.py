import reflex as rx
from ..state.settings_state import SettingsState

GOLD = "#d4a85a"

def bp(initial=None, sm=None, md=None, lg=None, xl=None):
    return rx.breakpoints(initial=initial, sm=sm, md=md, lg=lg, xl=xl)

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
        *[
            rx.link(
                rx.image(
                    src=icon,
                    width=bp(initial="18px", md="24px"),
                    height=bp(initial="18px", md="24px"),
                    style={"filter":"brightness(0) invert(1)"},
                    _hover={"transform":"scale(1.1)"},
                    transition="all .2s ease",
                ),
                href=href,
                is_external=True,
            )
            for icon, href in [
                ("/instagram.svg", SettingsState.settings.get("instagram", "https://www.instagram.com/attih_soul/")),
                ("/youtube.svg", SettingsState.settings.get("youtube", "https://www.youtube.com/channel/UC26rJ72ZSCYK8MfMt3FsFWg")),
                ("/spotify.svg", SettingsState.settings.get("spotify", "https://open.spotify.com/artist/5kL7MUEVmuucYk2LsJlrLC")),
                ("/wikipedia.svg", SettingsState.settings.get("wikipedia", "https://en.wikipedia.org/wiki/Attih_Soul")),
            ]
        ],
        spacing="3",
        position="absolute",
        top=bp(initial="12px", md="1.5rem"),
        left=bp(initial="12px", md="1.5rem"),
        z_index="40",
    )

def brand_logo() -> rx.Component:
    return rx.box(
        rx.text(
            "Attih Soul",
            font_size=bp(initial="1.8rem", md="4.5rem"),
            color=GOLD,
            font_style="italic",
            font_weight="500",
        ),
        position="absolute",
        top="1rem",
        right=bp(initial="1rem", md="auto"),
        left=bp(initial="auto", md="50%"),
        transform=bp(initial="none", md="translateX(-50%)"),
        z_index="40",
    )

def center_badge():
    return rx.box(
        rx.center(rx.text("A", color=GOLD, font_size=bp(initial="2rem", md="4rem"), font_style="italic")),
        width=bp(initial="70px", md="120px"),
        height=bp(initial="70px", md="120px"),
        border_radius="50%",
        background="black",
        border=f"2px solid {GOLD}",
        position="absolute",
        top="50%",
        left="50%",
        transform="translate(-50%, -50%)",
        z_index="25",
    )

def explore_button(text, href):
    return rx.link(
        rx.hstack(
            rx.text(text, color="white", font_weight="600"),
            rx.box("→", color="white", background=GOLD, border_radius="50%", width="32px", height="32px",
                   display="flex", align_items="center", justify_content="center"),
            spacing="3",
        ),
        href=href,
        border=f"1px solid {GOLD}",
        border_radius="9999px",
        padding="0.75rem 1rem",
        text_decoration="none",
    )

def side_panel(title, top_icon, label, features, button_text, video_src, href, dark):
    return rx.box(
        video_bg(video_src),
        overlay(dark),
        rx.center(
            rx.vstack(
                rx.heading(title, color="white", font_size=bp(initial="24px", md="4rem"), text_align="center"),
                rx.text(
                    label,
                    color="white",
                    font_family="Georgia, serif",
                    font_size=bp(initial="10px", md="14px"),
                    letter_spacing="2px",
                    text_align="center",
                ),
                rx.divider(border_color=GOLD, width="42%"),
                rx.vstack(
                    *[
                        rx.hstack(
                            rx.icon(icon, size=20, color=GOLD),
                            rx.text(text, color="white", font_size=bp(initial="13px", md="16px")),
                            spacing="2",
                            align_items="center",
                        )
                        for icon, text in features
                    ],
                    spacing="2",
                    align="center",
                ),
                explore_button(button_text, href),
                spacing="4",
                align="center",
            ),
            width="100%",
            height="100%",
            position="relative",
            z_index="10",
        ),
        position="relative",
        width=bp(initial="100%", md="50%"),
        height=bp(initial="50vh", md="100vh"),
        overflow="hidden",
    )

def homepage() -> rx.Component:
    return rx.box(
        rx.flex(
            side_panel(
                "THE ARTIST",
                "music",
                "ORIGINAL MUSIC",
                [("music", "Original Songs"), ("play", "Music Videos"), ("ticket", "Live Shows")],
                "LISTEN & DISCOVER",
                "/artist_bg.mp4",
                "/artist",
                "rgba(0,0,0,0.45)",
            ),
            side_panel(
                "THE PERFORMER",
                "mic",
                "LIVE PERFORMANCES",
                [("heart", "Weddings"), ("building", "Corporate Events"), ("sparkles", "Private Events")],
                "EXPLORE MORE",
                "/performer_bg.mp4",
                "/performer",
                "rgba(0,0,0,0.35)",
            ),
            direction=bp(initial="column", md="row"),
            width="100%",
            min_height="100vh",
        ),
        social_icons(),
        brand_logo(),
        rx.box(center_badge(), display=bp(initial="none", md="block")),
        rx.box(
            rx.text("TWO SIDES, ONE VOICE.", color="white", font_size=bp(initial="10px", md="1rem"),
                    font_weight="600", letter_spacing="0.15em"),
            position="absolute",
            bottom=bp(initial="8px", md="2rem"),
            left="50%",
            transform="translateX(-50%)",
            z_index="40",
        ),
        width="100%",
        max_width="100vw",
        min_height="100vh",
        position="relative",
        overflow_x="hidden",
        background="black",
        on_mount=SettingsState.load_settings,
    )
