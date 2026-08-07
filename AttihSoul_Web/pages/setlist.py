import reflex as rx
from .navbar import navbar
from ..components.footer import footer

# ============ THEME (self-contained) ============
GOLD = "#d4a85a"
TEXT_WHITE = "#ffffff"
TEXT_GRAY = "#a1a1a1"
DARK_BG = "#0a0a0a"
CARD_BG = "#111111"

def bp(initial=None, sm=None, md=None, lg=None, xl=None):
    return rx.breakpoints(initial=initial, sm=sm, md=md, lg=lg, xl=xl)

# ============ HELPERS (self-contained) ============
def video_bg(src: str) -> rx.Component:
    return rx.el.video(
        rx.el.source(src=src, type="video/mp4"),
        auto_play=True, loop=True, muted=True, plays_inline=True,
        style={
            "position": "absolute", "top": "0", "left": "0",
            "width": "100%", "height": "100%", "objectFit": "cover", "zIndex": "0",
        },
    )

def overlay(color: str) -> rx.Component:
    return rx.box(
        position="absolute", top="0", left="0", width="100%", height="100%",
        background=color, z_index="1",
    )

def gold_button(text: str, href: str = "#") -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.text(text, color="white", font_weight="600", font_size=bp(initial="12px", md="16px")),
            rx.box("→", color="white", background=GOLD, border_radius="50%",
                   width=bp(initial="20px", md="32px"), height=bp(initial="20px", md="32px"),
                   display="flex", align_items="center", justify_content="center",
                   font_size=bp(initial="10px", md="14px")),
            spacing="3", align="center",
            padding=bp(initial="4px 8px", md="0.75rem 1rem"),
        ),
        href=href,
        display="inline-block",
        border=f"1px solid {GOLD}",
        border_radius="9999px",
        background="rgba(0,0,0,0.25)",
        text_decoration="none",
        _hover={"background": "rgba(212,168,90,0.15)"},
    )

# ============ SONG DATA (from uploaded catalogue) ============

# ---- Solo Acoustic ----
solo_acoustic_soul_rnb = [
    "Ain’t No Sunshine – Bill Withers",
    "All My Life – KCi & JoJo",
    "Apologise – One Republic",
    "Back To Black – Amy Winehouse",
    "Climax – Usher",
    "Colors – Black Pumas",
    "Crazy – Gnarls Barkley",
    "Down On My Knees - Ayo",
    "Fallin – Alicia Keys",
    "Feeling Good – Nina Simone",
    "Hallelujah – Leonard Cohen",
    "Halo – Beyoncé",
    "I’d Rather Go Blind – Etta James",
    "Just The Way You Are – Bruno Mars",
    "Latch – Sam Smith",
    "Let It Be – Beatles",
    "Let It Go – James Bay",
    "Let Me Love You – Mario",
    "Mercy – Duffy",
    "Rise Up – Andra Day",
    "So Sick – Ne-Yo",
    "Stand By Me – Ben E King",
    "Stay With Me – Sam Smith",
    "Still The One – Shania Twain",
    "Tennessee Whiskey – Chris Stapleton",
    "This City – Sam Fischer",
    "Valerie – Amy Winehouse",
    "Wake Me Up – Avicii",
    "What About Love – Lemar",
    "Why I Love You – Major",
]

solo_acoustic_pop_rock_folk = [
    "A Thousand Years – Christina Perri",
    "All In My Head – Tori Kelly",
    "Beneath Your Beautiful – Labrinth",
    "Break Even – The Script",
    "Can You Feel The Love Tonight – Elton John",
    "Chandelier – Sia",
    "Chasing Cars – Snow Patrol",
    "Clown – Emeli Sandé",
    "Elastic Heart – Sia",
    "Everything I Wanted – Billie Eilish",
    "Fix You – Coldplay",
    "Flying Without Wings – Westlife",
    "Free Fallin – Tom Petty",
    "Get Lucky – Daft Punk",
    "Goodbye My Lover – James Blunt",
    "Hello – Adele",
    "Hero – Enrique Iglesias",
    "Lost Without You – Freya Ridings",
    "Love the Way You Lie – Rihanna",
    "Make It Rain – Ed Sheeran",
    "Make You Feel My Love – Adele",
    "Payphone – Maroon 5",
    "Perfect – Ed Sheeran",
    "Roses – James Arthur",
    "Say You Won’t Let Go – James Arthur",
    "Skinny Love – Birdy",
    "Someone Like You – Adele",
    "Someone You Loved – Lewis Capaldi",
    "Talking to the Moon – Bruno Mars",
    "Teenage Dream – Katy Perry",
    "The Blower’s Daughter – Damien Rice",
    "The Man Who Can’t Be Moved – The Script",
    "Thinking Out Loud – Ed Sheeran",
    "Yellow – Coldplay",
    "You Are The Reason – Calum Scott",
]

solo_acoustic_reggae_afro = [
    "African Queen – 2Face",
    "Angel – Shaggy",
    "Beautiful Girls – Sean Kingston",
    "Jailer – Asa",
    "Magic – Coldplay",
    "Me Love – Sean Kingston",
    "No Woman No Cry – Bob Marley",
    "Redemption Song – Bob Marley",
]

# ---- Full Band ----
full_band_soul_rnb = [
    "Ain’t No Sunshine – Bill Withers",
    "All In My Head – Attih Soul",
    "Back to Black – Amy Winehouse",
    "Beat It – Michael Jackson",
    "Bring It on Home to Me – Sam Cooke",
    "Closer – Ne-Yo",
    "Colours – Black Pumas",
    "Crazy – Gnarls Barkley",
    "DJ’s Got Us Falling in Love – Usher",
    "Don’t Stop till You Get Enough – Michael Jackson",
    "End of the Road – Boyz II Men",
    "Feeling Good – Nina Simone",
    "First Time – Teeks",
    "Forget You – CeeLo Green",
    "Get Lucky – Daft Punk",
    "Grenade – Bruno Mars",
    "I Feel Good – James Brown",
    "I’d Rather Go Blind – Etta James",
    "I’ll Make Love To You – Boyz II Men",
    "Just The Way You Are – Bruno Mars",
    "Killing Me Softly – Lauryn Hill",
    "Latch – Sam Smith",
    "Locked Out of Heaven – Bruno Mars",
    "Mercy – Duffy",
    "My Girl – Temptations",
    "My Love Is Your Love – Whitney Houston",
    "Not the Only One – Sam Smith",
    "Our Love – Samm Henshaw",
    "So Sick – Ne-Yo",
    "Stand By Me – Ben E King",
    "Stay With Me – Sam Smith",
    "Superstitious – Stevie Wonder",
    "Titanium - Sia",
    "Unaware – Allen Stone",
    "Uptown Funk – Bruno Mars",
    "Valerie – Amy Winehouse",
    "Wake Me Up – Avicii",
    "Without You - Usher",
    "When a Man Loves a Woman – Michael Bolton",
]

full_band_pop_rock_folk = [
    "Fix You – Coldplay",
    "Free Fallin – Tom Petty",
    "Make It Rain – Ed Sheeran",
    "One and Only – Adele",
    "Thinking Out Loud – Ed Sheeran",
]

full_band_reggae_afro = [
    "African Queen – Tuface Idibia",
    "Gbona – Burna Boy",
    "Happy – Pharrell",
    "In The Music – Attih Soul",
    "Iyawo Mi – Timi Dakolo",
    "La La La – Naughty Boy",
    "Man Down - Rihanna",
    "Me Love – Sean Kingston",
    "Redemption Song – Bob Marley",
    "Rude – Magic",
]

full_band_originals = [
    "All In My Head – Attih Soul",
    "Friendzone – Attih Soul",
    "In The Music – Attih Soul",
    "Karma – Attih Soul",
    "Someday I’ll Find You – Attih Soul",
]

# ============ COMPONENTS ============

def song_item(title: str) -> rx.Component:
    return rx.text(title, color=TEXT_GRAY, font_size="0.95rem", line_height="1.8")

def song_grid(songs: list) -> rx.Component:
    return rx.grid(
        *[song_item(s) for s in songs],
        columns=bp(initial="1", sm="2", lg="3"),
        spacing="4",
        width="100%",
    )

def category_heading(text: str) -> rx.Component:
    return rx.vstack(
        rx.heading(text, color=GOLD, size="4", font_weight="600"),
        rx.divider(border_color="#222"),
        spacing="2",
        width="100%",
    )

# ============ SETLIST PAGE ============
def setlist_page() -> rx.Component:
    return rx.box(
        navbar(),

        # HERO
        rx.box(
            video_bg("/hero video.mp4"),
            overlay("rgba(0,0,0,0.55)"),
            rx.center(
                rx.vstack(
                    rx.text(
                        "SETLIST",
                        color=GOLD,
                        font_size="0.9rem",
                        letter_spacing="4px",
                        font_weight="500",
                    ),
                    rx.heading(
                        "SETLIST / REPERTOIRE",
                        font_size=bp(initial="2.4rem", md="4rem", lg="4.6rem"),
                        font_weight="700",
                        color=TEXT_WHITE,
                        text_align="center",
                        line_height="1.05",
                    ),
                    rx.text(
                        "Discover Attih Soul’s live repertoire,\nfrom intimate acoustic performances\nto full band performances.",
                        color=TEXT_WHITE,
                        font_size=bp(initial="1rem", md="1.15rem"),
                        text_align="center",
                        max_width="620px",
                        white_space="pre-line",
                    ),
                    spacing="4",
                    align="center",
                    padding_x="1rem",
                ),
                width="100%",
                height="100%",
                position="relative",
                z_index="10",
            ),
            position="relative",
            width="100%",
            height=bp(initial="90vh", md="100vh"),
            min_height="500px",
            overflow="hidden",
        ),

        # SOLO ACOUSTIC
        rx.box(
            rx.container(
                rx.vstack(
                    rx.text("REPERTOIRE", color=GOLD, font_size="0.85rem", letter_spacing="3px"),
                    rx.heading("Solo Acoustic", color=TEXT_WHITE, font_size="2.5rem", font_weight="700"),
                    rx.text(
                        "Intimate Acoustic Performances Spanning from Soul, Rnb, Pop, Folk, Reggae and Afro.",
                        color=TEXT_GRAY,
                        font_size="1.05rem",
                        max_width="680px",
                    ),
                    rx.box(height="1.5rem"),
                    # Soul / R&B
                    category_heading("Soul / R&B"),
                    song_grid(solo_acoustic_soul_rnb),
                    rx.box(height="2rem"),
                    # Pop / Rock / Folk
                    category_heading("Pop / Rock / Folk"),
                    song_grid(solo_acoustic_pop_rock_folk),
                    rx.box(height="2rem"),
                    # Reggae / Afro
                    category_heading("Reggae / Afro"),
                    song_grid(solo_acoustic_reggae_afro),
                    spacing="4",
                    align_items="start",
                    width="100%",
                ),
                max_width="1200px",
            ),
            padding=bp(initial="3rem 1.5rem", md="4rem 3rem"),
            background=DARK_BG,
        ),

        # FULL BAND
        rx.box(
            rx.container(
                rx.vstack(
                    rx.text("REPERTOIRE", color=GOLD, font_size="0.85rem", letter_spacing="3px"),
                    rx.heading("Full Band", color=TEXT_WHITE, font_size="2.5rem", font_weight="700"),
                    rx.text(
                        "Full band performances bringing energy, depth and a rich live sound.",
                        color=TEXT_GRAY,
                        font_size="1.05rem",
                        max_width="680px",
                    ),
                    rx.box(height="1.5rem"),
                    # Soul / R&B
                    category_heading("Soul / R&B"),
                    song_grid(full_band_soul_rnb),
                    rx.box(height="2rem"),
                    # Pop / Rock / Folk
                    category_heading("Pop / Rock / Folk"),
                    song_grid(full_band_pop_rock_folk),
                    rx.box(height="2rem"),
                    # Reggae / Afro
                    category_heading("Reggae / Afro"),
                    song_grid(full_band_reggae_afro),
                    rx.box(height="2rem"),
                    # Originals
                    category_heading("Originals"),
                    song_grid(full_band_originals),
                    spacing="4",
                    align_items="start",
                    width="100%",
                ),
                max_width="1200px",
            ),
            padding=bp(initial="3rem 1.5rem", md="4rem 3rem"),
            background="#0f0f0f",
        ),

        # BOTTOM CTA
        rx.box(
            rx.container(
                rx.vstack(
                    rx.heading("Looking for a specific song?", color=TEXT_WHITE, font_size="2.3rem", font_weight="600"),
                    rx.text(
                        "Special requests can be arranged for weddings,\nprivate events, restaurants, hotels, corporate functions\nand private celebrations.",
                        color=TEXT_GRAY,
                        font_size="1.05rem",
                        text_align="center",
                        white_space="pre-line",
                    ),
                    rx.box(height="1.25rem"),
                    gold_button("Book Attih Soul", "/contact"),
                    spacing="3",
                    align="center",
                ),
                max_width="800px",
            ),
            padding=bp(initial="3rem 1.5rem", md="5rem 3rem"),
            background=DARK_BG,
            text_align="center",
        ),

        # FOOTER
        footer(),
    )