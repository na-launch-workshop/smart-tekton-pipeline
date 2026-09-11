import sqlite3
import pytest
from app.main import greet, get_user


def test_greet_default():
    assert greet() == "Hello, World!"


def test_greet_with_name():
    assert greet("Alice") == "Hello, Alice!"


@pytest.fixture
def db(tmp_path):
    db_path = tmp_path / "app.db"
    with sqlite3.connect(db_path) as conn:
        conn.execute("CREATE TABLE users (username TEXT, email TEXT)")
        conn.execute("INSERT INTO users VALUES ('alice', 'alice@example.com')")
    return str(db_path)


def test_get_user_found(db, monkeypatch):
    monkeypatch.setattr("app.main.sqlite3.connect", lambda _: sqlite3.connect(db))
    result = get_user("alice")
    assert result is not None
    assert result[0] == "alice"


def test_get_user_not_found(db, monkeypatch):
    monkeypatch.setattr("app.main.sqlite3.connect", lambda _: sqlite3.connect(db))
    result = get_user("nobody")
    assert result is None
