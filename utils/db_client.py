import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "test_data.db"


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def fetch_all_users() -> list[dict]:
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT id, name, username, email, phone FROM users ORDER BY id"
        ).fetchall()
    return [dict(row) for row in rows]


def fetch_users_with_companies() -> list[dict]:
    query = """
        SELECT u.id, u.name, u.email, c.name AS company_name, c.catch_phrase
        FROM users u
        JOIN companies c ON c.user_id = u.id
        ORDER BY u.id
    """
    with get_connection() as conn:
        rows = conn.execute(query).fetchall()
    return [dict(row) for row in rows]


def fetch_user_by_id(user_id: int) -> dict | None:
    query = """
        SELECT u.id, u.name, u.username, u.email, u.phone, c.name AS company_name
        FROM users u
        JOIN companies c ON c.user_id = u.id
        WHERE u.id = ?
    """
    with get_connection() as conn:
        row = conn.execute(query, (user_id,)).fetchone()
    return dict(row) if row else None
