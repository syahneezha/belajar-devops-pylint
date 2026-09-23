"""Modul demonstrasi kode yang sudah diperbaiki mengikuti PEP 8."""


def proses_data(nilai_a, nilai_b, nilai_c, daftar_e, angka_tambahan):
    """Memproses beberapa nilai dan mengembalikan hasil perhitungan.

    Args:
        nilai_a: Flag boolean pertama.
        nilai_b: Flag boolean kedua.
        nilai_c: Nilai opsional, bisa None.
        daftar_e: List berisi minimal satu elemen numerik.
        angka_tambahan: List berisi dua angka tambahan untuk perhitungan.

    Returns:
        Hasil penjumlahan jika kondisi terpenuhi, selain itu None.
    """
    if not nilai_a or nilai_b or nilai_c is not None:
        return None

    hasil = daftar_e[0] + angka_tambahan[0] + angka_tambahan[1]
    print(f"Hasil perhitungan: {hasil}")
    return hasil


def main():
    """Fungsi utama untuk menjalankan proses_data dengan contoh nilai."""
    proses_data(True, False, None, [2], [1, 3])


if __name__ == "__main__":
    main()
    