import reflex as rx

GOLD = "#D4AF37"


def blog_post_card(post: dict):
    from ...state.blog_state import BlogState

    is_editing = BlogState.editing_id == post["id"]
    return rx.box(
        rx.cond(
            is_editing,
            # Edit mode
            rx.vstack(
                rx.heading(f"Editing: {post['title']}", color=GOLD, size="5"),
                rx.input(
                    placeholder="Title",
                    value=BlogState.title,
                    on_change=BlogState.set_title,
                    width="100%",
                ),
                rx.text_area(
                    placeholder="Content",
                    value=BlogState.content,
                    on_change=BlogState.set_content,
                    width="100%",
                    min_height="150px",
                ),
                rx.hstack(
                    rx.input(
                        placeholder="Category",
                        value=BlogState.category,
                        on_change=BlogState.set_category,
                        width="100%",
                    ),
                    rx.select(
                        ["draft", "published"],
                        value=BlogState.status,
                        on_change=BlogState.set_status,
                        width="100%",
                    ),
                    spacing="3",
                    width="100%",
                ),
                rx.input(
                    placeholder="Featured Image URL",
                    value=BlogState.featured_image,
                    on_change=BlogState.set_featured_image,
                    width="100%",
                ),
                rx.hstack(
                    rx.button("Save", on_click=BlogState.save_edit, background=GOLD, color="black"),
                    rx.button("Cancel", on_click=BlogState.cancel_edit, color_scheme="gray", color="white"),
                    spacing="3",
                ),
                spacing="3",
                width="100%",
                padding="15px",
                background="#1A1A1A",
                border_radius="8px",
            ),
            # View mode
            rx.vstack(
                rx.hstack(
                    rx.heading(post["title"], color="white", size="5"),
                    rx.spacer(),
                    rx.badge(
                        post.get("status", "draft"),
                        color_scheme=rx.match(
                            post.get("status"),
                            ("published", "green"),
                            ("draft", "orange"),
                            "gray",
                        ),
                    ),
                    spacing="3",
                    width="100%",
                ),
                rx.text(post.get("category", "general"), color="#AAAAAA", font_size="0.85rem"),
                rx.text(post["content"], color="#CCCCCC"),
                rx.hstack(
                    rx.button("Edit", on_click=lambda: BlogState.start_edit(post["id"]), background=GOLD, color="black", size="2"),
                    rx.button("Delete", on_click=lambda: BlogState.delete_post(post["id"]), color_scheme="red", size="2"),
                    spacing="3",
                ),
                spacing="3",
                align="start",
                width="100%",
                padding="15px",
                background="#1A1A1A",
                border="1px solid #333333",
                border_radius="8px",
            ),
        ),
        width="100%",
    )


def blog_manager():
    from ...state.blog_state import BlogState

    return rx.vstack(
        rx.heading("Blog Manager", color=GOLD, size="5"),
        rx.text("Create, edit, and manage blog posts.", color="#AAAAAA"),
        rx.divider(),
        # Create new post
        rx.box(
            rx.heading("New Post", color=GOLD, size="4"),
            rx.input(
                placeholder="Blog Title",
                value=BlogState.title,
                on_change=BlogState.set_title,
                width="100%",
            ),
            rx.text_area(
                placeholder="Write your blog content here...",
                value=BlogState.content,
                on_change=BlogState.set_content,
                width="100%",
                min_height="220px",
            ),
            rx.hstack(
                rx.input(
                    placeholder="Category (e.g. Music, Events, News)",
                    value=BlogState.category,
                    on_change=BlogState.set_category,
                    width="100%",
                ),
                rx.select(
                    ["draft", "published"],
                    value=BlogState.status,
                    on_change=BlogState.set_status,
                    width="100%",
                ),
                spacing="3",
                width="100%",
            ),
            rx.input(
                placeholder="Featured Image URL (optional)",
                value=BlogState.featured_image,
                on_change=BlogState.set_featured_image,
                width="100%",
            ),
            rx.button(
                "Publish Post",
                on_click=BlogState.publish_post,
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
        # Existing posts
        rx.heading("All Posts", color=GOLD, size="4"),
        rx.foreach(
            BlogState.posts,
            blog_post_card,
        ),
        spacing="5",
        width="100%",
        align="stretch",
    )