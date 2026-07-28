import sqlite3, os
for guess in [os.path.join("AttihSoul_Web","state","gallery.db"), os.path.join("AttihSoul_Web","gallery.db"), "gallery.db"]:
    if os.path.exists(guess):
        print("DB:", guess)
        conn = sqlite3.connect(guess)
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='gallery_items'")
        print("table exists:", cur.fetchone() is not None)
        cur.execute("PRAGMA table_info(gallery_items)")
        print("columns:", cur.fetchall())
        cur.execute("SELECT * FROM gallery_items")
        rows = cur.fetchall()
        print("rows:", len(rows))
        for r in rows:
            print(r)
        conn.close()
        break
else:
    print("gallery.db not found")