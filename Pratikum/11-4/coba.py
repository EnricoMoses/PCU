# --- Doni's Magic Plant (rekursi + try/except, tanpa loop) ---

def minta_hari():
    """
    Meminta input hari dari pengguna secara rekursif.
    Valid: integer >= 1.
    """
    try:
        n = int(input("Masukkan hari: ").strip())
        if n < 1:
            print("Error: Hari minimal harus 1!")
            return minta_hari()
        return n
    except Exception:
        print("Error: Input harus berupa angka! Silakan coba lagi.")
        return minta_hari()


def langkah_berikutnya(state):
    """
    Transformasi satu hari ke depan.
    state = (tunas, prajurit, jendral, raja)
    Aturan:
      - tunas -> prajurit
      - prajurit -> jendral
      - jendral -> raja
      - raja tetap raja dan menghasilkan 1 tunas per raja
    """
    t, p, j, r = state
    # hari berikutnya:
    t2 = r          # semua raja melahirkan tunas baru
    p2 = t          # tunas menjadi prajurit
    j2 = p          # prajurit menjadi jendral
    r2 = r + j      # raja bertahan + jendral naik jadi raja
    return (t2, p2, j2, r2)


def format_barisan(state):
    """Menyusun teks seperti '1 raja 1 prajurit 1 tunas' (skip yang 0)"""
    t, p, j, r = state
    bagian = []
    if r: bagian.append(f"{r} raja")
    if j: bagian.append(f"{j} jendral")
    if p: bagian.append(f"{p} prajurit")
    if t: bagian.append(f"{t} tunas")
    return " ".join(bagian) if bagian else "0"


def cetak_perkembangan(target_hari, hari_ke=1, state=(1, 0, 0, 0)):
    """
    Mencetak Hari 1..X secara rekursif.
    state awal: Hari-1 = 1 tunas.
    """
    print(f"Hari ke-{hari_ke}: {format_barisan(state)}")
    if hari_ke == target_hari:
        return
    cetak_perkembangan(target_hari, hari_ke + 1, langkah_berikutnya(state))


X = minta_hari()
cetak_perkembangan(X)