import sqlite3

def create_database():
    conn = sqlite3.connect("lost_found.db")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            category TEXT NOT NULL,
            location TEXT NOT NULL,
            date TEXT NOT NULL,
            description TEXT,
            contact TEXT NOT NULL,
            item_type TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

create_database()

