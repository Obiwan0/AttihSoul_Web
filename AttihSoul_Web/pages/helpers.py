import reflex as rx

# ============ THEME ============
GOLD = "#d4a85a"
TEXT_WHITE = "#ffffff"
TEXT_GRAY = "#a1a1a1"
DARK_BG = "#0a0a0a"
CARD_BG = "#111111"

# ============ BREAKPOINT HELPER ============
def bp(initial=None, sm=None, md=None, lg=None, xl=None):
    return rx.breakpoints(initial=initial, sm=sm, md=md, lg=lg, xl=xl)

# ============ VIDEO BACKGROUND ============
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

# ============ OVERLAY ============
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

# ============ GOLD BUTTON ============
def gold_button(text: str, href: str = "#", **kwargs) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.text(
                text,
                color="white",
                font_weight="600",
                font_size=bp(initial="12px", md="16px"),
            ),
            rx.box(
                "→",
                color="white",
                background=GOLD,
                border_radius="50%",
                width="28px",
                height="28px",
                display="flex",
                align_items="center",
                justify_content="center",
                flex_shrink="0",
            ),
            justify_content="space-between",
            align_items="center",
            width="100%",
        ),
        href=href,
        width="100%",
        display="block",
        padding="0.85rem 1.2rem",
        border=f"1px solid {GOLD}",
        border_radius="9999px",
        background="rgba(0,0,0,.25)",
        text_decoration="none",
        box_sizing="border-box",
        _hover={
            "background": "rgba(212,168,90,.15)",
        },
        **kwargs,
    )

# ============ SOCIAL ICONS ============
def social_icons(settings: dict | None = None) -> rx.Component:
    if settings is None:
        settings = {}
    return rx.hstack(
        rx.link("Instagram", href=settings.get("instagram", "https://instagram.com"), color=TEXT_WHITE, _hover={"color": GOLD}),
        rx.link("YouTube", href=settings.get("youtube", "https://youtube.com"), color=TEXT_WHITE, _hover={"color": GOLD}),
        rx.link("TikTok", href=settings.get("tiktok", "https://tiktok.com"), color=TEXT_WHITE, _hover={"color": GOLD}),
        rx.link("Spotify", href=settings.get("spotify", "https://open.spotify.com"), color=TEXT_WHITE, _hover={"color": GOLD}),
        rx.link("X", href=settings.get("x", "https://x.com"), color=TEXT_WHITE, _hover={"color": GOLD}),
        spacing="4",
        padding="0 3rem",
    )

# ============ BRAND LOGO ============
def brand_logo(title: str | None = None) -> rx.Component:
    if title is None:
        title = "Attih Soul"
    return rx.box(
        rx.center(
            rx.text(title, color=GOLD, font_weight="800", font_size="2.2rem", letter_spacing="0.5px"),
        ),
        padding_y="1.5rem",
    )


# ============ YOUTUBE THUMBNAIL ============
def youtube_thumbnail(video_id: str) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.box(
                rx.image(
                    src=f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg",
                    width="100%", border_radius="12px", loading="lazy", transition="transform .35s ease",
                    _hover={"transform": "scale(1.05)"},
                ),
                rx.center(
                    rx.box(
                        rx.icon("play", size=38, color="black"),
                        width="72px", height="72px", background=GOLD, border_radius="50%",
                        display="flex", align_items="center", justify_content="center", transition="all .35s ease",
                        _hover={"transform": "scale(1.1)", "boxShadow": "0 0 45px rgba(212,168,90,.6)"},
                    ),
                    position="absolute", top="0", left="0", width="100%", height="100%",
                ),
                position="relative", cursor="pointer", overflow="hidden", border_radius="12px",
            )
        ),
        rx.dialog.content(
            rx.box(
                rx.el.iframe(
                    src=f"https://www.youtube.com/embed/{video_id}?autoplay=1",
                    width="100%", height="100%", border="0",
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture",
                    allow_full_screen=True,
                ),
                width="100%", style={"aspectRatio": "16 / 9"},
            ),
            max_width="1000px", padding="0", overflow="hidden", border_radius="12px", background="black",
        ),
    )
