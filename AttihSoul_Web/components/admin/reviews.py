import reflex as rx
from ...state.review_state import ReviewState

GOLD = "#D4AF37"


def review_card(review: dict):
    status_colors = {
        "pending": "#FF9800",
        "approved": "#4CAF50",
        "rejected": "#f44336",
    }
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.text(review["name"], font_weight="bold", color=GOLD, font_size="1.1rem"),
                rx.spacer(),
                rx.badge(
                    review["status"],
                    color_scheme=rx.match(
                        review["status"],
                        ("pending", "orange"),
                        ("approved", "green"),
                        ("rejected", "red"),
                        "gray",
                    ),
                ),
                width="100%",
            ),
            rx.text(review["review"], color="white"),
            rx.hstack(
                rx.cond(
                    review["status"] != "approved",
                    rx.button(
                        "Approve",
                        on_click=lambda: ReviewState.approve_review(review["id"]),
                        background="#4CAF50",
                        color="white",
                        size="2",
                        _hover={"background": "#388E3C"},
                    ),
                ),
                rx.cond(
                    review["status"] != "rejected",
                    rx.button(
                        "Reject",
                        on_click=lambda: ReviewState.reject_review(review["id"]),
                        color_scheme="red",
                        size="2",
                    ),
                ),
                rx.button(
                    "Delete",
                    on_click=lambda: ReviewState.delete_review(review["id"]),
                    color_scheme="red",
                    size="2",
                    variant="outline",
                ),
                spacing="3",
                wrap="wrap",
            ),
            spacing="4",
            align="start",
        ),
        width="100%",
        background="#1A1A1A",
        border="1px solid #222222",
        border_radius="12px",
        padding="20px",
    )


def reviews_manager():
    return rx.vstack(
        rx.heading("Review Manager", color=GOLD, size="5"),
        rx.text("Approve, reject, or delete customer reviews.", color="#AAAAAA"),
        rx.divider(),
        # Search
        rx.input(
            placeholder="Search reviews...",
            value=ReviewState.search_query,
            on_change=ReviewState.set_search_query,
            width="100%",
        ),
        # Tabs
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger("Pending", value="pending"),
                rx.tabs.trigger("Approved", value="approved"),
                rx.tabs.trigger("Rejected", value="rejected"),
                rx.tabs.trigger("All", value="all"),
            ),
            rx.tabs.content(
                rx.cond(
                    ReviewState.pending_reviews.length() > 0,
                    rx.vstack(
                        rx.foreach(ReviewState.pending_reviews, review_card),
                        spacing="4",
                        width="100%",
                    ),
                    rx.text("No pending reviews.", color="#AAAAAA"),
                ),
                value="pending",
            ),
            rx.tabs.content(
                rx.cond(
                    ReviewState.approved_reviews.length() > 0,
                    rx.vstack(
                        rx.foreach(ReviewState.approved_reviews, review_card),
                        spacing="4",
                        width="100%",
                    ),
                    rx.text("No approved reviews.", color="#AAAAAA"),
                ),
                value="approved",
            ),
            rx.tabs.content(
                rx.cond(
                    ReviewState.rejected_reviews.length() > 0,
                    rx.vstack(
                        rx.foreach(ReviewState.rejected_reviews, review_card),
                        spacing="4",
                        width="100%",
                    ),
                    rx.text("No rejected reviews.", color="#AAAAAA"),
                ),
                value="rejected",
            ),
            rx.tabs.content(
                rx.cond(
                    ReviewState.filtered_reviews.length() > 0,
                    rx.vstack(
                        rx.foreach(ReviewState.filtered_reviews, review_card),
                        spacing="4",
                        width="100%",
                    ),
                    rx.text("No reviews found.", color="#AAAAAA"),
                ),
                value="all",
            ),
            default_value="pending",
            width="100%",
        ),
        spacing="5",
        width="100%",
        align="stretch",
    )
