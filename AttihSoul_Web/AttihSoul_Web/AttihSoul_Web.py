import reflex as rx

from .pages.homepage import homepage
from .pages.artist import artist_page
from .pages.performer import performer_page
from .pages.about import about_page
from .pages.services import services_page
from .pages.blog import blog_page   # ← NEW
from .pages.admin import admin_page
from .pages.contact import contact_page

from .state.review_state import ReviewState
from .state.blog_state import BlogState

app = rx.App(
    style={
        "body": {
            "margin": "0",
            "padding": "0",
            "background": "black",
            "fontFamily": "Arial, sans-serif",
        }
    }
)

app.add_page(homepage, route="/", title="AttihSoul")
app.add_page(artist_page, route="/artist", title="The Artist")
app.add_page(performer_page, route="/performer", title="The Performer")
app.add_page(about_page, route="/about", title="About – Attih Soul")
app.add_page(services_page, route="/services", title="Services – Attih Soul")

app.add_page(
    admin_page,
    route="/admin",
    title="Admin Dashboard",
    on_load=ReviewState.load_reviews,
)
app.add_page(
    blog_page,
    route="/blog",
    title="Blog – Attih Soul",
    on_load=BlogState.load_posts,
)
app.add_page(
    contact_page,
    route="/contact",
    title="Contact – Attih Soul",
)