import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import heapq

# ======================= DATA LOKASI RESMI =======================
nama_lokasi = {
    "1": "FTSP",
    "2": "Aula Barat",
    "3": "Teknik Sipil",
    "4": "Fisika",
    "5": "RSG",
    "6": "FSRD",
    "7": "Aula Timur",
    "8": "LFM/9009",
    "9": "Semi Murni, Desain",
    "10": "Labtek IXB - Teknik Arsitektur",
    "11": "Labtek IXC - Teknik Geodesi, Teknik Lingkungan",
    "12": "Labtek IXA - Teknik Planologi",
    "13": "Teknik Lingkungan",
    "14": "Teknik Geodesi",
    "15": "GKU Timur",
    "16": "Labtek VIII - FIMPA, Teknik Elektro, UPT Bahasa",
    "17": "Labtek V - PIKSI, Teknik Informatika",
    "18": "Labtek VI - Farmasi, MKDU",
    "19": "Labtek VII - Teknik Fisika, Teknik Kelautan",
    "20": "CC Timur",
    "21": "CC Barat",
    "22": "Plaza Widya",
    "23": "Labtek I - Teknik Mesin",
    "24": "Labtek XI - Biologi, Geofisika, Meteorologi",
    "25": "Labtek X - Teknik Kimia, Teknik Mineral",
    "26": "Oktagon",
    "27": "TVST",
    "28": "TPB",
    "29": "Kerjasama PLN - ITB",
    "30": "Labtek I - Teknik Geofisika, Lab Struktur",
    "31": "Kimia",
    "32": "FTM, Teknik Geologi, Teknik Pertambangan",
    "33": "Pusat Penelitian Energi, LAPI",
    "34": "Perpustakaan Pusat",
    "35": "GSU",
    "36": "Labtek III",
    "37": "Labtek II",
    "38": "Labtek I FTI, Teknik Industri, Matematika, Astronomi, PPPPM",
    "39": "Pariwisata",
    "40": "ATM BNI GKU Timur",
    "41": "SARAGA"
}

# ======================= GRAF =======================
graph = {
    "FTSP": ["Aula Barat"],
    "Aula Barat": ["Teknik Sipil", "RSG", "ATM BNI Aula Barat"],
    "Teknik Sipil": ["Fisika"],
    "Fisika": ["RSG"],
    "RSG": ["FSRD", "Aula Timur"],
    "FSRD": ["Aula Timur"],
    "Aula Timur": ["LFM/9009"],
    "LFM/9009": ["Semi Murni, Desain"],
    "Semi Murni, Desain": ["Labtek IXB - Teknik Arsitektur"],
    "Labtek IXB - Teknik Arsitektur": ["Labtek IXC - Teknik Geodesi, Teknik Lingkungan"],
    "Labtek IXC - Teknik Geodesi, Teknik Lingkungan": ["Labtek IXA - Teknik Planologi"],
    "Labtek IXA - Teknik Planologi": ["Teknik Lingkungan"],
    "Teknik Lingkungan": ["Teknik Geodesi"],
    "Teknik Geodesi": ["GKU Timur"],
    "GKU Timur": ["ATM BNI GKU Timur", "East Hall", "CC Timur"],
    "East Hall": ["ATM BRI", "ATM Bukopin"],
    "Labtek VIII - FIMPA, Teknik Elektro, UPT Bahasa": ["Labtek VI - Farmasi, MKDU"],
    "Labtek V - PIKSI, Teknik Informatika": ["Labtek VI - Farmasi, MKDU"],
    "Labtek VI - Farmasi, MKDU": ["Labtek VII - Teknik Fisika, Teknik Kelautan"],
    "Labtek VII - Teknik Fisika, Teknik Kelautan": ["Plaza Widya"],
    "CC Timur": ["Plaza Widya"],
    "CC Barat": ["Plaza Widya"],
    "Plaza Widya": ["GKU Timur", "Labtek V - PIKSI, Teknik Informatika"],
    "Labtek I - Teknik Mesin": ["Labtek XI - Biologi, Geofisika, Meteorologi"],
    "Labtek XI - Biologi, Geofisika, Meteorologi": ["Labtek X - Teknik Kimia, Teknik Mineral"],
    "Labtek X - Teknik Kimia, Teknik Mineral": ["Oktagon"],
    "Oktagon": ["TVST"],
    "TVST": ["TPB"],
    "TPB": ["Kerjasama PLN - ITB"],
    "Kerjasama PLN - ITB": ["Labtek I - Teknik Geofisika, Lab Struktur"],
    "Labtek I - Teknik Geofisika, Lab Struktur": ["Kimia"],
    "Kimia": ["FTM, Teknik Geologi, Teknik Pertambangan"],
    "FTM, Teknik Geologi, Teknik Pertambangan": ["Pusat Penelitian Energi, LAPI"],
    "Pusat Penelitian Energi, LAPI": ["Perpustakaan Pusat"],
    "Perpustakaan Pusat": ["GSU"],
    "GSU": ["Labtek III"],
    "Labtek III": ["Labtek II"],
    "Labtek II": ["Labtek I FTI, Teknik Industri, Matematika, Astronomi, PPPPM"],
    "Labtek I FTI, Teknik Industri, Matematika, Astronomi, PPPPM": ["Pariwisata"],
    "Pariwisata": ["SARAGA"],
    "GKU Barat": ["ATM Niaga"],
    "Gerbang Depan": ["ATM Mandiri", "ATM BCA"],
    "ATM BNI Aula Barat": [],
    "ATM BNI GKU Timur": [],
    "ATM BRI": [],
    "ATM Bukopin": [],
    "ATM Niaga": [],
    "ATM Mandiri": [],
    "ATM BCA": [],
    "SARAGA": []
}

# ======================= ATM NODES =======================
atm_nodes_by_bank = {
    "BNI": ["ATM BNI Aula Barat", "ATM BNI GKU Timur"],
    "NIAGA": ["ATM Niaga"],
    "BRI": ["ATM BRI"],
    "BUKOPIN": ["ATM Bukopin"],
    "MANDIRI": ["ATM Mandiri"],
    "BCA": ["ATM BCA"]
}
all_atm_nodes = [atm for lst in atm_nodes_by_bank.values() for atm in lst]

# ======================= UCS =======================
def ucs(graph, start, goals):
    queue = [(0, start, [])]
    visited = set()
    while queue:
        cost, node, path = heapq.heappop(queue)
        if node in visited:
            continue
        visited.add(node)
        path = path + [node]
        if node in goals:
            return path, cost
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(queue, (cost + 10, neighbor, path))
    return None, float('inf')

# ======================= GUI =======================
root = tk.Tk()
root.title("Pencarian ATM Terdekat ITB Ganesha")
root.geometry("1100x700")

frame_left = tk.Frame(root)
frame_left.pack(side=tk.LEFT, padx=10, pady=10)

frame_right = tk.Frame(root)
frame_right.pack(side=tk.TOP, anchor='n', padx=20, pady=20)

# Peta
try:
    img = Image.open("peta_itb.png")
    img = img.resize((850, 850))
    img_tk = ImageTk.PhotoImage(img)
    label_img = tk.Label(frame_left, image=img_tk)
    label_img.pack()
except FileNotFoundError:
    tk.Label(frame_left, text="[Peta tidak ditemukan: simpan sebagai 'peta_itb.png']").pack()

# Input
tk.Label(frame_right, text="Masukkan Lokasi Anda:", font=("Helvetica", 12, "bold")).pack(anchor="w")
entry_lokasi = tk.Entry(frame_right, font=("Helvetica", 12))
entry_lokasi.pack(fill='x')

tk.Label(frame_right, text="Masukkan Bank (BNI, BRI, MANDIRI, BCA, BUKOPIN, NIAGA) atau kosong:", font=("Helvetica", 12, "bold")).pack(anchor="w", pady=(10,0))
entry_bank = tk.Entry(frame_right, font=("Helvetica", 12))
entry_bank.pack(fill='x')

frame_result = tk.LabelFrame(frame_right, text="Hasil Pencarian", font=("Helvetica", 12, "bold"), padx=10, pady=10)
frame_result.pack(fill='both', expand=True, pady=20)

output = tk.Label(frame_result, text="", justify="left", font=("Helvetica", 11), anchor="w", wraplength=450)
output.pack(anchor="w")

# Petunjuk langkah
def arahkan(path):
    instruksi = []
    for i in range(1, len(path)):
        instruksi.append(f"- Dari {path[i-1]} ke {path[i]} (ikuti papan arah/lurus/belok)")
    return "\n".join(instruksi)

# Cari tombol
def cari():
    lokasi = entry_lokasi.get().strip()
    bank = entry_bank.get().strip().upper()

    if lokasi not in graph:
        messagebox.showerror("Error", f"Lokasi '{lokasi}' tidak ditemukan di graf.")
        return

    tujuan = atm_nodes_by_bank.get(bank, all_atm_nodes)
    path, cost = ucs(graph, lokasi, tujuan)

    if path:
        instruksi = arahkan(path)
        hasil = f"Jalur: {' → '.join(path)}\nJarak: {cost} meter\n\nLangkah-langkah:\n{instruksi}\n\nSemua ATM mendukung ATM Bersama."
    else:
        hasil = "Tidak ditemukan jalur ke ATM."
    output.config(text=hasil)

tk.Button(frame_right, text="Cari ATM Terdekat", font=("Helvetica", 12, "bold"), command=cari).pack(pady=10)

root.mainloop()
