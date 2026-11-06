import sqlite3

db = sqlite3.connect("training.db")

db.execute("DROP TABLE IF EXISTS users")

db.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL
)
""")

users = [
    ("jsmith", "Training123!", "employee"),
    ("mjohnson", "Welcome2026!", "employee"),
    ("admin", "Falcon2026!", "admin"),
    ("security", "BlueTeam2026!", "analyst")
]

db.executemany(
    "INSERT INTO users (username,password,role) VALUES (?,?,?)",
    users
)

db.commit()
db.close()

print("Training database initialized.")
