import reflex as rx
from ...state.music_state import MusicState

GOLD = "#D4AF37"


def song_card(song: dict):
    is_editing = MusicState.editing_id == song["id"]
    return rx.box(
        rx.cond(
            is_editing,
            # Edit mode
            rx.vstack(
                rx.heading(f"Editing: {song['title']}", color=GOLD, size="5"),
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
                    placeholder="YouTube Link",
                    value=MusicState.youtube,
                    on_change=MusicState.set_youtube,
                    width="100%",
                ),
                rx.input(
                    placeholder="Apple Music Link",
                    value=MusicState.apple_music,
                    on_change=MusicState.set_apple_music,
                    width="100%",
                ),
                rx.input(
                    placeholder="Album Cover Image URL",
                    value=MusicState.cover,
                    on_change=MusicState.set_cover,
                    width="100%",
                ),
                rx.hstack(
                    rx.button("Save", on_click=MusicState.save_edit, background=GOLD, color="black"),
                    rx.button("Cancel", on_click=MusicState.cancel_edit, color_scheme="gray", color="white"),
                    spacing="3",
                ),
                spacing="3",
                width="100%",
                padding="15px",
                background="#1A1A1A",
                border_radius="8px",
            ),
            # View mode
            rx.box(
                rx.hstack(
                    rx.cond(
                        song["cover"] != "",
                        rx.image(
                            src=song["cover"],
                            width="50px",
                            height="50px",
                            object_fit="cover",
                            border_radius="6px",
                        ),
                        rx.box(),
                    ),
                    rx.vstack(
                        rx.text(song["title"], color="white", font_weight="600"),
                        rx.hstack(
                            rx.cond(
                                song["spotify"] != "",
                                rx.link("Spotify", href=song["spotify"], color=GOLD, font_size="0.8rem", is_external=True),
                            ),
                            rx.cond(
                                song["youtube"] != "",
                                rx.link("YouTube", href=song["youtube"], color=GOLD, font_size="0.8rem", is_external=True),
                            ),
                            spacing="2",
                        ),
                        spacing="1",
                        align="start",
                    ),
                    rx.spacer(),
                    rx.button(
                        "Edit",
                        on_click=lambda: MusicState.start_edit(song["id"]),
                        background=GOLD,
                        color="black",
                        size="2",
                    ),
                    rx.button(
                        "Delete",
                        on_click=lambda: MusicState.delete_song(song["id"]),
                        color_scheme="red",
                        size="2",
                        variant="outline",
                    ),
                    spacing="3",
                    width="100%",
                ),
                width="100%",
                padding="10px",
                background="#1A1A1A",
                border="1px solid #333333",
                border_radius="8px",
            ),
        ),
        width="100%",
    )


def music_page():
    return rx.vstack(
        rx.heading("Music Library", color=GOLD, size="6"),
        rx.text("Manage every song that appears on the Artist page.", color="#BBBBBB"),
        rx.divider(),
        # Add new song
        rx.box(
            rx.heading("Add New Song", color=GOLD, size="4"),
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
                placeholder="YouTube Link",
                value=MusicState.youtube,
                on_change=MusicState.set_youtube,
                width="100%",
            ),
            rx.input(
                placeholder="Apple Music Link",
                value=MusicState.apple_music,
                on_change=MusicState.set_apple_music,
                width="100%",
            ),
            rx.input(
                placeholder="Album Cover Image URL",
                value=MusicState.cover,
                on_change=MusicState.set_cover,
                width="100%",
            ),
            rx.button(
                "Add Song",
                on_click=MusicState.add_song,
                background=GOLD,
                color="black",
                width={"base": "100%", "sm": "220px"},
            ),
            spacing="4",
            width="100%",
            padding="20px",
            background="#111111",
            border="1px solid #333333",
            border_radius="8px",
        ),
        rx.divider(),
        rx.heading("Saved Songs", color=GOLD, size="4"),
        rx.foreach(MusicState.songs, song_card),
        spacing="5",
        width="100%",
        align="stretch",
    )
