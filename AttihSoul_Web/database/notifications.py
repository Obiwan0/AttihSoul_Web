"""Resend-based booking notification helper.

Sends a concise booking request email to info@attihsoul.com through the
Resend HTTP API using only the Python standard library.

Required environment variables (values live in the Render dashboard, never
in source code):
    RESEND_API_KEY  - Resend API key
    RESEND_FROM     - verified sender address (e.g. bookings@attihsoul.com)

If either variable is missing, sending is a no-op so existing deployments
keep working exactly as before.
"""

import json
import os
import urllib.request

RESEND_API_URL = "https://api.resend.com/emails"

RECIPIENT = "info@attihsoul.com"
SUBJECT = "New Booking Request — Attih Soul"


def send_booking_notification(booking: dict) -> None:
    """POST a booking notification to Resend.

    Never raises: every failure (missing config, DNS, timeout, non-2xx API
    response, unexpected exception) is swallowed so the caller's booking
    flow is never affected.
    """
    api_key = os.getenv("RESEND_API_KEY", "").strip()
    sender = os.getenv("RESEND_FROM", "").strip()
    if not api_key or not sender:
        return

    payload = {
        "from": sender,
        "to": [RECIPIENT],
        "subject": SUBJECT,
        "text": (
            f"Name: {booking.get('name', '')}\n"
            f"Email: {booking.get('email', '')}\n"
            f"Phone: {booking.get('phone', '')}\n"
            f"Event Type: {booking.get('event_type', '')}\n"
            f"Event Date: {booking.get('event_date', '')}\n"
            f"Location: {booking.get('location', '')}\n"
            f"Message: {booking.get('message', '')}\n"
        ),
    }

    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        RESEND_API_URL,
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            response.read()
    except Exception:
        # A notification failure must never break or roll back a booking.
        pass