import os
from datetime import datetime

print(10 * "=", "CRUD MENGHAPUS FILE", 10 * "=")


def file_age(file_path):
    # Mendapatkan tanggal modifikasi file
    modified_time = os.path.getmtime(file_path)
    modified_date = datetime.fromtimestamp(modified_time)

    # Mendapatkan tanggal saat ini
    tanggal_sekarang = datetime.now()

    # Menghitung selisih waktu antara tanggal modifikasi dan tanggal saat ini
    selisih = tanggal_sekarang - modified_date
    print(f"selisih hari : {selisih}")
    return selisih

def delete_file_jika_lama(file_path):
    # Memeriksa usia file
    selisih = file_age(file_path)

    # Jika usia file melebihi 7 hari dan nama file mengandung "Screenshot", hapus file
    if selisih.days > 7 and "Screenshot" in file_path:
        os.remove(file_path)
        print(f"File {file_path} telah dihapus karena sudah berada selama lebih dari 7 hari.")
    else:
        print(f"File {file_path} belum berusia lebih dari 7 hari atau bukan file 'Screenshot'. Tidak perlu dihapus.")


# Contoh pemakaian
direktori_screenshot = "D:\Magang\Tugas Crud\sampah"
files = os.listdir(direktori_screenshot)

for file in files:
    file_path = os.path.join(direktori_screenshot, file)
    if os.path.isfile(file_path):
        delete_file_jika_lama(file_path)