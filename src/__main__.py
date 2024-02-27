import function
import csv
import sys
import os

def initialize_db():
         """
         Funsi ini berfungsi sebagai inisialisasi data yang diambil dari db
         """
         database = {}  # Inisialisasi database
         try:
                  with open(PATH, 'r') as file:
                           reader = csv.reader(file, delimiter=';')
                           # Cek apakah file CSV kosong
                           if not any(row for row in reader):
                                    print("Perhatian : File CSV kosong.")
                                    return database
                           
                           # Reset posisi file ke awal
                           file.seek(0)
                           
                           # Baca file CSV dan inisialisasi database
                           for row in reader:
                                    kode_barang, nama, harga, stok, keterangan = row
                                    database.update({nama: [kode_barang, nama, f"Rp.{int(harga)}", f"{int(stok)} pck", keterangan]})
         except FileNotFoundError:
                  print("Perhatian : File tidak ditemukan.")
         except ValueError:
                  print("Perhatian : Format file CSV tidak sesuai.")
         except Exception as e:
                  print("Perhatian : Terjadi kesalahan:", str(e))
         return database

def main():
         """
         Main Program utama
         """

         while True : 
                  #inputan dari user
                  choice = function.int_validation(main_menu)
                  function.clear_screen()
                  if choice == 1 :
                           function.show_menu_data(database)
                           function.clear_screen()
                  elif choice == 2 :
                           function.add_data_barang(database)
                           function.clear_screen()
                  elif choice == 3 :
                           function.update_data(database)
                           function.clear_screen()
                  elif choice == 4 :
                           function.delete_data(database)
                           function.clear_screen()
                  elif choice == 5:
                           function.pembelian(database)
                           function.clear_screen()
                  elif choice == 6:
                           print(f'Terimakasih....{username} sampai jumpa kembali\n')
                           break
                  else:
                           print('Masukan angka 1 sampai 5 !')
                           continue

                  # Menjaga agar database selalu diperbarui
         with open(PATH, 'w') as file:
                  # Membuat objek writer
                  writer = csv.writer(file, delimiter=";")
                  # Menulis data ke dalam file csv
                  writer.writerows(database.values())



if __name__ == "__main__":

                  #mendefinisikan menu utama aplikasi
                  main_menu = '''
                  SELAMAT DATANG DI TOKO BERKAH JAYA

Menu Utama : 

1. Menampilkan Data Barang
2. Menambahkan Data Barang
3. Update Data Barang
4. Menghapus Data Barang
5. Cek Out Barang 
6. Exit

Silahkan Pilih Angka 1 sampai 6 : '''

                  if getattr(sys, 'frozen', False):
                           PATH = sys._MEIPASS
                           PATH = os.path.join(PATH, 'data/db.csv') 
                  else:
                           PATH = os.getcwd()
                           PATH = os.path.join(PATH, 'data/db.csv') 

         # Membersihkan tampilan user
function.clear_screen()

         # Initializing database
database = initialize_db()


while True :
                           function.clear_screen()
                           print("""
                                             LOGIN APP TOKO BERKAH JAYA
                  """)     
                           username = function.str_validation('Masukan username : ')
                           password = function.str_validation('Masukan password : ')

                           if username.lower() == 'topik' and password.lower() == '123':
                                    #menjalankan menu utama
                                    print(f'Berhasil login.... Selamat datang {username}')
                                    main()
                           else:
                                    print('\nUsername dan Password yang anda masukan Salah.')
                                    while True:
                                             choice = function.str_validation("\nApakah Anda ingin mencoba login lagi? (y/n): ").lower()
                                             if choice == 'y':
                                                      break  # Kembali ke loop login utama
                                             elif choice == 'n':
                                                      print("\nTerima kasih telah menggunakan aplikasi. Sampai jumpa!")
                                                      exit()  # Keluar dari program
                                             else:
                                                      print("\nMasukan tidak valid. Mohon masukkan 'y' atau 'n'.")
                                                      continue
                                    continue