import reflex as rx
from ...state.music_state import MusicState

def song_card(song: dict):
    return rx.box(
        rx.hstack(
            rx.text(song["title"], color="white"),
            rx.spacer(),
            rx.text(song["spotify"], color="#BBBBBB", font_size="0.8rem"),
            spacing="4",
        ),
        width="100%",
        padding="10px",
        border="1px solid #333333",
        border_radius="8px",
    )

def music_page():
    return rx.vstack(

        rx.heading(
            "Music Library",
            color="#D4AF37",
            size="6",
        ),

        rx.text(
            "Manage every song that appears on the Artist page.",
            color="#BBBBBB",
        ),

        rx.input(
            placeholder="Song Title",
            value=MusicState.title,
            on_change=MusicState.set_title,
            width="100%",
        ),

        rx.input(
            placeholder="Spotify Link",
            value=MusicState.spotify,
            on_change=MusicState.set_spotify,
            width="100%",
        ),

        rx.input(
            placeholder="Apple Music Link",
            value=MusicState.apple_music,
            on_change=MusicState.set_apple_music,
            width="100%",
        ),

        rx.input(
            placeholder="YouTube Link",
            value=MusicState.youtube,
            on_change=MusicState.set_youtube,
            width="100%",
        ),

        rx.input(
            placeholder="Album Cover Image",
            value=MusicState.cover,
            on_change=MusicState.set_cover,
            width="100%",
        ),

        rx.button(
            "Add Song",
            on_click=MusicState.add_song,
            background="#D4AF37",
            color="black",
            width={
                "base": "100%",
                "sm": "220px",
            },
        ),
        
        rx.divider(),
        
        rx.heading(
            "Saved Songs",
            color="#D4AF37",
        ),
        
        rx.foreach(
            MusicState.songs,
            song_card,
        ),

        spacing="5",
        width="100%",
        align="stretch",

        on_mount=MusicState.load_songs,
    )