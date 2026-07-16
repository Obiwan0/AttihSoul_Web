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
def social_icons() -> rx.Component:
    return rx.hstack(
        rx.link("Instagram", href="https://instagram.com", color=TEXT_WHITE, _hover={"color": GOLD}),
        rx.link("YouTube", href="https://youtube.com", color=TEXT_WHITE, _hover={"color": GOLD}),
        rx.link("TikTok", href="https://tiktok.com", color=TEXT_WHITE, _hover={"color": GOLD}),
        spacing="4",
        padding="0 3rem",
    )

# ============ BRAND LOGO ============
def brand_logo() -> rx.Component:
    return rx.box(
        rx.center(
            rx.text("Attih Soul", color=GOLD, font_weight="800", font_size="2.2rem", letter_spacing="0.5px"),
        ),
        padding_y="1.5rem",
    )