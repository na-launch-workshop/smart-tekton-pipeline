import sqlite3


def greet(name="World"):
    return f"Hello, {name}!"


def get_user(username):
    with sqlite3.connect("app.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        return cursor.fetchone()


def main():
    print(greet())

    user_input = input("Enter username: ")
    try:
        user = get_user(user_input)
        print(f"Found: {user}")
    except sqlite3.Error as e:
        print(f"Database error: {e}")


if __name__ == "__main__":
    main()
