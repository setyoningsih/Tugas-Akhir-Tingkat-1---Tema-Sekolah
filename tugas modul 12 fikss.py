import tkinter as tk
from tkinter import messagebox

def tampilkan_daftar_mahasiswa():
    daftar_mahasiswa_window = tk.Toplevel(root)
    daftar_mahasiswa_window.title("Daftar Mahasiswa Perempuan Prodi S1 Informatika Tingkat 1")

    daftar_label = tk.Label(daftar_mahasiswa_window, text="Daftar Mahasiswa : ")
    daftar_label.pack()

    daftar_text = """
    1. Retno Setyoningsih
    2. Ketrin Anastasya
    3. Heva Maya Oktaviana
    4. Fausiah Zahra
    5. Anisa Eka Wulandari
    """
    daftar_mahasiswa_label = tk.Label(daftar_mahasiswa_window, text=daftar_text)
    daftar_mahasiswa_label.pack()

def cek_ketersediaan_matkul(mata_kuliah):
    mata_kuliah_list = ["Logika Informatika dan Sistem Digital", "Algoritma dan Pemrograman", "Arsitektur dan Organisasi Komputer", "Matematika Diskrit"]
    if mata_kuliah in mata_kuliah_list:
        return True
    else:
        return False

def cek_mata_kuliah():
    mata_kuliah_text = mata_kuliah_entry.get()
    try:
        mata_kuliah = mata_kuliah_text
        if cek_ketersediaan_matkul(mata_kuliah):
            messagebox.showinfo("Ketersediaan Mata Kuliah", f"{mata_kuliah} Tersedia di Kampus.")
        else:
            messagebox.showinfo("Ketersediaan Mata Kuliah", f"{mata_kuliah} Tidak Tersedia di Kampus.")
            mata_kuliah_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error!", "Masukkan Harus Berupa Teks.")

def keluar():
    root.destroy()

root = tk.Tk()
root.title("Aplikasi Kampus")

daftar_button = tk.Button(root, text="Daftar Mahasiswa", command=tampilkan_daftar_mahasiswa)
daftar_button.pack()

mata_kuliah_label = tk.Label(root, text="Masukkan Mata Kuliah : ")
mata_kuliah_label.pack()

mata_kuliah_entry = tk.Entry(root)
mata_kuliah_entry.pack()

cek_mata_kuliah_button = tk.Button(root, text="Cek Mata Kuliah", command=cek_mata_kuliah)
cek_mata_kuliah_button.pack()

exit_button = tk.Button(root, text="Keluar", command=keluar)
exit_button.pack()

root.mainloop()
