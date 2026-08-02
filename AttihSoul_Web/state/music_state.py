import reflex as rx
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DB_NAME = BASE_DIR / "database" / "music.db"

from ..database.music_dp import init_music_db
init_music_db()


class MusicState(rx.State):

    title: str = ""
    spotify: str = ""
    youtube: str = ""
    apple_music: str = ""
    cover: str = ""
    editing_id: int | None = None

    songs: list[dict] = []

    @rx.event
    def load_songs(self):
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, title, spotify, youtube, apple_music, cover
            FROM songs
            ORDER BY id DESC
        """)
        self.songs = [dict(r) for r in cursor.fetchall()]
        conn.close()

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
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO songs(title, spotify, youtube, apple_music, cover) VALUES (?, ?, ?, ?, ?)",
            (self.title, self.spotify, self.youtube, self.apple_music, self.cover),
        )
        conn.commit()
        conn.close()
        self.load_songs()
        self.title = ""
        self.spotify = ""
        self.youtube = ""
        self.apple_music = ""
        self.cover = ""

    @rx.event
    def start_edit(self, song_id: int):
        self.editing_id = song_id
        for song in self.songs:
            if song["id"] == song_id:
                self.title = song["title"]
                self.spotify = song["spotify"]
                self.youtube = song["youtube"]
                self.apple_music = song["apple_music"]
                self.cover = song["cover"]
                break

    @rx.event
    def cancel_edit(self):
        self.editing_id = None
        self.title = ""
        self.spotify = ""
        self.youtube = ""
        self.apple_music = ""
        self.cover = ""

    @rx.event
    def save_edit(self):
        if self.editing_id is None:
            return
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE songs SET title=?, spotify=?, youtube=?, apple_music=?, cover=? WHERE id=?",
            (self.title, self.spotify, self.youtube, self.apple_music, self.cover, self.editing_id),
        )
        conn.commit()
        conn.close()
        self.cancel_edit()
        self.load_songs()

    @rx.event
    def delete_song(self, song_id: int):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM songs WHERE id=?", (song_id,))
        conn.commit()
        conn.close()
        self.load_songs()