import reflex as rx
from .helpers import GOLD, TEXT_WHITE, bp


def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            # Brand logo
                rx.link(
                rx.text(
                    "Attih Soul",
                    color=GOLD,
                    font_weight="700",
                    font_size="1.35rem",
                    font_style="italic",
                ),
                href="/",
                text_decoration="none",
            ),

            rx.spacer(),

            # Desktop navigation
            rx.hstack(
                rx.link(
                    "Home",
                    href="/",
                    color=TEXT_WHITE,
                    font_size="0.95rem",
                    _hover={"color": GOLD},
                ),
                rx.link(
                    "About",
                    href="/about",
                    color=TEXT_WHITE,
                    font_size="0.95rem",
                    _hover={"color": GOLD},
                ),
                rx.link(
                    "Artist",
                    href="/artist",
                    color=TEXT_WHITE,
                    font_size="0.95rem",
                    _hover={"color": GOLD},
                ),
                rx.link(
                    "Performer",
                    href="/performer",
                    color=TEXT_WHITE,
                    font_size="0.95rem",
                    _hover={"color": GOLD},
                ),
                rx.link(
                    "Services",
                    href="/services",
                    color=TEXT_WHITE,
                    font_size="0.95rem",
                    _hover={"color": GOLD},
                ),
                rx.link(
                    "Blog",
                    href="/blog",
                    color=TEXT_WHITE,
                    font_size="0.95rem",
                    _hover={"color": GOLD},
                ),
                spacing="6",
                align="center",
                display=bp(
                    initial="none",
                    lg="flex",
                ),
            ),

            # Contact button
            rx.link(
                rx.text(
                    "Contact",
                    color="white",
                    font_weight="600",
                    font_size="0.9rem",
                ),
                href="/contact",
                border=f"1px solid {GOLD}",
                border_radius="9999px",
                padding="0.4rem 1rem",
                background="rgba(0,0,0,0.25)",
                text_decoration="none",
                _hover={
                    "background": "rgba(212,168,90,0.15)"
                },
                display=bp(
                    initial="none",
                    lg="inline-flex",
                ),
            ),

            # Mobile hamburger
            rx.box(
                rx.drawer.root(
                    rx.drawer.trigger(
                        rx.icon(
                            tag="menu",
                            color=TEXT_WHITE,
                            size=28,
                        ),
                    ),
                    rx.drawer.content(
                        rx.vstack(
                            rx.link("Home", href="/", color=TEXT_WHITE),
                            rx.link("About", href="/about", color=TEXT_WHITE),
                            rx.link("Artist", href="/artist", color=TEXT_WHITE),
                            rx.link("Performer", href="/performer", color=TEXT_WHITE),
                            rx.link("Services", href="/services", color=TEXT_WHITE),
                            rx.link("Blog", href="/blog", color=TEXT_WHITE),
                            rx.link("Contact", href="/contact", color=TEXT_WHITE),
                            spacing="4",
                            align="start",
                            padding="1.5rem",
                        ),
                        side="left",
                        background="rgba(0,0,0,0.92)",
                    ),
                ),
                display=bp(
                    initial="flex",
                    lg="none",
                ),
            ),

            width="100%",
            align="center",
            justify="between",
            padding_x="2rem",
            padding_y="1rem",
            min_height="5rem",
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