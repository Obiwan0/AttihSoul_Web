import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DB_NAME = BASE_DIR / "database" / "music.db"

DEFAULT_SONGS = [
    {
        "title": "All In My Head",
        "spotify": "https://distrokid.com/hyperfollow/attihsoul/all-in-my-head-2",
        "youtube": "",
        "apple_music": "",
        "cover": "/album cover/Ph-29.jpg",
    },
    {
        "title": "Dreams",
        "spotify": "https://open.spotify.com/track/4Xgw3qk0ctc2Yl2r2gnPYD?si=7ded252791804879",
        "youtube": "",
        "apple_music": "",
        "cover": "",
    },
    {
        "title": "Good Old Days (Choir Version)",
        "spotify": "https://distrokid.com/hyperfollow/attihsoul/good-old-days-choir-version",
        "youtube": "",
        "apple_music": "",
        "cover": "/album cover/card 2.jpg",
    },
    {
        "title": "Healed Too Much (Choir Version)",
        "spotify": "https://distrokid.com/hyperfollow/attihsoul/healed-too-much-choir-version",
        "youtube": "",
        "apple_music": "",
        "cover": "/album cover/card 3.jpg",
    },
    {
        "title": "Kiss Ya (Live at Estudio Tanger)",
        "spotify": "https://distrokid.com/hyperfollow/attihsoul/kiss-ya-live-at-estudio-tanger-barcelona",
        "youtube": "",
        "apple_music": "",
        "cover": "/album cover/card 6.jpg",
    },
    {
        "title": "Someday i will find you ",
        "spotify": "https://open.spotify.com/album/0o3SVABgv4LEhsLXXCI11r?si=MYMnkv31TrCgF1WVNQ_GIg",
        "youtube": "",
        "apple_music": "",
        "cover": "",
    },
]


def init_music_db():
    conn = sqlite3.connect(DB_NAME)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS songs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            spotify TEXT,
            youtube TEXT,
            apple_music TEXT,
            cover TEXT
        )
    """)

    # Seed default songs only when the table is empty
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM songs")
    count = cursor.fetchone()[0]
    if count == 0:
        for song in DEFAULT_SONGS:
            cursor.execute(
                "INSERT INTO songs(title, spotify, youtube, apple_music, cover) VALUES (?, ?, ?, ?, ?)",
                (song["title"], song["spotify"], song["youtube"], song["apple_music"], song["cover"]),
            )
        conn.commit()

    conn.close()


init_music_db()
