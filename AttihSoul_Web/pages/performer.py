import reflex as rx
from .navbar import navbar
from ..components.footer import footer
from ..state.review_state import ReviewState
from ..state.gallery_state import GalleryState
from ..state.settings_state import SettingsState
from .helpers import (
    bp,
    GOLD,
    TEXT_WHITE,
    TEXT_GRAY,
    DARK_BG,
    CARD_BG,
    video_bg,
    overlay,
    social_icons,
    brand_logo,
    gold_button,
    youtube_thumbnail,
)

# =====================================================
# COMPONENTS
# =====================================================

def review_card(review):
    return rx.box(
        rx.vstack(
            rx.text(review["review"], color=TEXT_WHITE, line_height="1.8"),
            rx.text(f"— {review['name']}", color=TEXT_GRAY),
            spacing="3", align_items="start",
        ),
        bg=CARD_BG, padding="2rem", border_radius="14px", width="100%", border="1px solid rgba(212,175,55,.12)"
    )

def performance_card(item):
    """Reusable card for a single performance video."""
    return rx.box(
        rx.cond(
            item["media_type"] == "video",
            rx.box(
                youtube_thumbnail(item["src"]),
                rx.box(
                    rx.vstack(
                        rx.text(item["title"], color=TEXT_WHITE, font_weight="600"),
                        rx.link(
                            rx.hstack(rx.icon("play", size=16), rx.text("Watch Performance"), spacing="2", color=GOLD),
                            href=f"https://youtu.be/{item['src']}", is_external=True
                        ),
                        spacing="2", align_items="start"
                    ),
                    padding="1rem",
                ),
                background=CARD_BG,
                border_radius="18px",
                overflow="hidden",
                _hover={
                    "transform": "translateY(-8px)",
                    "boxShadow": "0 20px 50px rgba(212,168,90,.18)",
                },
                transition="all .3s ease",
            ),
        ),
    )

def performance_gallery_section(heading_text: str, items_getter, padding):
    """Render a section heading + grid of performance cards."""
    return rx.box(
        rx.container(
            rx.vstack(
                rx.heading(heading_text, color=TEXT_WHITE, size="5", width="100%", text_align="center"),
                rx.cond(
                    items_getter.length() > 0,
                    rx.grid(
                        rx.foreach(
                            items_getter,
                            lambda item: performance_card(item),
                        ),
                        columns=bp(initial="1", sm="2", md="3"), spacing="6", width="100%", justify_items="center",
                    ),
                    rx.text("No videos yet.", color=TEXT_GRAY, text_align="center"),
                ),
                spacing="5", align_items="center", width="100%",
            ),
            max_width="1200px",
        ),
        padding=padding, background="#0d0d0d",
    )

def stat_box(number, title):
    return rx.box(
        rx.vstack(
            rx.heading(number, color=GOLD, font_size=bp(initial="2.7rem", md="3.5rem")),
            rx.text(title, color=TEXT_WHITE),
            spacing="2", align_items="center",
        ),
        background=CARD_BG,
        border=f"1px solid rgba(212,175,55,.15)",
        border_radius="16px",
        padding="2rem",
        width="100%",
        box_shadow="0 8px 25px rgba(0,0,0,.25)",
        _hover={
            "transform": "translateY(-6px)",
            "border": f"1px solid {GOLD}",
            "boxShadow": "0 20px 45px rgba(212,168,90,.18)",
        },
        transition="all .3s ease",
    )

def booking_card(icon, title, description):
    return rx.box(
        rx.vstack(
            rx.icon(icon, size=32, color=GOLD),
            rx.heading(title, color=GOLD, size="4"),
            rx.text(description, color=TEXT_GRAY, text_align="center"),
            spacing="2", align_items="center",
        ),
        background=CARD_BG,
        border_radius="16px",
        padding="2rem",
        width="100%",
        min_height="230px",
        border="1px solid rgba(212,175,55,.15)",
        _hover={
            "transform": "translateY(-5px)",
            "border": f"1px solid {GOLD}",
        },
        transition="all .3s ease",
    )

def feature_card(icon, title):
    return rx.box(
        rx.vstack(
            rx.icon(icon, size=40, color=GOLD),
            rx.text(title, color=TEXT_WHITE, font_weight="600"),
            spacing="3", align_items="center",
        ),
        bg=CARD_BG, padding="2rem", border_radius="16px", border=f"1px solid rgba(212,175,55,.15)",
        _hover={
            "transform": "translateY(-6px)",
            "border": f"1px solid {GOLD}",
        },
        transition="all .3s ease",
    )

# =====================================================
# MAIN PAGE
# =====================================================

def performer_page():
    section_padding = bp(initial="4rem 1.5rem", sm="5rem 2rem", md="6rem 3rem", lg="7rem 3rem")

    return rx.box(
        navbar(),
        # HERO SECTION
        rx.box(
            video_bg("/hero video.mp4"),
            overlay("rgba(0,0,0,.55)"),
            rx.flex(
                rx.vstack(
                    rx.text("LIVE PERFORMER", color=GOLD),
                    rx.heading(
                        "Unforgettable Live Performances", 
                        color=TEXT_WHITE, 
                        font_size=bp(initial="1.8rem", sm="2.7rem", md="4rem", lg="5rem"), 
                        line_height="1.1",
                        text_align="center"
                    ),
                    rx.text("Soul • Jazz • Funk • Acoustic", color=GOLD, font_size=bp(initial="0.9rem", md="1rem"), letter_spacing="4px"),
                    rx.text("From intimate weddings to international stages, every performance is crafted to leave a lasting memory.", color=TEXT_GRAY, width="100%", max_width="720px", padding_x=bp(initial="1rem", md="0"), text_align="center"),
                    
                    # Single Hero CTA
                    rx.link(
                        rx.button(
                            "Book Now",
                            size="3",
                            variant="solid",
                            background=GOLD,
                            color="black",
                            border_radius="9999px",
                            padding_x="2.5rem",
                            padding_y="1.5rem",
                            width=bp(
                                initial="220px",
                                sm="240px",
                                md="260px",
                            ),
                            _hover={
                                "background": "#e3bb73",
                                "transform": "translateY(-2px)",
                            },
                            transition="all .3s ease",
                        ),
                        href="#book",
                    ),
                    
                    spacing=bp(initial="3", md="6"),
                    align_items="center",
                    width="100%",
                    max_width="700px",
                    padding_x="1rem",
                ),
                width="100%",
                height="100%",
                justify_content="center",
                align_items="center",
                position="relative",
                z_index="5",
                padding_top=bp(initial="3rem", md="0"),
            ),
            position="relative", height="95vh",
        ),
        rx.box(social_icons(SettingsState.settings), display=bp(initial="none", md="flex"), width="100%", justify="center"),
        rx.box(brand_logo(), padding_top="3rem", padding_bottom="5rem"),
        
        # STATS
        rx.box(
            rx.container(
                rx.grid(
                    stat_box("600+", "Live Performances"),
                    stat_box("120+", "Private Events"),
                    stat_box("19", "Countries"),
                    columns=bp(initial="1", sm="3"),
                    spacing="6",
                ),
                max_width="1200px",
            ),
            padding=section_padding, background=DARK_BG,
        ),
        
        # PERFORMANCE GALLERY — Solo Acoustic
        rx.box(
            rx.container(
                rx.vstack(
                    rx.text("LIVE PERFORMANCE", color=GOLD, letter_spacing="2px"),
                    rx.heading("Live Performance Highlights", color=TEXT_WHITE, size="7"),
                    rx.text("Watch clips from past performances and experience the energy live.", color=TEXT_GRAY, max_width="650px", text_align="center", margin_bottom="2rem"),
                    spacing="5", align_items="center", width="100%",
                ),
                max_width="1200px",
            ),
            id="gallery", padding=section_padding, background="#0d0d0d",
        ),
        performance_gallery_section("Solo Acoustic", GalleryState.solo_acoustic_videos, section_padding),
        performance_gallery_section("Duo", GalleryState.duo_videos, section_padding),
        performance_gallery_section("Trio", GalleryState.trio_videos, section_padding),
        performance_gallery_section("Band Quartet", GalleryState.band_quartet_videos, section_padding),
        performance_gallery_section("Adapted String Band", GalleryState.adapted_string_band_videos, section_padding),
        
        
        # WHY CHOOSE
        rx.box(
            rx.container(
                rx.vstack(
                    rx.heading("Why Clients Choose AttihSoul", color=TEXT_WHITE, size="7", text_align="center"),
                    rx.grid(
                        feature_card("briefcase", "Professional Live Band"),
                        feature_card("globe", "Worldwide Performance Experience"),
                        feature_card("music", "Customized Musical Experience"),
                        feature_card("clock", "Always On Time"),
                        columns=bp(initial="1", sm="2", md="4"),
                        spacing="6",
                        width="100%",
                    ),
                    spacing="6",
                ),
                max_width="1200px",
            ),
            padding=section_padding, background=DARK_BG,
        ),
        
        # BOOKING
        rx.box(
            rx.container(
                rx.vstack(
                    rx.heading("Available for Your Next Event", color=TEXT_WHITE, font_size="2.5rem"),
                    rx.text("Available for weddings, concerts, corporate events and private celebrations worldwide.", color=TEXT_GRAY, max_width="620px", text_align="center"),
                    rx.grid(
                        booking_card("music", "Weddings", "Elegant live music for unforgettable ceremonies."),
                        booking_card("briefcase", "Corporate Events", "Professional performances for premium events."),
                        booking_card("calendar", "Private Celebrations", "Birthdays, anniversaries and intimate gatherings."),
                        booking_card("mic", "Concerts", "Live concerts and festival performances."),
                        columns=bp(initial="1", sm="2", lg="4"),
                        spacing="6",
                        width="100%",
                    ),
                    rx.box(gold_button("Request a Booking", "/contact"), padding_top="2rem"),
                    spacing="5", align_items="center",
                ),
                max_width="1200px",
            ),
            id="book", padding=section_padding, background="#0d0d0d",
        ),
        
        # EXPERIENCE SECTION
        rx.box(
            rx.container(
                rx.grid(
                    rx.box(rx.heading("Weddings", color=GOLD, size="5"), rx.text("Elegant acoustic performances tailored to your ceremony.", color=TEXT_GRAY), padding="2rem", bg=CARD_BG, border_radius="16px"),
                    rx.box(rx.heading("Corporate Events", color=GOLD, size="5"), rx.text("Professional entertainment that enhances your brand.", color=TEXT_GRAY), padding="2rem", bg=CARD_BG, border_radius="16px"),
                    rx.box(rx.heading("International Festivals", color=GOLD, size="5"), rx.text("Experienced touring performer with global stage presence.", color=TEXT_GRAY), padding="2rem", bg=CARD_BG, border_radius="16px"),
                    columns=bp(initial="1", md="3"), spacing="6"
                ),
                max_width="1200px",
            ),
            padding=section_padding, background=DARK_BG
        ),
        
        # REVIEWS FORM
        rx.box(
            rx.container(
                rx.vstack(
                    rx.heading("Share Your Experience", color=TEXT_WHITE, font_size="2rem"),
                    rx.text(".", color=TEXT_GRAY, max_width="650px", text_align="center"),
                    rx.input(placeholder="Your Name", value=ReviewState.name, on_change=ReviewState.set_name, width="100%", bg="#181818", border="1px solid rgba(212,175,55,.15)", color=TEXT_WHITE),
                    rx.text_area(placeholder="Tell everyone about your experience...", value=ReviewState.review, on_change=ReviewState.set_review, width="100%", min_height="180px", bg="#181818", border="1px solid rgba(212,175,55,.15)", color=TEXT_WHITE),
                    rx.button("Submit Review", on_click=ReviewState.submit_review, background=GOLD, color="black", width=bp(initial="100%", sm="220px"), border_radius="9999px"),
                    spacing="4", align_items="center",
                ),
                max_width="700px",
            ),
            padding=section_padding, background="#0d0d0d",
        ),
        
        rx.box(
            rx.container(
                rx.vstack(
                    rx.text("TESTIMONIALS", color=GOLD, letter_spacing="2px"),
                    rx.heading("What Audiences Are Saying", color=TEXT_WHITE, font_size="2.5rem"),
                    rx.cond(
                        ReviewState.approved_reviews.length() > 0,
                        rx.grid(rx.foreach(ReviewState.approved_reviews, review_card), columns=bp(initial="1", md="2"), spacing="6", width="100%"),
                        rx.text("Be the first to share your experience with AttihSoul.", color=TEXT_GRAY),
                    ),
                    spacing="5", align_items="center",
                ),
                max_width="1200px",
            ),
            padding=section_padding, background="#0d0d0d",
        ),
        footer(),
        background=DARK_BG,
        on_mount=[ReviewState.load_reviews, GalleryState.on_load, SettingsState.load_settings],
    )
