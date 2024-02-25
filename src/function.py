from tabulate import tabulate
import os


def clear_screen():
         """
         A function to clean the user interface
         """
         # For Windows
         if os.name == 'nt':
                  _ = os.system('cls')
         # For macOS and Linux
         else:
                  _ = os.system('clear')

def int_validation(prompt):
         """
         Fungsi untuk melakukan validasi input bilangan bulat positif.
         """

         while True:
                  try:
                           integer = int(input(prompt))
                           if integer < 0:
                                    print("\nPeringatan : masukan anda tidak boleh negatif !")
                                    clear_screen()
                                    continue
                           else:
                                    return integer
                  except ValueError:
                                    clear_screen()
                                    print("\nPeringatan : Silakan masukan bilangan bulat !")


def str_validation(str):
         """
         Fungsi untuk melakukan validasi inputan str atau bukan
         """

         while True : 
                  setense = input(str)
                  if setense.isalnum() or setense.replace(" ", "").upper():
                           return setense
                  else:
                           print('Peringatan : Silahkan input alfabet yang benar!')
                           continue


def data_table(data, coloums, title):
         """
         Fungsi untuk membuat sebuah tabel dengan library tabulate
         """

         numbered_data = [[i + 1] + row for i, row in enumerate(data)]
         print(title.center(80))
         print(tabulate(numbered_data, headers=coloums, tablefmt='fancy_grid'))

def show_menu_data(database):
         #variabel menu read data
         read_menu_data = '''
                  SELAMAT DATANG DI TOKO BERKAH JAYA

Menu Read Data : 

1. Tampilkan Data Barang
2. Cari Data Barang
3. Kembali Menu Utama

Silahkan Pilih Angka 1 sampai 3 : '''
                  
         while True:
                  choice_read = int_validation(read_menu_data)
                  clear_screen()
                  if choice_read == 1:   
                           data_table(
                           data=database.values(),
                           coloums=['No', 'Kode Barang', 'Nama Barang','Harga', 'Stok' , 'Keterangan'],
                           title='\nTABEL BARANG TOKO BERKAH JAYA\n'         
                           )
                  elif choice_read == 2:
                           data_table(
                           data=database.values(),
                           coloums=['No', 'Kode Barang', 'Nama Barang','Harga', 'Stok' , 'Keterangan'],
                           title='\nTABEL BARANG TOKO BERKAH JAYA\n'         
                           ) 
                           show_data_filter(database)
                  elif choice_read == 3 :
                           break
                  else :
                           print('Masukan angka 1 sampai 3 !')
                           continue

def show_data_filter(database):
         
         while True:
                  kode_barang = str_validation('\nMasukan kode barang : ')
                  clear_screen()
                  for item in database.values():
                           if kode_barang.upper() == item[0]:
                                    data_table(
                                             data=[item],
                                             coloums=['No', 'Kode Barang', 'Nama Barang', 'Harga', 'Stok', 'Keterangan'],
                                             title='\nTABEL BARANG TOKO BERKAH JAYA\n'
                                    )
                                    print('\nBarang yang Anda cari telah ditemukan.\n')
                                    return  # Berhenti dari fungsi setelah menampilkan data
                  else:
                           print('\nMohon maaf kode barang yang Anda cari tidak ada, mohon priksa kembali kode barang.')
                           break


def add_data_barang(database):
         """
         Fungsi untuk menambahkan data barang
         """

         #variabel menu add data barang
         read_add_data = '''
                  SELAMAT DATANG DI TOKO BERKAH JAYA

Menu Tambah Data : 

1. Tambahkan Data Barang
2. Kembali Menu Utama

Silahkan Pilih Angka 1 sampai 2 : '''

         while True:
                  choice_add = int_validation(read_add_data)
                  clear_screen()  
                  if choice_add == 1:
                           while True:
                                    print("""\n                     MENAMBAHKAN DATA BARANG         \n""")
                                    kode_barang = str_validation('Masukan Kode Barang : ')
                                    # Validasi panjang kode barang dan awalan "KB"
                                    if len(kode_barang) != 5 or not kode_barang.startswith("KB"):
                                             print("Kode barang harus memiliki panjang 5 karakter dan diawali dengan 'KB'. Contoh : 'KB999'")
                                             continue

                                    items = list(database.values())
                                    if not items:
                                             nama_barang = str_validation('Masukkan Nama Barang: ')
                                             harga = int_validation('Masukkan Harga Barang: ')
                                             stok = int_validation('Masukkan Stok Barang: ')
                                             keterangan = str_validation('Masukkan Keterangan: ')

                                             validasi_save = str_validation('\nAnda ingin save (y/t): ')
                                             if validasi_save.lower() == 'y':
                                                      database.update({
                                                               f'{nama_barang}': [
                                                               kode_barang.upper(),
                                                               nama_barang,
                                                               harga,
                                                               stok,
                                                               keterangan]
                                                      })
                                                      data_table(
                                                                        data=database.values(),
                                                                        coloums=['No', 'Kode Barang', 'Nama Barang', 'Harga', 'Stok', 'Keterangan'],
                                                                        title='\nTABEL BARANG TOKO BERKAH JAYA\n'
                                                               )
                                                      print('\nData Berhasil Disimpan.')
                                                      break
                                    #meriksa apakah kode barang sudah ada atau belum   
                                    else:              
                                             for item in items:
                                                      if kode_barang.upper() == item[0]:
                                                               print('Mohon maaf kode barang yang anda masukan sudah terdaftar.')
                                                               break
                                                      else:    
                                                               nama_barang = str_validation('Masukan Nama Barang : ')
                                                               harga = int_validation('Masukan Harga Barang : ')
                                                               stok = int_validation('Masukan Stok Barang : ')
                                                               keterangan = str_validation('Masukan Keterangan : ')

                                                      validasi_save = str_validation('\nAnda ingin save (y/t) : ')
                                                      
                                                      if validasi_save.lower() == 'y' :
                                                               database.update({
                                                                        f'{nama_barang}': [
                                                                                 kode_barang.upper(),
                                                                                 nama_barang,
                                                                                 harga,
                                                                                 stok,
                                                                                 keterangan]
                                                                                 })
                                                               data_table(
                                                               data=database.values(),
                                                               coloums=['No', 'Kode Barang', 'Nama Barang','Harga', 'Stok' , 'Keterangan'],
                                                               title='\nTABEL BARANG TOKO BERKAH JAYA\n'         
                                                               )
                                                               print('\nData Berhasil Disimpan.')
                                                               break
                                                      else:
                                                               data_table(
                                                               data=database.values(),
                                                               coloums=['No', 'Kode Barang', 'Nama Barang','Harga', 'Stok' , 'Keterangan'],
                                                               title='\nTABEL BARANG TOKO BERKAH JAYA\n'         
                                                               )
                                                               break
                                             break
                                    break
                  elif choice_add == 2 :
                           break
                  else:
                           print('Masukan angka 1 sampai 2 !')
                           continue

def update_data(database):
    """
    Fungsi untuk menambahkan data barang
    """
    # Variabel menu update data
    update_data_menu = '''
                  SELAMAT DATANG DI TOKO BERKAH JAYA

Menu Update Data : 

1. Update Data Barang
2. Kembali Menu Utama

Silahkan Pilih Angka 1 sampai 2 : '''

    while True:
        choice_update = int_validation(update_data_menu)
        clear_screen()
        if choice_update == 1:
            data_table(data=database.values(),
                       coloums=['No', 'Kode Barang', 'Nama Barang', 'Harga', 'Stok', 'Keterangan'],
                       title='\nTABEL BARANG TOKO BERKAH JAYA\n')

            while True:
                print("""\n                     UPDATE DATA BARANG         \n""")
                kode_barang = str_validation('Masukan Kode Barang yang Akan di Update : ')
                clear_screen()
                # Validasi panjang kode barang dan awalan "KB"
                if len(kode_barang) != 5 or not kode_barang.startswith("KB"):
                    print("Kode barang harus memiliki panjang 5 karakter dan diawali dengan 'KB'. Contoh : 'KB999'")
                    continue

                items = list(database.values())
                item_found = False

                # Periksa apakah kode barang sudah ada atau belum
                for item in items:
                    if kode_barang.upper() == item[0]:
                        data_table(data=[item],
                                   coloums=['No', 'Kode Barang', 'Nama Barang', 'Harga', 'Stok', 'Keterangan'],
                                   title='\nTABEL BARANG TOKO BERKAH JAYA\n')

                        print('\nBarang yang Anda ingin update.\n')

                        choice_validasi = str_validation('Apakah ingin melanjutkan update data diatas [y/t] ? : ')

                        if choice_validasi.lower() == 'y':
                            while True:
                                choice_update_column = str_validation('Masukan Nama Kolom yang Akan di Update : ')
                                if choice_update_column.title() not in ['Nama Barang', 'Harga', 'Stok', 'Keterangan']:
                                    print('Nama kolom tidak valid.')
                                    continue
                                else:
                                    new_data = str_validation(f'Masukan Data yang baru untuk {choice_update_column}: ')
                                    if choice_update_column.title() == 'Stok':
                                           a = int(new_data)
                                           item[3] += a
                                           break
                                    else:
                                             validasi_save = str_validation('\nAnda ingin save (y/t) : ')
                                             if validasi_save.lower() == 'y' :
                                                      item[['Kode Barang', 'Nama Barang', 'Harga', 'Stok', 'Keterangan'].index(choice_update_column.title())] = new_data
                                                      item_found = True
                                                      break
                                             break
                        break
                if not item_found:
                    clear_screen()
                    data_table(
                    data=database.values(),
                    coloums=['No', 'Kode Barang', 'Nama Barang', 'Harga', 'Stok', 'Keterangan'],
                    title='\nTABEL BARANG TOKO BERKAH JAYA\n'
                  )
                    print(f'\nData tidak jadi di Update.')
                    break
                else:
                    clear_screen()
                    data_table(
                    data=database.values(),
                    coloums=['No', 'Kode Barang', 'Nama Barang', 'Harga', 'Stok', 'Keterangan'],
                    title='\nTABEL BARANG TOKO BERKAH JAYA\n'
                  )
                    print(f'\nData Kolom "{choice_update_column}" berhasil diperbarui.')
                    break
        elif choice_update == 2:
            break
        else:
            print('Masukan angka 1 sampai 2 !')


def delete_data(database):
    '''
    Fungsi untuk melakukan delete data barang
    '''
    update_data = '''
                  SELAMAT DATANG DI TOKO BERKAH JAYA

Menu Delete Data : 

1. Delete Data Barang
2. Kembali Menu Utama

Silahkan Pilih Angka 1 sampai 2 : '''

    while True:
        choice_add = int_validation(update_data)
        clear_screen()
        if choice_add == 1:
            while True:
                print("""\nMENGHAPUS DATA BARANG\n""")
                data_table(
                    data=database.values(),
                    coloums=['No', 'Kode Barang', 'Nama Barang', 'Harga', 'Stok', 'Keterangan'],
                    title='\nTABEL BARANG TOKO BERKAH JAYA\n'
                )
                kode_barang = str_validation('\nMasukan Kode Barang : ')
                # Validasi panjang kode barang dan awalan "KB"
                if len(kode_barang) != 5 or not kode_barang.startswith("KB"):
                    print("\nKode barang harus memiliki panjang 5 karakter dan diawali dengan 'KB'. Contoh : 'KB999'")
                    continue

                item_found = False
                # Mencari item berdasarkan kode barang
                for key, value in database.items():
                    if value[0] == kode_barang.upper():
                        item_found = True
                        clear_screen()
                        data_table(
                            data=[value],
                            coloums=['No', 'Kode Barang', 'Nama Barang', 'Harga', 'Stok', 'Keterangan'],
                            title='\nData yang akan dihapus:\n'
                        )
                        validasi_delete = str_validation(f'\nAnda ingin mendelete data dengan kode {kode_barang} (y/t) : ')
                        if validasi_delete.lower() == 'y':
                            del database[key]  # Hapus item dari database
                            print("\nData berhasil dihapus.")
                        break  # Keluar dari loop pencarian

                if not item_found:
                    print('\nMohon maaf data yang anda cari tidak ada.')

                lagi = str_validation("\nApakah Anda ingin menghapus data lagi? (y/t) : ")
                if lagi.lower() != 'y':
                    break  # Keluar dari loop hapus data

        elif choice_add == 2:
            break  # Keluar dari loop menu delete data
        else:
            print('\nMasukan angka 1 sampai 2 !')


