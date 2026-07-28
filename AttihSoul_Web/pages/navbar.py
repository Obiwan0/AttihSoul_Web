import reflex as rx
from .helpers import GOLD, TEXT_WHITE, bp
from ..state.settings_state import SettingsState


class NavbarState(rx.State):
    """Controls mobile drawer open/close."""
    drawer_open: bool = False

    @rx.event
    def toggle_drawer(self):
        self.drawer_open = not self.drawer_open

    @rx.event
    def close_drawer(self):
        self.drawer_open = False


def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            # Brand logo (hidden on mobile when drawer is open)
            rx.box(
                rx.link(
                    rx.text(
                        SettingsState.settings.get("hero_title", "Attih Soul"),
                        color=GOLD,
                        font_weight="700",
                        font_size="1.35rem",
                        font_style="italic",
                    ),
                    href="/",
                    text_decoration="none",
                ),
                display=rx.cond(NavbarState.drawer_open, "none", "block"),
            ),

            rx.spacer(),

            # Desktop navigation (hidden on mobile)
            rx.hstack(
                rx.link("Home", href="/", color=TEXT_WHITE, font_size="0.95rem", _hover={"color": GOLD}),
                rx.link("About", href="/about", color=TEXT_WHITE, font_size="0.95rem", _hover={"color": GOLD}),
                rx.link("Artist", href="/artist", color=TEXT_WHITE, font_size="0.95rem", _hover={"color": GOLD}),
                rx.link("Performer", href="/performer", color=TEXT_WHITE, font_size="0.95rem", _hover={"color": GOLD}),
                rx.link("Services", href="/services", color=TEXT_WHITE, font_size="0.95rem", _hover={"color": GOLD}),
                rx.link("Blog", href="/blog", color=TEXT_WHITE, font_size="0.95rem", _hover={"color": GOLD}),
                spacing="6",
                align="center",
                display=bp(initial="none", lg="flex"),
            ),

            # Contact button (desktop only)
            rx.link(
                rx.text("Contact", color="white", font_weight="600", font_size="0.9rem"),
                href="/contact",
                border=f"1px solid {GOLD}",
                border_radius="9999px",
                padding="0.4rem 1rem",
                background="rgba(0,0,0,0.25)",
                text_decoration="none",
                _hover={"background": "rgba(212,168,90,0.15)"},
                display=bp(initial="none", lg="inline-flex"),
            ),

            # Hamburger button (mobile only)
            rx.box(
                rx.button(
                    rx.cond(
                        NavbarState.drawer_open,
                        rx.icon("x", size=28, color=TEXT_WHITE),
                        rx.icon("menu", size=28, color=TEXT_WHITE),
                    ),
                    on_click=NavbarState.toggle_drawer,
                    background="transparent",
                    border="none",
                    cursor="pointer",
                    padding="0.5rem",
                    _hover={"opacity": "0.8"},
                ),
                display=bp(initial="flex", lg="none"),
                align_items="center",
            ),

            width="100%",
            align="center",
            justify="between",
            padding_x="2rem",
            padding_y="1rem",
            min_height="5rem",
        ),

        # Mobile drawer overlay
        rx.cond(
            NavbarState.drawer_open,
            rx.box(
                rx.vstack(
                    rx.link("Home", href="/", color=TEXT_WHITE, font_size="1.1rem", on_click=NavbarState.close_drawer, width="100%", padding="0.75rem 1.5rem", _hover={"color": GOLD, "background": "rgba(212,168,90,0.08)"}),
                    rx.link("About", href="/about", color=TEXT_WHITE, font_size="1.1rem", on_click=NavbarState.close_drawer, width="100%", padding="0.75rem 1.5rem", _hover={"color": GOLD, "background": "rgba(212,168,90,0.08)"}),
                    rx.link("Artist", href="/artist", color=TEXT_WHITE, font_size="1.1rem", on_click=NavbarState.close_drawer, width="100%", padding="0.75rem 1.5rem", _hover={"color": GOLD, "background": "rgba(212,168,90,0.08)"}),
                    rx.link("Performer", href="/performer", color=TEXT_WHITE, font_size="1.1rem", on_click=NavbarState.close_drawer, width="100%", padding="0.75rem 1.5rem", _hover={"color": GOLD, "background": "rgba(212,168,90,0.08)"}),
                    rx.link("Services", href="/services", color=TEXT_WHITE, font_size="1.1rem", on_click=NavbarState.close_drawer, width="100%", padding="0.75rem 1.5rem", _hover={"color": GOLD, "background": "rgba(212,168,90,0.08)"}),
                    rx.link("Blog", href="/blog", color=TEXT_WHITE, font_size="1.1rem", on_click=NavbarState.close_drawer, width="100%", padding="0.75rem 1.5rem", _hover={"color": GOLD, "background": "rgba(212,168,90,0.08)"}),
                    rx.link("Contact", href="/contact", color=TEXT_WHITE, font_size="1.1rem", on_click=NavbarState.close_drawer, width="100%", padding="0.75rem 1.5rem", _hover={"color": GOLD, "background": "rgba(212,168,90,0.08)"}),
                    spacing="1",
                    align="start",
                    padding="1.5rem 0",
                    width="100%",
                ),
                position="fixed",
                top="5rem",
                left="0",
                width="100%",
                background="rgba(0,0,0,0.95)",
                z_index="49",
                border_top="1px solid rgba(212,168,90,0.15)",
                animation="fadeIn 0.2s ease",
            ),
        ),

        position="fixed",
        top="0",
        left="0",
        width="100%",
        z_index="50",
        background="transparent",
        backdrop_filter="none",
        border_bottom="none",
        transition="all .35s ease",
    )