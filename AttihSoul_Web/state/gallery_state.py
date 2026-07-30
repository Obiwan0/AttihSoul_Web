import sqlite3
import re
import reflex as rx

DB_NAME = "gallery.db"


def extract_youtube_id(url_or_id: str) -> str:
    """Extract a YouTube video ID from a URL or return the input if it's already an ID."""
    # If it's already an 11-char alphanumeric ID, return as-is
    if re.match(r'^[a-zA-Z0-9_-]{11}$', url_or_id.strip()):
        return url_or_id.strip()
    # Try to extract from various YouTube URL formats
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
    # Return as-is if no pattern matches (might be a custom ID or image URL)
    return url_or_id.strip()


# Default gallery items seeded on first run
DEFAULT_GALLERY_ITEMS = [
    # Artist Videos (latest_visuals)
    {"title": "All In My Head (Official Visualizer)", "media_type": "video", "src": extract_youtube_id("https://youtu.be/n70SRpi1yqQ"), "category": "latest_visuals"},
    {"title": "Dreams (Choir Version)", "media_type": "video", "src": extract_youtube_id("https://youtu.be/_FMdyEiD0d4"), "category": "latest_visuals"},
    {"title": "Good Old Days", "media_type": "video", "src": extract_youtube_id("https://youtu.be/g0bGUmKtH6M"), "category": "latest_visuals"},
    {"title": "Healed Too Much", "media_type": "video", "src": extract_youtube_id("https://youtu.be/Us7tmJA6nCA"), "category": "latest_visuals"},
    {"title": "Kiss Ya (Live at Estudio Tanger)", "media_type": "video", "src": extract_youtube_id("https://youtu.be/Rbhmcxowxqk"), "category": "latest_visuals"},
    {"title": "Shades of Emotions", "media_type": "video", "src": extract_youtube_id("https://youtu.be/gktCjHgb8qA"), "category": "latest_visuals"},
    {"title": "The Acoustic Experiment", "media_type": "video", "src": extract_youtube_id("https://youtu.be/3S-OZ9_6kgE"), "category": "latest_visuals"},
    # Solo Acoustic (solo_acoustic)
    {"title": "Solo Acoustic Performance 1", "media_type": "video", "src": extract_youtube_id("https://youtu.be/LVjWiR6wQBY"), "category": "solo_acoustic"},
    {"title": "Solo Acoustic Performance 2", "media_type": "video", "src": extract_youtube_id("https://youtu.be/vs2h3rUioLA"), "category": "solo_acoustic"},
    {"title": "Solo Acoustic Performance 3", "media_type": "video", "src": extract_youtube_id("https://youtu.be/M-eVHHelKnA"), "category": "solo_acoustic"},
    {"title": "Solo Acoustic Performance 4", "media_type": "video", "src": extract_youtube_id("https://youtu.be/YcJ62FDE9xE"), "category": "solo_acoustic"},
    # Duo (duo)
    {"title": "Duo Performance 1", "media_type": "video", "src": extract_youtube_id("https://youtu.be/fGS_y0w1kKg"), "category": "duo"},
    {"title": "Duo Performance 2", "media_type": "video", "src": extract_youtube_id("https://youtu.be/0E3v0eyepQs"), "category": "duo"},
    {"title": "Duo Performance 3", "media_type": "video", "src": extract_youtube_id("https://youtu.be/Rweeseb053E"), "category": "duo"},
    # Trio (trio)
    {"title": "Trio Performance 1", "media_type": "video", "src": extract_youtube_id("https://youtu.be/DGygpfx15U4"), "category": "trio"},
    {"title": "Trio Performance 2", "media_type": "video", "src": extract_youtube_id("https://youtu.be/Ndnwl7zmNgk"), "category": "trio"},
    {"title": "Trio Performance 3", "media_type": "video", "src": extract_youtube_id("https://youtu.be/A46g5r43BEs"), "category": "trio"},
    {"title": "Trio Performance 4", "media_type": "video", "src": extract_youtube_id("https://youtu.be/8sae2Gie1ok"), "category": "trio"},
    # Band Quartet (band_quartet)
    {"title": "Band Quartet Performance 1", "media_type": "video", "src": extract_youtube_id("https://youtu.be/TCYKha5YPhw"), "category": "band_quartet"},
    {"title": "Band Quartet Performance 2", "media_type": "video", "src": extract_youtube_id("https://youtu.be/r6cOjytq28M"), "category": "band_quartet"},
    {"title": "Band Quartet Performance 3", "media_type": "video", "src": extract_youtube_id("https://youtu.be/Yq1nhNdrtig"), "category": "band_quartet"},
    {"title": "Band Quartet Performance 4", "media_type": "video", "src": extract_youtube_id("https://youtu.be/wutbeR5NllM"), "category": "band_quartet"},
    {"title": "Band Quartet Performance 5", "media_type": "video", "src": extract_youtube_id("https://youtu.be/BTGCpztYu-0"), "category": "band_quartet"},
    {"title": "Band Quartet Performance 6", "media_type": "video", "src": extract_youtube_id("https://youtu.be/indPYTdCrw"), "category": "band_quartet"},
    {"title": "Band Quartet Performance 7", "media_type": "video", "src": extract_youtube_id("https://youtu.be/UF5eVp_YHNA"), "category": "band_quartet"},
    {"title": "Band Quartet Performance 8", "media_type": "video", "src": extract_youtube_id("https://youtu.be/LDIt022YMtE"), "category": "band_quartet"},
    # Adapted String Band (adapted_string_band)
    {"title": "Adapted String Band Performance 1", "media_type": "video", "src": extract_youtube_id("https://youtu.be/sjXqnlwdAtI"), "category": "adapted_string_band"},
    {"title": "Adapted String Band Performance 2", "media_type": "video", "src": extract_youtube_id("https://youtu.be/uEceLymEHU0"), "category": "adapted_string_band"},
    {"title": "Adapted String Band Performance 3", "media_type": "video", "src": extract_youtube_id("https://youtu.be/K_aORwN6h9E"), "category": "adapted_string_band"},
    {"title": "Adapted String Band Performance 4", "media_type": "video", "src": extract_youtube_id("https://youtu.be/q3LV0uB2d-U"), "category": "adapted_string_band"},
]


def init_db():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS gallery_items(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            media_type TEXT NOT NULL DEFAULT 'image',
            src TEXT NOT NULL,
            category TEXT DEFAULT 'general',
            created_at TEXT DEFAULT (datetime('now'))
        )
    """)
    # Seed default items only when the table is empty
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM gallery_items")
    count = cursor.fetchone()[0]
    if count == 0:
        for item in DEFAULT_GALLERY_ITEMS:
            cursor.execute(
                "INSERT INTO gallery_items(title, media_type, src, category) VALUES (?, ?, ?, ?)",
                (item["title"], item["media_type"], item["src"], item["category"]),
            )
        conn.commit()
    conn.close()


init_db()


class GalleryState(rx.State):
    """Manages images and videos in the gallery."""

    title: str = ""
    media_type: str = "image"
    src: str = ""
    category: str = "general"
    editing_id: int | None = None

    items: list[dict] = []
    is_mounted: bool = False

    @rx.var
    def artist_videos(self) -> list[dict]:
        """Return only items with category 'latest_visuals'."""
        return [item for item in self.items if item.get("category") == "latest_visuals"]

    @rx.var
    def solo_acoustic_videos(self) -> list[dict]:
        """Return only video items with category 'solo_acoustic'."""
        return [item for item in self.items if item.get("media_type") == "video" and item.get("category") == "solo_acoustic"]

    @rx.var
    def duo_videos(self) -> list[dict]:
        """Return only video items with category 'duo'."""
        return [item for item in self.items if item.get("media_type") == "video" and item.get("category") == "duo"]

    @rx.var
    def trio_videos(self) -> list[dict]:
        """Return only video items with category 'trio'."""
        return [item for item in self.items if item.get("media_type") == "video" and item.get("category") == "trio"]

    @rx.var
    def band_quartet_videos(self) -> list[dict]:
        """Return only video items with category 'band_quartet'."""
        return [item for item in self.items if item.get("media_type") == "video" and item.get("category") == "band_quartet"]

    @rx.var
    def adapted_string_band_videos(self) -> list[dict]:
        """Return only video items with category 'adapted_string_band'."""
        return [item for item in self.items if item.get("media_type") == "video" and item.get("category") == "adapted_string_band"]

    @rx.event
    def on_load(self):
        self.is_mounted = True
        self.load_items()

    @rx.event
    def load_items(self):
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM gallery_items ORDER BY id DESC")
        rows = [dict(r) for r in cur.fetchall()]
        conn.close()
        self.items = rows

    @rx.event
    def set_title(self, value: str):
        self.title = value

    @rx.event
    def set_media_type(self, value: str):
        self.media_type = value

    @rx.event
    def set_src(self, value: str):
        self.src = value

    @rx.event
    def set_category(self, value: str):
        self.category = value

    @rx.event
    def add_item(self):
        if not self.title.strip() or not self.src.strip():
            return
        # Auto-extract YouTube ID if a URL was provided
        clean_src = extract_youtube_id(self.src.strip())
        conn = sqlite3.connect(DB_NAME)
        conn.execute(
            "INSERT INTO gallery_items(title, media_type, src, category) VALUES(?, ?, ?, ?)",
            (self.title.strip(), self.media_type, clean_src, self.category.strip()),
        )
        conn.commit()
        conn.close()
        self.title = ""
        self.media_type = "image"
        self.src = ""
        self.category = "general"
        self.load_items()

    @rx.event
    def start_edit(self, item_id: int):
        self.editing_id = item_id
        for item in self.items:
            if item["id"] == item_id:
                self.title = item["title"]
                self.media_type = item["media_type"]
                self.src = item["src"]
                self.category = item["category"]
                break

    @rx.event
    def cancel_edit(self):
        self.editing_id = None
        self.title = ""
        self.media_type = "image"
        self.src = ""
        self.category = "general"

    @rx.event
    def save_edit(self):
        if self.editing_id is None:
            return
        conn = sqlite3.connect(DB_NAME)
        conn.execute(
            "UPDATE gallery_items SET title=?, media_type=?, src=?, category=? WHERE id=?",
            (self.title.strip(), self.media_type, self.src.strip(), self.category.strip(), self.editing_id),
        )
        conn.commit()
        conn.close()
        self.cancel_edit()
        self.load_items()

    @rx.event
    def delete_item(self, item_id: int):
        conn = sqlite3.connect(DB_NAME)
        conn.execute("DELETE FROM gallery_items WHERE id=?", (item_id,))
        conn.commit()
        conn.close()
        self.load_items()