import os
from datetime import datetime

print(10 * "=", "CRUD MENGHAPUS FILE", 10 * "=")

def file_age(file_path):
    # Mendapatkan tanggal modifikasi file
    modified_time = os.path.getmtime(file_path)
    modified_date = datetime.fromtimestamp(modified_time)

    # Mendapatkan tanggal saat ini
    current_date = datetime.now()
    difference = current_date - modified_date
    return difference.days

def delete_file_if_old(file_path):
    age_in_days = file_age(file_path)
    if age_in_days > 3:      #jika file berusia lebih dari 3 hari otomatis terhapus
        os.remove(file_path)
        print(f"File {file_path} telah dihapus karena sudah berada selama lebih dari 3 hari.")
    else:
        print(f"File {file_path} belum berusia lebih dari 3 hari. Tidak perlu dihapus.")


# Contoh pemakaian
folder_path = "D:\Magang\Tugas Crud\sampah"
files = os.listdir(folder_path)

for file in files:
    file_path = os.path.join(folder_path, file)
    if os.path.isfile(file_path):
        delete_file_if_old(file_path)
