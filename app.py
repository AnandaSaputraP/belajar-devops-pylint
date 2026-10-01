"""Aplikasi contoh untuk belajar scanning keamanan dengan semgrep."""
import sqlite3


def get_user(username):
    """Ambil data user dari database dengan query berparameter."""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    return cursor.fetchall()


def main():
    """Fungsi utama program."""
    nama = input("Masukkan username: ")
    print(get_user(nama))


if __name__ == "__main__":
    main()
