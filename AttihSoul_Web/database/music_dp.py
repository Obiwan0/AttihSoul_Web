import sqlite3

DB_NAME = "music.db"


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

    conn.commit()
    conn.close()


init_music_db()