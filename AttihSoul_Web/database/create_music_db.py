import sqlite3

conn = sqlite3.connect("music.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS songs (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    title TEXT,

    spotify TEXT,

    youtube TEXT,

    apple_music TEXT,

    cover TEXT

)
""")

conn.commit()

conn.close()

print("Music database created successfully.")