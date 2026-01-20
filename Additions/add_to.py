import sqlite3


#EDIT THIS PART
DB_NAME = "Library_items.db"

LIBRARIES = [
    {
        "name": "REPLACE WITH LIBRARY NAME",
        "description": "WHAT THIS LIBRARY DOES": [
            "TAGS",
            "YOU CAN ADD AS MANY AS YOU WANT"
        ],
        "items": [
            ("FUNCTION", "DESCRIPTION OF FUNCTION", "EXAMPLE USAGE"),
            ("YOU CAN ADD MORE", "MORE TAGS", "JUST LIKE THIS ONE IS SEPERATED")
        ]
    },
]


#LEAVE THIS PART
conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()
cur.execute("PRAGMA foreign_keys = ON;")

for lib in LIBRARIES:
    cur.execute(
        "INSERT OR IGNORE INTO library (name, description) VALUES (?, ?)",
        (lib["name"], lib["description"])
    )

    cur.execute("SELECT id FROM library WHERE name = ?", (lib["name"],))
    library_id = cur.fetchone()[0]

    for tag in lib["tags"]:
        normalized_tag = " ".join(tag.lower().split())
        cur.execute("INSERT OR IGNORE INTO tags (tag) VALUES (?)", (normalized_tag,))
        cur.execute("SELECT id FROM tags WHERE tag = ?", (normalized_tag,))
        tag_id = cur.fetchone()[0]

        cur.execute(
            "INSERT OR IGNORE INTO library_tags (library_id, tag_id) VALUES (?, ?)",
            (library_id, tag_id)
        )

    cur.executemany(
        "INSERT OR IGNORE INTO items (library_id, name, description, example) VALUES (?, ?, ?, ?)",
        [(library_id, n, d, e) for n, d, e in lib["items"]]
    )

conn.commit()
conn.close()
