import sqlite3
import requests
from pathlib import Path

DB_PATH = Path(__file__).parent / "test_data.db"
API_URL = "https://jsonplaceholder.typicode.com/users"


def _create_tables(conn: sqlite3.Connection) -> None:
    conn.execute("DROP TABLE IF EXISTS companies")
    conn.execute("DROP TABLE IF EXISTS users")
    conn.execute("""
        CREATE TABLE users (
            id       INTEGER PRIMARY KEY,
            name     TEXT NOT NULL,
            username TEXT,
            email    TEXT NOT NULL,
            phone    TEXT
        )
    """)
    conn.execute("""
        CREATE TABLE companies (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id      INTEGER NOT NULL,
            name         TEXT NOT NULL,
            catch_phrase TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)
    conn.commit()


def seed_database() -> int:
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()
    users = response.json()

    with sqlite3.connect(DB_PATH) as conn:
        _create_tables(conn)
        for user in users:
            conn.execute(
                "INSERT INTO users (id, name, username, email, phone) VALUES (?, ?, ?, ?, ?)",
                (user["id"], user["name"], user["username"], user["email"], user["phone"])
            )
            company = user.get("company", {})
            conn.execute(
                "INSERT INTO companies (user_id, name, catch_phrase) VALUES (?, ?, ?)",
                (user["id"], company.get("name", ""), company.get("catchPhrase", ""))
            )
        conn.commit()

    print(f"Seeded {len(users)} users into {DB_PATH}")
    return len(users)


if __name__ == "__main__":
    seed_database()
