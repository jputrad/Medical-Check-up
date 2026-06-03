import tkinter as tk

def cek_suhu():
    try:
        suhu = int(entry.get())
        if suhu >= 38:
            hasil.config(text=" Anda Sehat WalafiaSebentar Lagi anda Akan Meninggal", fg="red")
        else:
            hasil.config(text="✅Sehat, Sesok Kuliah", fg="green")
    except:
        hasil.config(text="Input harus angka!", fg="orange")

# Buat window utama
root = tk.Tk()
root.title("Cek Prediksi Kematian")
root.geometry("300x200")
root.configure(bg="#f0f0f0")

# Judul
label = tk.Label(root, text="Masukkan Suhu (°C):", font=("Arial", 12), bg="#f0f0f0")
label.pack(pady=10)

# Input
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

# Tombol
tombol = tk.Button(root, text="Cek", command=cek_suhu, font=("Arial", 12), bg="#4CAF50", fg="white")
tombol.pack(pady=10)

# Output
hasil = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0")
hasil.pack(pady=10)

root.mainloop()
