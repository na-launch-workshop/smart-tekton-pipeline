import sqlite3


def greet(name="World"):
    return f"Hello, {name}!"


def get_user(username):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    return cursor.fetchone()


def main():
    message = greet()
    print(message)

    user_input = input("Enter username: ")
    user = get_user(user_input)
    print(f"Found: {user}")


if __name__ == "__main__":
    main()
