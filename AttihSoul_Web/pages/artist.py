import reflex as rx
from ..state.settings_state import SettingsState
from ..state.music_state import MusicState
from ..state.gallery_state import GalleryState
from .navbar import navbar
from ..components.footer import footer
from .helpers import youtube_thumbnail

# =====================================================
# CONSTANTS & DATA
# =====================================================

GOLD = "#d4a85a"
TEXT_WHITE = "#ffffff"
TEXT_GRAY = "#a1a1a1"
DARK_BG = "#0a0a0a"
CARD_BG = "#111111"


def bp(initial=None, sm=None, md=None, lg=None, xl=None):
    return rx.breakpoints(initial=initial, sm=sm, md=md, lg=lg, xl=xl)

# =====================================================
# COMPONENTS
# =====================================================

def video_bg(src: str):
    return rx.el.video(
        rx.el.source(src=src, type="video/mp4"),
        auto_play=True, loop=True, muted=True, plays_inline=True,
        style={"position": "absolute", "top": "0", "left": "0", "width": "100%", "height": "100%", "objectFit": "cover", "zIndex": "0"},
    )

def overlay(color: str):
    return rx.box(position="absolute", top="0", left="0", width="100%", height="100%", background=color, z_index="1")

def social_icons():
    items = [
        ("/instagram.svg", SettingsState.settings.get("instagram", "https://instagram.com/attih_soul")),
        ("/youtube.svg", SettingsState.settings.get("youtube", "https://youtube.com/@attihsoul")),
        ("/spotify.svg", SettingsState.settings.get("spotify", "https://open.spotify.com/artist/5kL7MUEVmuucYk2LsJlrLC")),
        ("/tiktok.svg", SettingsState.settings.get("tiktok", "https://www.tiktok.com/@attihsoul")),
        ("/x.svg", SettingsState.settings.get("x", "https://x.com/attihsoul")),
    ]
    return rx.hstack(
        *[rx.link(rx.image(src=icon, width="22px", style={"filter": "brightness(0) invert(1)"}), href=url, is_external=True) for icon, url in items],
        spacing="4", justify="center",
    )

def gold_button(text, href="#"):
    return rx.link(
        rx.hstack(
            rx.text(text, color="white", font_weight="600"),
            rx.box("→", background=GOLD, color="black", border_radius="50%", width="34px", height="34px", display="flex", align_items="center", justify_content="center", font_weight="700"),
            spacing="3",
        ),
        href=href, border=f"1px solid {GOLD}", border_radius="9999px", padding="0.8rem 1.25rem", text_decoration="none", transition="all .3s ease",
        _hover={"background": GOLD, "transform": "translateY(-2px)"},
    )

def music_card(title, year, img, link):
    return rx.link(
        rx.box(
            rx.vstack(
                rx.image(src=img, width="100%", height="220px", object_fit="cover", border_radius="10px"),
                rx.heading(title, size="4", color=TEXT_WHITE),
                rx.text(year, color=TEXT_GRAY),
                spacing="3", align="start", width="100%",
            ),
            bg=CARD_BG, padding="1rem", border_radius="14px", width="100%", transition="all .3s ease", 
            _hover={"transform": "translateY(-6px)", "boxShadow": "0 15px 40px rgba(212,168,90,.20)"},
        ),
        href=link, is_external=True, text_decoration="none", width="100%",
    )

def song_card_from_state(song: dict):
    """Render a song from MusicState."""
    return rx.link(
        rx.hstack(
            rx.text(song["title"], flex="1", color=TEXT_WHITE, font_weight="600"),
            rx.hstack(
                rx.cond(song["spotify"] != "", rx.text("Spotify", color=GOLD, font_size="0.8rem")),
                rx.cond(song["youtube"] != "", rx.text("YouTube", color=GOLD, font_size="0.8rem")),
                spacing="2",
            ),
        ),
        href=rx.cond(song["spotify"] != "", song["spotify"], rx.cond(song["youtube"] != "", song["youtube"], "#")),
        is_external=True, text_decoration="none", width="100%", padding="14px 18px", border_radius="4px", transition="all .25s ease",
        _hover={"background": "#181818", "transform": "translateX(6px)", "borderLeft": f"3px solid {GOLD}"},
    )

# =====================================================
# MAIN PAGE
# =====================================================

def artist_page():
    return rx.box(
        navbar(),
        # HERO
        rx.box(
            video_bg("/inside artist background hero section(1)(1).mp4"),
            overlay("rgba(0,0,0,.45)"),
            rx.center(
                rx.vstack(
                    rx.text("ARTIST", color=GOLD, text_align="center", letter_spacing="0.1em", font_size="0.9rem"),
                    rx.heading("ATTIH SOUL", color="white", font_size=bp(initial="36px", md="5rem"), text_align="center", width="100%"),
                    rx.text("Step into the sound, the story, and the soul of Attih Soul.", color="white", text_align="center", max_width=bp(initial="300px", sm="340px", md="600px"), margin_x="auto"),
                    rx.center(gold_button("Explore Music", "#music"), width="100%"),
                    spacing="5", align="center", width="100%",
                ),
                width="100%", height="100%", position="relative", z_index="10", padding_x=bp(initial="20px", sm="30px", md="60px"), align="center", justify="center",
            ),
            height=bp(initial="90vh", md="100vh"), position="relative",
        ),
        # POPULAR SONGS
        rx.box(
            rx.container(
                rx.vstack(
                    rx.text("POPULAR SONGS", color=GOLD, font_weight="700", letter_spacing="2px"),
                    rx.cond(
                        MusicState.songs.length() > 0,
                        rx.vstack(
                            rx.foreach(MusicState.songs, song_card_from_state),
                            spacing="2", align="stretch", width="100%",
                        ),
                        rx.text("No songs yet. Add songs from the Admin Dashboard.", color=TEXT_GRAY, text_align="center"),
                    ),
                    spacing="2", align="stretch", width="100%",
                ),
                max_width="1100px",
            ),
            id="music", background=DARK_BG, padding=bp(initial="3rem 1.5rem", md="4rem 3rem"),
        ),
        # DISCOGRAPHY
        rx.box(
            rx.container(
                rx.vstack(
                    rx.heading("Discography", color=TEXT_WHITE, width="100%", text_align=bp(initial="center", md="left")),
                    rx.grid(
                        music_card("All In My Head", "2025", "/album cover/Ph-29.jpg", "https://distrokid.com/hyperfollow/attihsoul/all-in-my-head-2"),
                        music_card("Dreams (Choir Version)", "2025", "/album cover/card 1.jpg", "https://distrokid.com/hyperfollow/attihsoul/dreams-choir-version"),
                        music_card("Good Old Days", "2025", "/album cover/card 2.jpg", "https://distrokid.com/hyperfollow/attihsoul/good-old-days-choir-version"),
                        music_card("Healed Too Much", "2025", "/album cover/card 3.jpg", "https://distrokid.com/hyperfollow/attihsoul/healed-too-much-choir-version"),
                        music_card("Shades of Emotions", "2025", "/album cover/card 4.jpg", "https://distrokid.com/hyperfollow/attihsoul/shades-of-emotions-2"),
                        music_card("The Acoustic Experiment", "2024", "/album cover/card 5.jpg", "https://distrokid.com/hyperfollow/attihsoul/the-acoustic-experiment"),
                        music_card("Kiss Ya (Live)", "2024", "/album cover/card 6.jpg", "https://distrokid.com/hyperfollow/attihsoul/kiss-ya-live-at-estudio-tanger-barcelona"),
                        columns=bp(initial="1", sm="2", md="3", lg="4"), spacing="6", width="100%", justify_items="center", align_items="stretch",
                    ),
                    # FEATURED VISUALS
                    rx.box(
                        rx.heading("Latest Visuals", color=TEXT_WHITE, size="5", width="100%", text_align=bp(initial="center", md="left")),
                        rx.text("Watch Attih Soul's latest official visuals and experience the music beyond audio.", color=TEXT_GRAY, max_width="650px", width="100%", text_align=bp(initial="center", md="left"), margin_bottom="2rem"),
                        rx.cond(
                            GalleryState.artist_videos.length() > 0,
                            rx.grid(
                                rx.foreach(
                                    GalleryState.artist_videos,
                                    lambda item: rx.box(
                                        rx.cond(
                                            item["media_type"] == "video",
                                            rx.box(
                                                youtube_thumbnail(item["src"]),
                                                rx.box(
                                                    rx.text(item["title"], color=TEXT_WHITE, font_weight="600", padding="1rem 0.5rem 0.5rem"),
                                                ),
                                                width="100%",
                                                bg=CARD_BG,
                                                border_radius="14px",
                                                overflow="hidden",
                                                _hover={
                                                    "transform": "translateY(-6px)",
                                                    "boxShadow": "0 15px 40px rgba(212,168,90,.18)",
                                                },
                                                transition="all .3s ease",
                                            ),
                                        ),
                                    ),
                                ),
                                columns=bp(initial="1", sm="2", md="3"),
                                spacing="6",
                                width="100%",
                            ),
                            rx.text("Music videos coming soon.", color=TEXT_GRAY),
                        ),
                        padding_top="5rem", width="100%",
                    ),
                    spacing="6", width="100%",
                ),
                max_width="1200px",
            ),
            padding=bp(initial="3rem 1.5rem", md="4rem 3rem"),
            background="#0d0d0d",
        ),
        # ABOUT
        rx.box(
            rx.container(
                rx.vstack(
                    rx.heading("About Attih Soul", color=TEXT_WHITE, width="100%", text_align=bp(initial="center", md="left")),
                    rx.text("Attih Soul is a Nigerian Afro-Soul artist whose music blends soul, R&B, Afro influences, and cinematic storytelling into emotionally rich experiences. Every release explores themes of love, healing, identity, and human connection, creating music that resonates far beyond the first listen.", color=TEXT_GRAY, max_width="850px", line_height="1.8", font_size="1.05rem"),
                    spacing="5", width="100%", align_items=bp(initial="center", md="start"), text_align=bp(initial="center", md="left"),
                ),
                max_width="1100px",
            ),
            padding=bp(initial="4rem 1.5rem", md="5rem 3rem"),
            background=DARK_BG,
        ),
        # STAY CONNECTED
        rx.box(
            rx.container(
                rx.vstack(rx.heading("Stay Connected", color=TEXT_WHITE), social_icons(), spacing="4", align="center"),
            ),
            background="#0b0b0b", padding=bp(initial="3rem 1.5rem", md="4rem"),
        ),
        rx.divider(border_color="#222"),
        footer(),
        background=DARK_BG,
        on_mount=[MusicState.load_songs, GalleryState.on_load, SettingsState.load_settings],
    )
