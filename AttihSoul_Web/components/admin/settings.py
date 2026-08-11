import reflex as rx
from ...state.settings_state import SettingsState

GOLD = "#D4AF37"


def setting_field(label: str, value, on_change, placeholder: str = "", is_textarea: bool = False):
    return rx.box(
        rx.text(label, color="#BBBBBB", font_size="0.85rem", margin_bottom="0.3rem"),
        rx.cond(
            is_textarea,
            rx.text_area(
                placeholder=placeholder,
                value=value,
                on_change=on_change,
                width="100%",
                min_height="80px",
            ),
            rx.input(
                placeholder=placeholder,
                value=value,
                on_change=on_change,
                width="100%",
            ),
        ),
        width="100%",
        margin_bottom="1rem",
    )


def settings_page():
    return rx.vstack(
        rx.heading("Site Settings", color=GOLD, size="5"),
        rx.text("Manage social links, contact info, and SEO settings.", color="#AAAAAA"),
        rx.divider(),
        # Social Links
        rx.box(
            rx.heading("Social Media Links", color=GOLD, size="4"),
            setting_field("Instagram URL", SettingsState.instagram, SettingsState.set_instagram, "https://instagram.com/..."),
            setting_field("YouTube URL", SettingsState.youtube, SettingsState.set_youtube, "https://youtube.com/..."),
            setting_field("Spotify URL", SettingsState.spotify, SettingsState.set_spotify, "https://open.spotify.com/..."),
            setting_field("TikTok URL", SettingsState.tiktok, SettingsState.set_tiktok, "https://tiktok.com/..."),
            setting_field("Wikipedia URL", SettingsState.wikipedia, SettingsState.set_wikipedia, "https://en.wikipedia.org/..."),
            setting_field("X (Twitter) URL", SettingsState.x, SettingsState.set_x, "https://x.com/..."),
            spacing="2",
            width="100%",
            padding="20px",
            background="#111111",
            border="1px solid #333333",
            border_radius="8px",
        ),
        # Contact Info
        rx.box(
            rx.heading("Contact Information", color=GOLD, size="4"),
            setting_field("Contact Email", SettingsState.contact_email, SettingsState.set_contact_email, "info@example.com"),
            setting_field("Contact Phone", SettingsState.contact_phone, SettingsState.set_contact_phone, "+1234567890"),
            spacing="2",
            width="100%",
            padding="20px",
            background="#111111",
            border="1px solid #333333",
            border_radius="8px",
        ),
        # Hero Text
        rx.box(
            rx.heading("Hero Text", color=GOLD, size="4"),
            setting_field("Hero Title", SettingsState.hero_title, SettingsState.set_hero_title, "Attih Soul"),
            setting_field("Hero Subtitle", SettingsState.hero_subtitle, SettingsState.set_hero_subtitle, "Soul • R&B • Afro • Acoustic"),
            spacing="2",
            width="100%",
            padding="20px",
            background="#111111",
            border="1px solid #333333",
            border_radius="8px",
        ),
        # About Page
        rx.box(
            rx.heading("About Page", color=GOLD, size="4"),
            setting_field(
                "About Intro Text",
                SettingsState.about_intro,
                SettingsState.set_about_intro,
                "Barcelona based Soul and R&B Artist available for bookings for Concerts, Festivals, Weddings, Galas and Parties worldwide",
                is_textarea=True,
            ),
            spacing="2",
            width="100%",
            padding="20px",
            background="#111111",
            border="1px solid #333333",
            border_radius="8px",
        ),
        # Performer Page
        rx.box(
            rx.heading("Performer Page", color=GOLD, size="4"),
            setting_field(
                "Hero Heading",
                SettingsState.performer_heading,
                SettingsState.set_performer_heading,
                "Unforgettable Live Performances",
            ),
            setting_field(
                "Hero Subtitle",
                SettingsState.performer_subtitle,
                SettingsState.set_performer_subtitle,
                "Soul • Jazz • Funk • Acoustic",
            ),
            setting_field(
                "Hero Description",
                SettingsState.performer_description,
                SettingsState.set_performer_description,
                "From intimate weddings to international stages, every performance is crafted to leave a lasting memory.",
                is_textarea=True,
            ),
            spacing="2",
            width="100%",
            padding="20px",
            background="#111111",
            border="1px solid #333333",
            border_radius="8px",
        ),
        # Services Page
        rx.box(
            rx.heading("Services Page", color=GOLD, size="4"),
            setting_field(
                "Hero Title",
                SettingsState.services_hero_title,
                SettingsState.set_services_hero_title,
                "Music for Concerts, Festivals and Events",
            ),
            setting_field(
                "Hero Intro",
                SettingsState.services_hero_intro,
                SettingsState.set_services_hero_intro,
                "Attih Soul is a brand synonymous with musical excellence, and its essence is captured in the services rendered.",
                is_textarea=True,
            ),
            spacing="2",
            width="100%",
            padding="20px",
            background="#111111",
            border="1px solid #333333",
            border_radius="8px",
        ),
        # SEO
        rx.box(
            rx.heading("SEO Settings", color=GOLD, size="4"),
            setting_field(
                "Meta Description",
                SettingsState.seo_description,
                SettingsState.set_seo_description,
                "Site description for search engines...",
                is_textarea=True,
            ),
            setting_field(
                "Meta Keywords",
                SettingsState.seo_keywords,
                SettingsState.set_seo_keywords,
                "keyword1, keyword2, keyword3",
                is_textarea=True,
            ),
            spacing="2",
            width="100%",
            padding="20px",
            background="#111111",
            border="1px solid #333333",
            border_radius="8px",
        ),
        rx.button(
            "Save All Settings",
            on_click=SettingsState.save_settings,
            background=GOLD,
            color="black",
            width={"base": "100%", "sm": "220px"},
        ),
        rx.cond(
            SettingsState.saved,
            rx.text("Settings saved successfully!", color="#4CAF50", font_weight="600"),
        ),
        spacing="5",
        width="100%",
        align="stretch",
    )
