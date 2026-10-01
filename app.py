import sqlite3


def get_user(username):
    """Ambil data user dari database (AMAN dari SQL injection)."""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    return cursor.fetchall()


def main():
    nama = input("Masukkan username: ")
    print(get_user(nama))


if __name__ == "__main__":
    main()