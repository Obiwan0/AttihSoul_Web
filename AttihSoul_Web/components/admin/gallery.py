import reflex as rx
from ...state.gallery_state import GalleryState, extract_youtube_id

GOLD = "#D4AF37"


def gallery_item_card(item: dict):
    is_editing = GalleryState.editing_id == item["id"]
    return rx.box(
        rx.cond(
            is_editing,
            # Edit mode
            rx.vstack(
                rx.heading(f"Editing: {item['title']}", color=GOLD, size="5"),
                rx.input(placeholder="Title", value=GalleryState.title, on_change=GalleryState.set_title, width="100%"),
                rx.hstack(
                    rx.select(["image", "video"], value=GalleryState.media_type, on_change=GalleryState.set_media_type, width="100%"),
                    rx.input(placeholder="Category", value=GalleryState.category, on_change=GalleryState.set_category, width="100%"),
                    spacing="3",
                    width="100%",
                ),
                rx.input(placeholder="YouTube Video ID or Image URL", value=GalleryState.src, on_change=GalleryState.set_src, width="100%"),
                rx.hstack(
                    rx.button("Save", on_click=GalleryState.save_edit, background=GOLD, color="black"),
                    rx.button("Cancel", on_click=GalleryState.cancel_edit, color_scheme="gray", color="white"),
                    spacing="3",
                ),
                spacing="3",
                width="100%",
                padding="15px",
                background="#1A1A1A",
                border_radius="8px",
            ),
            # View mode
            rx.box(
                rx.hstack(
                    rx.cond(
                        item["media_type"] == "image",
                        rx.image(src=item["src"], width="80px", height="80px", object_fit="cover", border_radius="6px"),
                        rx.box(
                            rx.image(
                                src=f"https://img.youtube.com/vi/{item['src']}/hqdefault.jpg",
                                width="80px",
                                height="80px",
                                object_fit="cover",
                                border_radius="6px",
                            ),
                        ),
                    ),
                    rx.vstack(
                        rx.text(item["title"], color="white", font_weight="600"),
                        rx.text(f"{item['media_type']} • {item.get('category', 'general')}", color="#AAAAAA", font_size="0.85rem"),
                        align="start",
                        spacing="1",
                    ),
                    rx.spacer(),
                    rx.button("Edit", on_click=lambda: GalleryState.start_edit(item["id"]), background=GOLD, color="black", size="2"),
                    rx.button("Delete", on_click=lambda: GalleryState.delete_item(item["id"]), color_scheme="red", size="2", variant="outline"),
                    spacing="3",
                    width="100%",
                ),
                width="100%",
                padding="10px",
                background="#1A1A1A",
                border="1px solid #333333",
                border_radius="8px",
            ),
        ),
        width="100%",
    )


def gallery_manager():
    return rx.vstack(
        rx.heading("Gallery Manager", color=GOLD, size="5"),
        rx.text("Manage images and videos displayed on the website.", color="#AAAAAA"),
        rx.text("For YouTube videos: paste the video URL or just the video ID. URLs are automatically converted.", color="#888888", font_size="0.85rem"),
        rx.divider(),
        # Add new item
        rx.box(
            rx.heading("Add New Item", color=GOLD, size="4"),
            rx.input(
                placeholder="Title",
                value=GalleryState.title,
                on_change=GalleryState.set_title,
                width="100%",
            ),
            rx.hstack(
                rx.select(
                    ["image", "video"],
                    value=GalleryState.media_type,
                    on_change=GalleryState.set_media_type,
                    width="100%",
                ),
                rx.input(
                    placeholder="Category (e.g. concerts, weddings, studio)",
                    value=GalleryState.category,
                    on_change=GalleryState.set_category,
                    width="100%",
                ),
                spacing="3",
                width="100%",
            ),
            rx.input(
                placeholder="YouTube URL, Video ID, or Image URL",
                value=GalleryState.src,
                on_change=GalleryState.set_src,
                width="100%",
            ),
            rx.button(
                "Add to Gallery",
                on_click=GalleryState.add_item,
                background=GOLD,
                color="black",
                width={"base": "100%", "sm": "220px"},
            ),
            spacing="4",
            width="100%",
            padding="20px",
            background="#111111",
            border="1px solid #333333",
            border_radius="8px",
        ),
        rx.divider(),
        rx.heading("Gallery Items", color=GOLD, size="4"),
        rx.foreach(GalleryState.items, gallery_item_card),
        spacing="5",
        width="100%",
        align="stretch",
    )
