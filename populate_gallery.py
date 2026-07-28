import sqlite3
import re

DB_PATH = "gallery.db"

def extract_youtube_id(url_or_id: str) -> str:
    if re.match(r'^[a-zA-Z0-9_-]{11}$', url_or_id.strip()):
        return url_or_id.strip()
    patterns = [
        r'(?:youtube\.com/watch\?.*v=)([a-zA-Z0-9_-]{11})',
        r'(?:youtu\.be/)([a-zA-Z0-9_-]{11})',
        r'(?:youtube\.com/embed/)([a-zA-Z0-9_-]{11})',
        r'(?:youtube\.com/shorts/)([a-zA-Z0-9_-]{11})',
    ]
    for pattern in patterns:
        match = re.search(pattern, url_or_id)
        if match:
            return match.group(1)
    return url_or_id.strip()

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Delete only the sample/placeholder videos
cur.execute("DELETE FROM gallery_items WHERE title IN (?,?,?,?)", (
    "All In My Head (Official Visualizer)",
    "Dreams (Choir Version)",
    "Good Old Days",
    "Live Performance Highlights",
))
print("Deleted sample rows:", cur.rowcount)

# Videos to insert
# Using IDs as primary key sequence starting from where real data begins
videos = [
    # Artist Latest Visuals
    ("say you love me", "video", "https://youtu.be/n70SRpi1yqQ", "latest_visuals"),
    # Add remaining artist videos
    ("Latest Visual 2", "video", "https://youtu.be/_FMdyEiD0d4", "latest_visuals"),
    ("Latest Visual 3", "video", "https://youtu.be/g0bGUmKtH6M", "latest_visuals"),
    ("Latest Visual 4", "video", "https://youtu.be/Us7tmJA6nCA", "latest_visuals"),
    ("Latest Visual 5", "video", "https://youtu.be/Rbhmcxowxqk", "latest_visuals"),
    ("Latest Visual 6", "video", "https://youtu.be/gktCjHgb8qA", "latest_visuals"),
    ("Latest Visual 7", "video", "https://youtu.be/3S-OZ9_6kgE", "latest_visuals"),
    # Performer Solo Acoustic
    ("Solo Acoustic 1", "video", "https://youtu.be/LVjWiR6wQBY", "solo_acoustic"),
    ("Solo Acoustic 2", "video", "https://youtu.be/vs2h3rUioLA", "solo_acoustic"),
    ("Solo Acoustic 3", "video", "https://youtu.be/M-eVHHelKnA", "solo_acoustic"),
    ("Solo Acoustic 4", "video", "https://youtu.be/YcJ62FDE9xE", "solo_acoustic"),
    # Performer Duo
    ("Duo 1", "video", "https://youtu.be/fGS_y0w1kKg", "duo"),
    ("Duo 2", "video", "https://youtu.be/0E3v0eyepQs", "duo"),
    ("Duo 3", "video", "https://youtu.be/Rweeseb053E", "duo"),
    # Performer Trio
    ("Trio 1", "video", "https://youtu.be/DGygpfx15U4", "trio"),
    ("Trio 2", "video", "https://youtu.be/Ndnwl7zmNgk", "trio"),
    ("Trio 3", "video", "https://youtu.be/A46g5r43BEs", "trio"),
    ("Trio 4", "video", "https://youtu.be/8sae2Gie1ok", "trio"),
    # Performer Band Quartet
    ("Band Quartet 1", "video", "https://youtu.be/TCYKha5YPhw", "band_quartet"),
    ("Band Quartet 2", "video", "https://youtu.be/r6cOjytq28M", "band_quartet"),
    ("Band Quartet 3", "video", "https://youtu.be/Yq1nhNdrtig", "band_quartet"),
    ("Band Quartet 4", "video", "https://youtu.be/wutbeR5NllM", "band_quartet"),
    ("Band Quartet 5", "video", "https://youtu.be/BTGCpztYu-0", "band_quartet"),
    ("Band Quartet 6", "video", "https://youtu.be/indPYTdCrwU", "band_quartet"),
    ("Band Quartet 7", "video", "https://youtu.be/UF5eVp_YHNA", "band_quartet"),
    ("Band Quartet 8", "video", "https://youtu.be/LDIt022YMtE", "band_quartet"),
    # Performer Adapted String Band (duplicate URL appears once in DB)
    ("Adapted String Band 1", "video", "https://youtu.be/sjXqnlwdAtI", "adapted_string_band"),
    ("Adapted String Band 2", "video", "https://youtu.be/uEceLymEHU0", "adapted_string_band"),
    ("Adapted String Band 3", "video", "https://youtu.be/K_aORwN6h9E", "adapted_string_band"),
    ("Adapted String Band 4", "video", "https://youtu.be/q3LV0uB2d-U", "adapted_string_band"),
]

inserted = 0
for title, media_type, url, category in videos:
    video_id = extract_youtube_id(url)
    cur.execute(
        "INSERT INTO gallery_items(title, media_type, src, category) VALUES(?, ?, ?, ?)",
        (title, media_type, video_id, category),
    )
    inserted += 1

conn.commit()
conn.close()
print(f"Inserted {inserted} videos")