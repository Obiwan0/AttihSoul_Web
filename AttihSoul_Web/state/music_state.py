import reflex as rx
import sqlite3

DB_NAME = "music.db"


class MusicState(rx.State):

    title: str = ""
    spotify: str = ""
    youtube: str = ""
    apple_music: str = ""
    cover: str = ""

    songs: list[dict] = []

    @rx.event
    def load_songs(self):
        conn = sqlite3.connect(DB_NAME)

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                title,
                spotify,
                youtube,
                apple_music,
                cover
            FROM songs
            ORDER BY id DESC
        """)

        rows = cursor.fetchall()

        conn.close()

        self.songs = [
            {
                "id": row[0],
                "title": row[1],
                "spotify": row[2],
                "youtube": row[3],
                "apple_music": row[4],
                "cover": row[5],
            }
            for row in rows
        ]

    @rx.event
    def set_title(self, value: str):
        self.title = value

    @rx.event
    def set_spotify(self, value: str):
        self.spotify = value

    @rx.event
    def set_youtube(self, value: str):
        self.youtube = value

    @rx.event
    def set_apple_music(self, value: str):
        self.apple_music = value

    @rx.event
    def set_cover(self, value: str):
        self.cover = value

    @rx.event
    def add_song(self):
        print("ADDING SONG...")
        print(self.title)

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO songs
            (title, spotify, youtube, apple_music, cover)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                self.title,
                self.spotify,
                self.youtube,
                self.apple_music,
                self.cover,
            ),
        )

        conn.commit()

        print("Rows:", cursor.rowcount)

        conn.close()

        self.load_songs()

        print("Songs loaded:", len(self.songs))

        self.title = ""
        self.spotify = ""
        self.youtube = ""
        self.apple_music = ""
        self.cover = ""