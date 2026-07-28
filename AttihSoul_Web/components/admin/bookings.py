import reflex as rx

GOLD = "#D4AF37"


def booking_card(booking: dict):
    from ...state.booking_state import BookingState

    status_colors = {
        "pending": "#FF9800",
        "approved": "#4CAF50",
        "rejected": "#f44336",
    }
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.heading(booking["name"], color=GOLD, size="5"),
                rx.spacer(),
                rx.badge(
                    booking["status"],
                    color_scheme=rx.match(
                        booking["status"],
                        ("pending", "orange"),
                        ("approved", "green"),
                        ("rejected", "red"),
                        "gray",
                    ),
                ),
                width="100%",
            ),
            rx.grid(
                rx.box(
                    rx.text("Email", color="#777777", font_size="0.85rem"),
                    rx.text(booking["email"], color="white"),
                ),
                rx.box(
                    rx.text("Phone", color="#777777", font_size="0.85rem"),
                    rx.text(booking.get("phone", "N/A"), color="white"),
                ),
                rx.box(
                    rx.text("Event Type", color="#777777", font_size="0.85rem"),
                    rx.text(booking.get("event_type", "N/A"), color="white"),
                ),
                rx.box(
                    rx.text("Location", color="#777777", font_size="0.85rem"),
                    rx.text(booking.get("location", "N/A"), color="white"),
                ),
                columns="2",
                spacing="3",
                width="100%",
            ),
            rx.cond(
                booking["message"] != "",
                rx.box(
                    rx.text("Message", color="#777777", font_size="0.85rem"),
                    rx.text(booking["message"], color="white"),
                    width="100%",
                ),
            ),
            rx.hstack(
                rx.cond(
                    booking["status"] != "approved",
                    rx.button(
                        "Approve",
                        on_click=lambda: BookingState.approve_booking(booking["id"]),
                        background="#4CAF50",
                        color="white",
                        size="2",
                        _hover={"background": "#388E3C"},
                    ),
                ),
                rx.cond(
                    booking["status"] != "rejected",
                    rx.button(
                        "Reject",
                        on_click=lambda: BookingState.reject_booking(booking["id"]),
                        color_scheme="red",
                        size="2",
                    ),
                ),
                rx.button(
                    "Delete",
                    on_click=lambda: BookingState.delete_booking(booking["id"]),
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


def bookings_manager():
    from ...state.booking_state import BookingState

    return rx.vstack(
        rx.heading("Booking Manager", color=GOLD, size="5"),
        rx.text("View, approve, reject, or delete booking requests.", color="#AAAAAA"),
        rx.divider(),
        # Search
        rx.input(
            placeholder="Search bookings...",
            value=BookingState.search_query,
            on_change=BookingState.set_search_query,
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
                    BookingState.pending_bookings.length() > 0,
                    rx.vstack(
                        rx.foreach(BookingState.pending_bookings, booking_card),
                        spacing="4",
                        width="100%",
                    ),
                    rx.text("No pending bookings.", color="#AAAAAA"),
                ),
                value="pending",
            ),
            rx.tabs.content(
                rx.cond(
                    BookingState.approved_bookings.length() > 0,
                    rx.vstack(
                        rx.foreach(BookingState.approved_bookings, booking_card),
                        spacing="4",
                        width="100%",
                    ),
                    rx.text("No approved bookings.", color="#AAAAAA"),
                ),
                value="approved",
            ),
            rx.tabs.content(
                rx.cond(
                    BookingState.rejected_bookings.length() > 0,
                    rx.vstack(
                        rx.foreach(BookingState.rejected_bookings, booking_card),
                        spacing="4",
                        width="100%",
                    ),
                    rx.text("No rejected bookings.", color="#AAAAAA"),
                ),
                value="rejected",
            ),
            rx.tabs.content(
                rx.cond(
                    BookingState.filtered_bookings.length() > 0,
                    rx.vstack(
                        rx.foreach(BookingState.filtered_bookings, booking_card),
                        spacing="4",
                        width="100%",
                    ),
                    rx.text("No bookings found.", color="#AAAAAA"),
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