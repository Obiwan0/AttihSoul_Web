-- ================================================================================
-- Combined SQLite Schema for AttihSoul_Web
-- Extracted from databases in AttihSoul_Web/database/
-- Source databases: blog.db, bookings.db, gallery.db, music.db, reviews.db, settings.db
-- ================================================================================

-- --------------------------------------------------------------------------------
-- DATABASE: blog.db
-- --------------------------------------------------------------------------------

CREATE TABLE blog_posts(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, content TEXT NOT NULL, category TEXT DEFAULT 'general', status TEXT DEFAULT 'draft', featured_image TEXT DEFAULT '', created_at TEXT DEFAULT (datetime('now')));

-- --------------------------------------------------------------------------------
-- DATABASE: bookings.db
-- --------------------------------------------------------------------------------

CREATE TABLE bookings(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT,
            event_type TEXT,
            event_date TEXT,
            location TEXT,
            message TEXT,
            status TEXT DEFAULT 'pending',
            created_at TEXT DEFAULT (datetime('now'))
        );

-- --------------------------------------------------------------------------------
-- DATABASE: gallery.db
-- --------------------------------------------------------------------------------

CREATE TABLE gallery_items(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            media_type TEXT NOT NULL DEFAULT 'image',
            src TEXT NOT NULL,
            category TEXT DEFAULT 'general',
            created_at TEXT DEFAULT (datetime('now'))
        );

-- --------------------------------------------------------------------------------
-- DATABASE: music.db
-- --------------------------------------------------------------------------------

CREATE TABLE songs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            spotify TEXT,
            youtube TEXT,
            apple_music TEXT,
            cover TEXT
        );

-- --------------------------------------------------------------------------------
-- DATABASE: reviews.db
-- --------------------------------------------------------------------------------

CREATE TABLE reviews(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        review TEXT,
        status TEXT DEFAULT 'pending'
    );

-- --------------------------------------------------------------------------------
-- DATABASE: settings.db
-- --------------------------------------------------------------------------------

CREATE TABLE settings(
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        );