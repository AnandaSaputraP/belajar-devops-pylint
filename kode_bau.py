"""Modul contoh yang sudah diperbaiki mengikuti PEP 8."""


def hitung_penjumlahan(nilai_a, nilai_b, daftar, tambahan):
    """Menjumlahkan beberapa nilai.

    Args:
        nilai_a: Bilangan pertama.
        nilai_b: Bilangan kedua.
        daftar: List bilangan, elemen pertama dipakai.
        tambahan: Bilangan tambahan.

    Returns:
        Hasil penjumlahan semua nilai.
    """
    return nilai_a + nilai_b + daftar[0] + tambahan


def main():
    """Fungsi utama program."""
    print(hitung_penjumlahan(1, 2, [3], 4))


if __name__ == "__main__":
    main()
