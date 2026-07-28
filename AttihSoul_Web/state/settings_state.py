import sqlite3
import reflex as rx

DB_NAME = "settings.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS settings(
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        )
    """)
    conn.commit()
    # Insert defaults
    defaults = {
        "instagram": "https://www.instagram.com/attih_soul/",
        "youtube": "https://www.youtube.com/channel/UC26rJ72ZSCYK8MfMt3FsFWg",
        "spotify": "https://open.spotify.com/artist/5kL7MUEVmuucYk2LsJlrLC",
        "tiktok": "https://www.tiktok.com/@attihsoul",
        "wikipedia": "https://en.wikipedia.org/wiki/Attih_Soul",
        "x": "https://x.com/attihsoul",
        "contact_email": "info@attihsoul.com",
        "contact_phone": "",
        "hero_title": "Attih Soul",
        "hero_subtitle": "Soul • R&B • Afro • Acoustic",
        "seo_description": "Attih Soul is an international soul and R&B artist based in Barcelona, available for concerts, festivals, weddings, and private events worldwide.",
        "seo_keywords": "Attih Soul, soul artist, R&B, Barcelona, live performer, wedding singer, corporate events",
    }
    for k, v in defaults.items():
        conn.execute(
            "INSERT OR IGNORE INTO settings(key, value) VALUES(?, ?)", (k, v)
        )
    conn.commit()
    conn.close()


init_db()


class SettingsState(rx.State):
    """Manages site-wide settings like social links, SEO, and contact info."""

    settings: dict[str, str] = {}

    # Editable fields
    instagram: str = ""
    youtube: str = ""
    spotify: str = ""
    tiktok: str = ""
    wikipedia: str = ""
    x: str = ""
    contact_email: str = ""
    contact_phone: str = ""
    hero_title: str = ""
    hero_subtitle: str = ""
    seo_description: str = ""
    seo_keywords: str = ""

    saved: bool = False

    @rx.event
    def load_settings(self):
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT key, value FROM settings")
        rows = cur.fetchall()
        conn.close()
        self.settings = {r["key"]: r["value"] for r in rows}
        self.instagram = self.settings.get("instagram", "")
        self.youtube = self.settings.get("youtube", "")
        self.spotify = self.settings.get("spotify", "")
        self.tiktok = self.settings.get("tiktok", "")
        self.wikipedia = self.settings.get("wikipedia", "")
        self.x = self.settings.get("x", "")
        self.contact_email = self.settings.get("contact_email", "")
        self.contact_phone = self.settings.get("contact_phone", "")
        self.hero_title = self.settings.get("hero_title", "")
        self.hero_subtitle = self.settings.get("hero_subtitle", "")
        self.seo_description = self.settings.get("seo_description", "")
        self.seo_keywords = self.settings.get("seo_keywords", "")

    def _save_setting(self, key: str, value: str):
        conn = sqlite3.connect(DB_NAME)
        conn.execute(
            "INSERT OR REPLACE INTO settings(key, value) VALUES(?, ?)", (key, value)
        )
        conn.commit()
        conn.close()

    @rx.event
    def set_instagram(self, value: str):
        self.instagram = value

    @rx.event
    def set_youtube(self, value: str):
        self.youtube = value

    @rx.event
    def set_spotify(self, value: str):
        self.spotify = value

    @rx.event
    def set_tiktok(self, value: str):
        self.tiktok = value

    @rx.event
    def set_wikipedia(self, value: str):
        self.wikipedia = value

    @rx.event
    def set_x(self, value: str):
        self.x = value

    @rx.event
    def set_contact_email(self, value: str):
        self.contact_email = value

    @rx.event
    def set_contact_phone(self, value: str):
        self.contact_phone = value

    @rx.event
    def set_hero_title(self, value: str):
        self.hero_title = value

    @rx.event
    def set_hero_subtitle(self, value: str):
        self.hero_subtitle = value

    @rx.event
    def set_seo_description(self, value: str):
        self.seo_description = value

    @rx.event
    def set_seo_keywords(self, value: str):
        self.seo_keywords = value

    @rx.event
    def save_settings(self):
        self._save_setting("instagram", self.instagram)
        self._save_setting("youtube", self.youtube)
        self._save_setting("spotify", self.spotify)
        self._save_setting("tiktok", self.tiktok)
        self._save_setting("wikipedia", self.wikipedia)
        self._save_setting("x", self.x)
        self._save_setting("contact_email", self.contact_email)
        self._save_setting("contact_phone", self.contact_phone)
        self._save_setting("hero_title", self.hero_title)
        self._save_setting("hero_subtitle", self.hero_subtitle)
        self._save_setting("seo_description", self.seo_description)
        self._save_setting("seo_keywords", self.seo_keywords)
        self.saved = True
        self.load_settings()