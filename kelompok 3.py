
# Menampilkan pesan selamat datang di Pizza Hut
print("Selamat Datang di Pizza Hut")
# Menampilkan pesan untuk memilih menu yang tersedia
print("Silahkan Pilih Menu yang Tersedia: ")
# Menampilkan daftar topping pizza beserta harga
print("+=============================================================+")
print("| No |      Topping Pizza        |            Harga           |")
print("+=============================================================+")
print("| 1. | Frankfurter BBQ           |           Rp 43.637        |")
print("| 2. | Meat Monsta               |           Rp 43.637        |")
print("| 3. | Super Supreme             |           Rp 43.637        |")
print("| 4. | Super Supreme Chicken     |           Rp 43.637        |")
print("+=============================================================+")

# Meminta pelanggan untuk memilih topping pizza
toppingPizza = str(input("Silahkan pilih topping pizza yang Anda inginkan: "))
# Inisialisasi harga topping
hargaTopping = 43637
# Inisialisasi harga pizza
hargaPizza = 0

# Memulai proses pemilihan topping pizza
if toppingPizza == "1":
    # Jika topping pizza yang dipilih adalah Frankfurter BBQ
    print("Anda telah memilih Frankfurter BBQ. ")
    print("====================================")
    # Menampilkan daftar crust yang tersedia beserta dengan harga
    print("Pilihan Crust yang tersedia: ")
    print("+=============================================================+")
    print("| No |      Pilihan Crust        |           Harga            |")
    print("+=============================================================+")
    print("| 1. | Pan                       |         Rp 0               |")
    print("| 2. | StuffedCrust Cheese       |         Rp 11.818          |")
    print("| 3. | StuffedCrust Sausage      |         Rp 9.091           |")
    print("| 4. | Cheese Bites              |         Rp 13.636          |")
    print("| 5. | Crown Crust               |         Rp 11.818          |")
    print("+=============================================================+")

    # Inisialisasi harga crust
    pan = 0
    stuffedCrustCheese = 11818
    stuffedCrustSausage = 9091
    cheeseBites = 13636
    crownCrust = 11818

    # Meminta pelanggan untuk memilih crust
    pilihanCrust = str(input("Silahkan pilih Crust yang Anda inginkan: "))
    # Memulai proses pemilihan crust
    if pilihanCrust == "1":
        # Jika crust yang dipilih adalah Pan
        print("Anda telah memilih Pan")
        # Menampilkan daftar ukuran pizza beserta harga
        print("Berikut adalah ukuran pizza yang tersedia beserta dengan harganya: ")
        print("+=============================================================+")
        print("| No |       Ukuran Pizza        |           Harga            |")
        print("+=============================================================+")
        print("| 1. | Personal                  |         Rp 0               |")
        print("| 2. | Regular                   |         Rp 57.273          |")
        print("| 3. | Large                     |         Rp 89.091          |")
        print("+=============================================================+")

        # Meminta pelanggan untuk memilih ukuran pizza
        ukuranPizza = str(input("Apa ukuran Pizza yang Anda inginkan: "))
        # Inisialisasi harga ukuran pizza
        personal = 0
        regular = 57273
        large = 89091
        # Memulai proses pemilihan ukuran pizza
        if ukuranPizza == "1":
            # Jika ukuran pizza yang dipilih adalah personal
            print("Anda telah memilih ukuran Pizza yang Personal")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 13.636? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 13636
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + pan + personal + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga pizza
                hargaPizza = (hargaTopping + pan + personal)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "2":
            # Jika ukuran pizza yang dipilih adalah regular
            print("Anda telah memilih ukuran Pizza yang Regular")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 16.364? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 16364
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + pan + regular + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + pan + regular)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "3":
            # Jika ukuran pizza yang dipilih adalah large
            print("Anda telah memilih ukuran Pizza yang Large")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 19.091? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 19091
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + pan + large + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + pan + large)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        else:
            # Menampilkan jika ukuran pizza yang dipilih tidak tersedia
            print("Ukuran Pizza yang Anda pilih tidak tersedia")            
    elif pilihanCrust == "2":
        # Jika crust yang dipilih adalah StuffedCrust Cheese
        print("Anda telah memilih StuffedCrust cheese")
        # Menampilkan daftar ukuran pizza beserta harga
        print("Berikut adalah ukuran pizza yang tersedia beserta dengan harganya: ")
        print("+=============================================================+")
        print("| No |       Ukuran Pizza        |           Harga            |")
        print("+=============================================================+")
        print("| 1. | Personal                  |         Rp 0               |")
        print("| 2. | Regular                   |         Rp 65.455          |")
        print("| 3. | Large                     |         Rp 104.545         |")
        print("+=============================================================+")

        # Meminta pelanggan untuk memilih ukuran pizza
        ukuranPizza = str(input("Apa ukuran Pizza yang Anda inginkan: "))
        # Inisialisasi harga ukuran pizza
        personal = 0
        regular = 65455
        large = 104545
        # Memulai proses pemilihan ukuran pizza
        if ukuranPizza == "1":
            # Jika ukuran pizza yang dipilih adalah personal
            print("Anda telah memilih ukuran Pizza yang Personal")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 13.636? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 13636
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustCheese + personal + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustCheese + personal)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "2":
            # Jika ukuran pizza yang dipilih adalah regular
            print("Anda telah memilih ukuran Pizza yang Regular")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 16.364? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 16364
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustCheese + regular + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustCheese + regular)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "3":
            # Jika ukuran pizza yang dipilih adalah large
            print("Anda telah memilih ukuran Pizza yang Large")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 19.091? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 19091
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustCheese + large + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustCheese + large)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        else:
            # Menampilkan jika ukuran pizza yang dipilih tidak tersedia
            print("Ukuran Pizza yang Anda pilih tidak tersedia")            
    elif pilihanCrust == "3":
        # Jika crust yang dipilih adalah StuffedCrust Sausage
        print("Anda telah memilih StuffedCrust Sausage")
        # Menampilkan daftar ukuran pizza beserta harga
        print("Berikut adalah ukuran pizza yang tersedia beserta dengan harganya: ")
        print("+=============================================================+")
        print("| No |       Ukuran Pizza        |           Harga            |")
        print("+=============================================================+")
        print("| 1. | Personal                  |         Rp 0               |")
        print("| 2. | Regular                   |         Rp 64.545          |")
        print("| 3. | Large                     |         Rp 102.727         |")
        print("+=============================================================+")

        # Meminta pelanggan untuk memilih ukuran pizza
        ukuranPizza = str(input("Apa ukuran Pizza yang Anda inginkan: "))
        # Inisialisasi harga ukuran pizza
        personal = 0
        regular = 64455
        large = 102727
        # Memulai proses pemilihan ukuran pizza
        if ukuranPizza == "1":
            # Jika ukuran pizza yang dipilih adalah personal
            print("Anda telah memilih ukuran Pizza yang Personal")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 13.636? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 13636
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustSausage + personal + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustSausage + personal)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "2":
            # Jika ukuran pizza yang dipilih adalah regular
            print("Anda telah memilih ukuran Pizza yang Regular")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 16.364? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 16364
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y 
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustSausage + regular + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                 # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustSausage + regular)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "3":
            # Jika ukuran pizza yang dipilih adalah large
            print("Anda telah memilih ukuran Pizza yang Large")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 19.091? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 19091
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustSausage + large + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustSausage + large)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        else:
            # Menampilkan jika ukuran pizza yang dipilih tidak tersedia
            print("Ukuran Pizza yang Anda pilih tidak tersedia")
    elif pilihanCrust == "4":
        # Jika crust yang dipilih adalah Cheese Bites
        print("Anda telah memilih Cheese Bites")
        # Menampilkan daftar ukuran pizza beserta harga
        print("Berikut adalah ukuran pizza yang tersedia beserta dengan harganya: ")
        print("+=============================================================+")
        print("| No |       Ukuran Pizza        |           Harga            |")
        print("+=============================================================+")
        print("| 1. | Personal                  |         Rp 0               |")
        print("| 2. | Regular                   |         Rp 66.364          |")
        print("| 3. | Large                     |         Rp 107.273         |")
        print("+=============================================================+")

        # Meminta pelanggan untuk memilih ukuran pizza
        ukuranPizza = str(input("Apa ukuran Pizza yang Anda inginkan: "))
        # Inisialisasi harga ukuran pizza
        personal = 0
        regular = 66364
        large = 107273
        # Memulai proses pemilihan ukuran pizza
        if ukuranPizza == "1":
            # Jika ukuran pizza yang dipilih adalah personal
            print("Anda telah memilih ukuran Pizza yang Personal")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 13.636? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 13636
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + cheeseBites + personal + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + cheeseBites + personal)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "2":
            # Jika ukuran pizza yang dipilih adalah regular
            print("Anda telah memilih ukuran Pizza yang Regular")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 16.364? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 16364
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + cheeseBites + regular + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + cheeseBites + regular)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "3":
            # Jika ukuran pizza yang dipilih adalah large
            print("Anda telah memilih ukuran Pizza yang Large")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 19.091? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 19091
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + cheeseBites + large + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + cheeseBites + large)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        else:
            # Menampilkan jika ukuran pizza yang dipilih tidak tersedia
            print("Ukuran Pizza yang Anda pilih tidak tersedia")
    elif pilihanCrust == "5":
        # Jika crust yang dipilih adalah Crown Crust
        print("Anda telah memilih Crown Crust")
        # Menampilkan daftar ukuran pizza beserta harga
        print("Berikut adalah ukuran pizza yang tersedia beserta dengan harganya: ")
        print("+=============================================================+")
        print("| No |       Ukuran Pizza        |           Harga            |")
        print("+=============================================================+")
        print("| 1. | Personal                  |         Rp 0               |")
        print("| 2. | Regular                   |         Rp 65.455          |")
        print("| 3. | Large                     |         Rp 104.545         |")
        print("+=============================================================+")

        # Meminta pelanggan untuk memilih ukuran pizza
        ukuranPizza = str(input("Apa ukuran Pizza yang Anda inginkan: "))
        # Inisialisasi harga ukuran pizza
        personal = 0
        regular = 65455
        large = 104545
        # Memulai proses pemilihan ukuran pizza
        if ukuranPizza == "1":
            # Jika ukuran pizza yang dipilih adalah personal
            print("Anda telah memilih ukuran Pizza yang Personal")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 13.636? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 13636
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + crownCrust + personal + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + crownCrust + personal)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "2":
            # Jika ukuran pizza yang dipilih adalah regular
            print("Anda telah memilih ukuran Pizza yang Regular")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 16.364? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 16364
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + crownCrust + regular + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + crownCrust + regular)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "3":
            # Jika ukuran pizza yang dipilih adalah large
            print("Anda telah memilih ukuran Pizza yang Large")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 19.091? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 19091
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + crownCrust + large + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                 # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + crownCrust + large)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        else:
            # Menampilkan jika ukuran pizza yang dipilih tidak tersedia
            print("Ukuran Pizza yang Anda pilih tidak tersedia")
    else:
        # Menampilkan jika pilihan crust tidak tersedia
        print("Crust yang Anda pilih tidak tersedia, silahkan pilih crust yang tersedia.")
elif toppingPizza == "2":
    # Jika topping pizza yang dipilih adalah Meat Monsta
    print("Anda telah memilih Meat Monsta")
    print("====================================")
    # Menampilkan daftar crust yang tersedia beserta dengan harga
    print("Pilihan Crust yang tersedia: ")
    print("+=============================================================+")
    print("| No |      Pilihan Crust        |           Harga            |")
    print("+=============================================================+")
    print("| 1. | Pan                       |         Rp 0               |")
    print("| 2. | StuffedCrust Cheese       |         Rp 11.818          |")
    print("| 3. | StuffedCrust Sausage      |         Rp 9.091           |")
    print("| 4. | Cheese Bites              |         Rp 13.636          |")
    print("| 5. | Crown Crust               |         Rp 11.818          |")
    print("+=============================================================+")

    # Inisialisasi harga crust
    pan = 0
    stuffedCrustCheese = 11818
    stuffedCrustSausage = 9091
    cheeseBites = 13636
    crownCrust = 11818

    # Meminta pelanggan untuk memilih crust
    pilihanCrust = str(input("Silahkan pilih Crust yang Anda inginkan: "))
    # Memulai proses pemilihan crust
    if pilihanCrust == "1":
        # Jika crust yang dipilih adalah Pan
        print("Anda telah memilih Pan")
        # Menampilkan daftar ukuran pizza beserta harga
        print("Berikut adalah ukuran pizza yang tersedia beserta dengan harganya: ")
        print("+=============================================================+")
        print("| No |       Ukuran Pizza        |           Harga            |")
        print("+=============================================================+")
        print("| 1. | Personal                  |         Rp 0               |")
        print("| 2. | Regular                   |         Rp 57.273          |")
        print("| 3. | Large                     |         Rp 89.091          |")
        print("+=============================================================+")

        # Meminta pelanggan untuk memilih ukuran pizza
        ukuranPizza = str(input("Apa ukuran Pizza yang Anda inginkan: "))
        # Inisialisasi harga ukuran pizza
        personal = 0
        regular = 57273
        large = 89091
        # Memulai proses pemilihan ukuran pizza
        if ukuranPizza == "1":
            # Jika ukuran pizza yang dipilih adalah personal
            print("Anda telah memilih ukuran Pizza yang Personal")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 13.636? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 13636
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + pan + personal + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga pizza
                hargaPizza = (hargaTopping + pan + personal)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "2":
            # Jika ukuran pizza yang dipilih adalah regular
            print("Anda telah memilih ukuran Pizza yang Regular")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 16.364? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 16364
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + pan + regular + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + pan + regular)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "3":
            # Jika ukuran pizza yang dipilih adalah large
            print("Anda telah memilih ukuran Pizza yang Large")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 19.091? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 19091
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + pan + large + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + pan + large)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        else:
            # Menampilkan jika ukuran pizza yang dipilih tidak tersedia
            print("Ukuran Pizza yang Anda pilih tidak tersedia")            
    elif pilihanCrust == "2":
        # Jika crust yang dipilih adalah StuffedCrust Cheese
        print("Anda telah memilih StuffedCrust cheese")
        # Menampilkan daftar ukuran pizza beserta harga
        print("Berikut adalah ukuran pizza yang tersedia beserta dengan harganya: ")
        print("+=============================================================+")
        print("| No |       Ukuran Pizza        |           Harga            |")
        print("+=============================================================+")
        print("| 1. | Personal                  |         Rp 0               |")
        print("| 2. | Regular                   |         Rp 65.455          |")
        print("| 3. | Large                     |         Rp 104.545         |")
        print("+=============================================================+")

        # Meminta pelanggan untuk memilih ukuran pizza
        ukuranPizza = str(input("Apa ukuran Pizza yang Anda inginkan: "))
        # Inisialisasi harga ukuran pizza
        personal = 0
        regular = 65455
        large = 104545
        # Memulai proses pemilihan ukuran pizza
        if ukuranPizza == "1":
            # Jika ukuran pizza yang dipilih adalah personal
            print("Anda telah memilih ukuran Pizza yang Personal")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 13.636? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 13636
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustCheese + personal + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustCheese + personal)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "2":
            # Jika ukuran pizza yang dipilih adalah regular
            print("Anda telah memilih ukuran Pizza yang Regular")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 16.364? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 16364
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustCheese + regular + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustCheese + regular)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "3":
            # Jika ukuran pizza yang dipilih adalah large
            print("Anda telah memilih ukuran Pizza yang Large")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 19.091? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 19091
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustCheese + large + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustCheese + large)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        else:
            # Menampilkan jika ukuran pizza yang dipilih tidak tersedia
            print("Ukuran Pizza yang Anda pilih tidak tersedia")            
    elif pilihanCrust == "3":
        # Jika crust yang dipilih adalah StuffedCrust Sausage
        print("Anda telah memilih StuffedCrust Sausage")
        # Menampilkan daftar ukuran pizza beserta harga
        print("Berikut adalah ukuran pizza yang tersedia beserta dengan harganya: ")
        print("+=============================================================+")
        print("| No |       Ukuran Pizza        |           Harga            |")
        print("+=============================================================+")
        print("| 1. | Personal                  |         Rp 0               |")
        print("| 2. | Regular                   |         Rp 64.545          |")
        print("| 3. | Large                     |         Rp 102.727         |")
        print("+=============================================================+")

        # Meminta pelanggan untuk memilih ukuran pizza
        ukuranPizza = str(input("Apa ukuran Pizza yang Anda inginkan: "))
        # Inisialisasi harga ukuran pizza
        personal = 0
        regular = 64455
        large = 102727
        # Memulai proses pemilihan ukuran pizza
        if ukuranPizza == "1":
            # Jika ukuran pizza yang dipilih adalah personal
            print("Anda telah memilih ukuran Pizza yang Personal")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 13.636? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 13636
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustSausage + personal + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustSausage + personal)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "2":
            # Jika ukuran pizza yang dipilih adalah regular
            print("Anda telah memilih ukuran Pizza yang Regular")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 16.364? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 16364
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y 
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustSausage + regular + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                 # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustSausage + regular)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "3":
            # Jika ukuran pizza yang dipilih adalah large
            print("Anda telah memilih ukuran Pizza yang Large")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 19.091? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 19091
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustSausage + large + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustSausage + large)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        else:
            # Menampilkan jika ukuran pizza yang dipilih tidak tersedia
            print("Ukuran Pizza yang Anda pilih tidak tersedia")
    elif pilihanCrust == "4":
        # Jika crust yang dipilih adalah Cheese Bites
        print("Anda telah memilih Cheese Bites")
        # Menampilkan daftar ukuran pizza beserta harga
        print("Berikut adalah ukuran pizza yang tersedia beserta dengan harganya: ")
        print("+=============================================================+")
        print("| No |       Ukuran Pizza        |           Harga            |")
        print("+=============================================================+")
        print("| 1. | Personal                  |         Rp 0               |")
        print("| 2. | Regular                   |         Rp 66.364          |")
        print("| 3. | Large                     |         Rp 107.273         |")
        print("+=============================================================+")

        # Meminta pelanggan untuk memilih ukuran pizza
        ukuranPizza = str(input("Apa ukuran Pizza yang Anda inginkan: "))
        # Inisialisasi harga ukuran pizza
        personal = 0
        regular = 66364
        large = 107273
        # Memulai proses pemilihan ukuran pizza
        if ukuranPizza == "1":
            # Jika ukuran pizza yang dipilih adalah personal
            print("Anda telah memilih ukuran Pizza yang Personal")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 13.636? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 13636
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + cheeseBites + personal + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + cheeseBites + personal)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "2":
            # Jika ukuran pizza yang dipilih adalah regular
            print("Anda telah memilih ukuran Pizza yang Regular")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 16.364? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 16364
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + cheeseBites + regular + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + cheeseBites + regular)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "3":
            # Jika ukuran pizza yang dipilih adalah large
            print("Anda telah memilih ukuran Pizza yang Large")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 19.091? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 19091
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + cheeseBites + large + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + cheeseBites + large)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        else:
            # Menampilkan jika ukuran pizza yang dipilih tidak tersedia
            print("Ukuran Pizza yang Anda pilih tidak tersedia")
    elif pilihanCrust == "5":
        # Jika crust yang dipilih adalah Crown Crust
        print("Anda telah memilih Crown Crust")
        # Menampilkan daftar ukuran pizza beserta harga
        print("Berikut adalah ukuran pizza yang tersedia beserta dengan harganya: ")
        print("+=============================================================+")
        print("| No |       Ukuran Pizza        |           Harga            |")
        print("+=============================================================+")
        print("| 1. | Personal                  |         Rp 0               |")
        print("| 2. | Regular                   |         Rp 65.455          |")
        print("| 3. | Large                     |         Rp 104.545         |")
        print("+=============================================================+")

        # Meminta pelanggan untuk memilih ukuran pizza
        ukuranPizza = str(input("Apa ukuran Pizza yang Anda inginkan: "))
        # Inisialisasi harga ukuran pizza
        personal = 0
        regular = 65455
        large = 104545
        # Memulai proses pemilihan ukuran pizza
        if ukuranPizza == "1":
            # Jika ukuran pizza yang dipilih adalah personal
            print("Anda telah memilih ukuran Pizza yang Personal")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 13.636? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 13636
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + crownCrust + personal + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + crownCrust + personal)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "2":
            # Jika ukuran pizza yang dipilih adalah regular
            print("Anda telah memilih ukuran Pizza yang Regular")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 16.364? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 16364
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + crownCrust + regular + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + crownCrust + regular)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "3":
            # Jika ukuran pizza yang dipilih adalah large
            print("Anda telah memilih ukuran Pizza yang Large")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 19.091? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 19091
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + crownCrust + large + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                 # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + crownCrust + large)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        else:
            # Menampilkan jika ukuran pizza yang dipilih tidak tersedia
            print("Ukuran Pizza yang Anda pilih tidak tersedia")
    else:
        # Menampilkan jika pilihan crust tidak tersedia
        print("Crust yang Anda pilih tidak tersedia, silahkan pilih crust yang tersedia.")
elif toppingPizza == "3":
    print("Anda telah memilih Super Supreme")
    print("====================================")
    # Menampilkan daftar crust yang tersedia beserta dengan harga
    print("Pilihan Crust yang tersedia: ")
    print("+=============================================================+")
    print("| No |      Pilihan Crust        |           Harga            |")
    print("+=============================================================+")
    print("| 1. | Pan                       |         Rp 0               |")
    print("| 2. | StuffedCrust Cheese       |         Rp 11.818          |")
    print("| 3. | StuffedCrust Sausage      |         Rp 9.091           |")
    print("| 4. | Cheese Bites              |         Rp 13.636          |")
    print("| 5. | Crown Crust               |         Rp 11.818          |")
    print("+=============================================================+")

    # Inisialisasi harga crust
    pan = 0
    stuffedCrustCheese = 11818
    stuffedCrustSausage = 9091
    cheeseBites = 13636
    crownCrust = 11818

    # Meminta pelanggan untuk memilih crust
    pilihanCrust = str(input("Silahkan pilih Crust yang Anda inginkan: "))
    # Memulai proses pemilihan crust
    if pilihanCrust == "1":
        # Jika crust yang dipilih adalah Pan
        print("Anda telah memilih Pan")
        # Menampilkan daftar ukuran pizza beserta harga
        print("Berikut adalah ukuran pizza yang tersedia beserta dengan harganya: ")
        print("+=============================================================+")
        print("| No |       Ukuran Pizza        |           Harga            |")
        print("+=============================================================+")
        print("| 1. | Personal                  |         Rp 0               |")
        print("| 2. | Regular                   |         Rp 57.273          |")
        print("| 3. | Large                     |         Rp 89.091          |")
        print("+=============================================================+")

        # Meminta pelanggan untuk memilih ukuran pizza
        ukuranPizza = str(input("Apa ukuran Pizza yang Anda inginkan: "))
        # Inisialisasi harga ukuran pizza
        personal = 0
        regular = 57273
        large = 89091
        # Memulai proses pemilihan ukuran pizza
        if ukuranPizza == "1":
            # Jika ukuran pizza yang dipilih adalah personal
            print("Anda telah memilih ukuran Pizza yang Personal")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 13.636? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 13636
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + pan + personal + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga pizza
                hargaPizza = (hargaTopping + pan + personal)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "2":
            # Jika ukuran pizza yang dipilih adalah regular
            print("Anda telah memilih ukuran Pizza yang Regular")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 16.364? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 16364
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + pan + regular + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + pan + regular)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "3":
            # Jika ukuran pizza yang dipilih adalah large
            print("Anda telah memilih ukuran Pizza yang Large")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 19.091? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 19091
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + pan + large + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + pan + large)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        else:
            # Menampilkan jika ukuran pizza yang dipilih tidak tersedia
            print("Ukuran Pizza yang Anda pilih tidak tersedia")            
    elif pilihanCrust == "2":
        # Jika crust yang dipilih adalah StuffedCrust Cheese
        print("Anda telah memilih StuffedCrust cheese")
        # Menampilkan daftar ukuran pizza beserta harga
        print("Berikut adalah ukuran pizza yang tersedia beserta dengan harganya: ")
        print("+=============================================================+")
        print("| No |       Ukuran Pizza        |           Harga            |")
        print("+=============================================================+")
        print("| 1. | Personal                  |         Rp 0               |")
        print("| 2. | Regular                   |         Rp 65.455          |")
        print("| 3. | Large                     |         Rp 104.545         |")
        print("+=============================================================+")

        # Meminta pelanggan untuk memilih ukuran pizza
        ukuranPizza = str(input("Apa ukuran Pizza yang Anda inginkan: "))
        # Inisialisasi harga ukuran pizza
        personal = 0
        regular = 65455
        large = 104545
        # Memulai proses pemilihan ukuran pizza
        if ukuranPizza == "1":
            # Jika ukuran pizza yang dipilih adalah personal
            print("Anda telah memilih ukuran Pizza yang Personal")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 13.636? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 13636
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustCheese + personal + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustCheese + personal)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "2":
            # Jika ukuran pizza yang dipilih adalah regular
            print("Anda telah memilih ukuran Pizza yang Regular")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 16.364? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 16364
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustCheese + regular + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustCheese + regular)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "3":
            # Jika ukuran pizza yang dipilih adalah large
            print("Anda telah memilih ukuran Pizza yang Large")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 19.091? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 19091
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustCheese + large + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustCheese + large)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        else:
            # Menampilkan jika ukuran pizza yang dipilih tidak tersedia
            print("Ukuran Pizza yang Anda pilih tidak tersedia")            
    elif pilihanCrust == "3":
        # Jika crust yang dipilih adalah StuffedCrust Sausage
        print("Anda telah memilih StuffedCrust Sausage")
        # Menampilkan daftar ukuran pizza beserta harga
        print("Berikut adalah ukuran pizza yang tersedia beserta dengan harganya: ")
        print("+=============================================================+")
        print("| No |       Ukuran Pizza        |           Harga            |")
        print("+=============================================================+")
        print("| 1. | Personal                  |         Rp 0               |")
        print("| 2. | Regular                   |         Rp 64.545          |")
        print("| 3. | Large                     |         Rp 102.727         |")
        print("+=============================================================+")

        # Meminta pelanggan untuk memilih ukuran pizza
        ukuranPizza = str(input("Apa ukuran Pizza yang Anda inginkan: "))
        # Inisialisasi harga ukuran pizza
        personal = 0
        regular = 64455
        large = 102727
        # Memulai proses pemilihan ukuran pizza
        if ukuranPizza == "1":
            # Jika ukuran pizza yang dipilih adalah personal
            print("Anda telah memilih ukuran Pizza yang Personal")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 13.636? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 13636
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustSausage + personal + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustSausage + personal)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "2":
            # Jika ukuran pizza yang dipilih adalah regular
            print("Anda telah memilih ukuran Pizza yang Regular")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 16.364? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 16364
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y 
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustSausage + regular + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                 # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustSausage + regular)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "3":
            # Jika ukuran pizza yang dipilih adalah large
            print("Anda telah memilih ukuran Pizza yang Large")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 19.091? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 19091
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustSausage + large + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustSausage + large)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        else:
            # Menampilkan jika ukuran pizza yang dipilih tidak tersedia
            print("Ukuran Pizza yang Anda pilih tidak tersedia")
    elif pilihanCrust == "4":
        # Jika crust yang dipilih adalah Cheese Bites
        print("Anda telah memilih Cheese Bites")
        # Menampilkan daftar ukuran pizza beserta harga
        print("Berikut adalah ukuran pizza yang tersedia beserta dengan harganya: ")
        print("+=============================================================+")
        print("| No |       Ukuran Pizza        |           Harga            |")
        print("+=============================================================+")
        print("| 1. | Personal                  |         Rp 0               |")
        print("| 2. | Regular                   |         Rp 66.364          |")
        print("| 3. | Large                     |         Rp 107.273         |")
        print("+=============================================================+")

        # Meminta pelanggan untuk memilih ukuran pizza
        ukuranPizza = str(input("Apa ukuran Pizza yang Anda inginkan: "))
        # Inisialisasi harga ukuran pizza
        personal = 0
        regular = 66364
        large = 107273
        # Memulai proses pemilihan ukuran pizza
        if ukuranPizza == "1":
            # Jika ukuran pizza yang dipilih adalah personal
            print("Anda telah memilih ukuran Pizza yang Personal")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 13.636? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 13636
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + cheeseBites + personal + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + cheeseBites + personal)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "2":
            # Jika ukuran pizza yang dipilih adalah regular
            print("Anda telah memilih ukuran Pizza yang Regular")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 16.364? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 16364
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + cheeseBites + regular + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + cheeseBites + regular)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "3":
            # Jika ukuran pizza yang dipilih adalah large
            print("Anda telah memilih ukuran Pizza yang Large")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 19.091? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 19091
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + cheeseBites + large + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + cheeseBites + large)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        else:
            # Menampilkan jika ukuran pizza yang dipilih tidak tersedia
            print("Ukuran Pizza yang Anda pilih tidak tersedia")
    elif pilihanCrust == "5":
        # Jika crust yang dipilih adalah Crown Crust
        print("Anda telah memilih Crown Crust")
        # Menampilkan daftar ukuran pizza beserta harga
        print("Berikut adalah ukuran pizza yang tersedia beserta dengan harganya: ")
        print("+=============================================================+")
        print("| No |       Ukuran Pizza        |           Harga            |")
        print("+=============================================================+")
        print("| 1. | Personal                  |         Rp 0               |")
        print("| 2. | Regular                   |         Rp 65.455          |")
        print("| 3. | Large                     |         Rp 104.545         |")
        print("+=============================================================+")

        # Meminta pelanggan untuk memilih ukuran pizza
        ukuranPizza = str(input("Apa ukuran Pizza yang Anda inginkan: "))
        # Inisialisasi harga ukuran pizza
        personal = 0
        regular = 65455
        large = 104545
        # Memulai proses pemilihan ukuran pizza
        if ukuranPizza == "1":
            # Jika ukuran pizza yang dipilih adalah personal
            print("Anda telah memilih ukuran Pizza yang Personal")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 13.636? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 13636
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + crownCrust + personal + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + crownCrust + personal)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "2":
            # Jika ukuran pizza yang dipilih adalah regular
            print("Anda telah memilih ukuran Pizza yang Regular")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 16.364? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 16364
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + crownCrust + regular + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + crownCrust + regular)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "3":
            # Jika ukuran pizza yang dipilih adalah large
            print("Anda telah memilih ukuran Pizza yang Large")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 19.091? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 19091
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + crownCrust + large + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                 # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + crownCrust + large)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        else:
            # Menampilkan jika ukuran pizza yang dipilih tidak tersedia
            print("Ukuran Pizza yang Anda pilih tidak tersedia")
    else:
        # Menampilkan jika pilihan crust tidak tersedia
        print("Crust yang Anda pilih tidak tersedia, silahkan pilih crust yang tersedia.")
elif toppingPizza == "4":
    print("Anda telah memilih Super Supreme Chicken")
    print("====================================")
    # Menampilkan daftar crust yang tersedia beserta dengan harga
    print("Pilihan Crust yang tersedia: ")
    print("+=============================================================+")
    print("| No |      Pilihan Crust        |           Harga            |")
    print("+=============================================================+")
    print("| 1. | Pan                       |         Rp 0               |")
    print("| 2. | StuffedCrust Cheese       |         Rp 11.818          |")
    print("| 3. | StuffedCrust Sausage      |         Rp 9.091           |")
    print("| 4. | Cheese Bites              |         Rp 13.636          |")
    print("| 5. | Crown Crust               |         Rp 11.818          |")
    print("+=============================================================+")

    # Inisialisasi harga crust
    pan = 0
    stuffedCrustCheese = 11818
    stuffedCrustSausage = 9091
    cheeseBites = 13636
    crownCrust = 11818

    # Meminta pelanggan untuk memilih crust
    pilihanCrust = str(input("Silahkan pilih Crust yang Anda inginkan: "))
    # Memulai proses pemilihan crust
    if pilihanCrust == "1":
        # Jika crust yang dipilih adalah Pan
        print("Anda telah memilih Pan")
        # Menampilkan daftar ukuran pizza beserta harga
        print("Berikut adalah ukuran pizza yang tersedia beserta dengan harganya: ")
        print("+=============================================================+")
        print("| No |       Ukuran Pizza        |           Harga            |")
        print("+=============================================================+")
        print("| 1. | Personal                  |         Rp 0               |")
        print("| 2. | Regular                   |         Rp 57.273          |")
        print("| 3. | Large                     |         Rp 89.091          |")
        print("+=============================================================+")

        # Meminta pelanggan untuk memilih ukuran pizza
        ukuranPizza = str(input("Apa ukuran Pizza yang Anda inginkan: "))
        # Inisialisasi harga ukuran pizza
        personal = 0
        regular = 57273
        large = 89091
        # Memulai proses pemilihan ukuran pizza
        if ukuranPizza == "1":
            # Jika ukuran pizza yang dipilih adalah personal
            print("Anda telah memilih ukuran Pizza yang Personal")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 13.636? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 13636
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + pan + personal + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga pizza
                hargaPizza = (hargaTopping + pan + personal)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "2":
            # Jika ukuran pizza yang dipilih adalah regular
            print("Anda telah memilih ukuran Pizza yang Regular")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 16.364? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 16364
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + pan + regular + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + pan + regular)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "3":
            # Jika ukuran pizza yang dipilih adalah large
            print("Anda telah memilih ukuran Pizza yang Large")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 19.091? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 19091
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + pan + large + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + pan + large)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        else:
            # Menampilkan jika ukuran pizza yang dipilih tidak tersedia
            print("Ukuran Pizza yang Anda pilih tidak tersedia")            
    elif pilihanCrust == "2":
        # Jika crust yang dipilih adalah StuffedCrust Cheese
        print("Anda telah memilih StuffedCrust cheese")
        # Menampilkan daftar ukuran pizza beserta harga
        print("Berikut adalah ukuran pizza yang tersedia beserta dengan harganya: ")
        print("+=============================================================+")
        print("| No |       Ukuran Pizza        |           Harga            |")
        print("+=============================================================+")
        print("| 1. | Personal                  |         Rp 0               |")
        print("| 2. | Regular                   |         Rp 65.455          |")
        print("| 3. | Large                     |         Rp 104.545         |")
        print("+=============================================================+")

        # Meminta pelanggan untuk memilih ukuran pizza
        ukuranPizza = str(input("Apa ukuran Pizza yang Anda inginkan: "))
        # Inisialisasi harga ukuran pizza
        personal = 0
        regular = 65455
        large = 104545
        # Memulai proses pemilihan ukuran pizza
        if ukuranPizza == "1":
            # Jika ukuran pizza yang dipilih adalah personal
            print("Anda telah memilih ukuran Pizza yang Personal")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 13.636? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 13636
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustCheese + personal + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustCheese + personal)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "2":
            # Jika ukuran pizza yang dipilih adalah regular
            print("Anda telah memilih ukuran Pizza yang Regular")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 16.364? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 16364
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustCheese + regular + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustCheese + regular)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "3":
            # Jika ukuran pizza yang dipilih adalah large
            print("Anda telah memilih ukuran Pizza yang Large")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 19.091? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 19091
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustCheese + large + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustCheese + large)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        else:
            # Menampilkan jika ukuran pizza yang dipilih tidak tersedia
            print("Ukuran Pizza yang Anda pilih tidak tersedia")            
    elif pilihanCrust == "3":
        # Jika crust yang dipilih adalah StuffedCrust Sausage
        print("Anda telah memilih StuffedCrust Sausage")
        # Menampilkan daftar ukuran pizza beserta harga
        print("Berikut adalah ukuran pizza yang tersedia beserta dengan harganya: ")
        print("+=============================================================+")
        print("| No |       Ukuran Pizza        |           Harga            |")
        print("+=============================================================+")
        print("| 1. | Personal                  |         Rp 0               |")
        print("| 2. | Regular                   |         Rp 64.545          |")
        print("| 3. | Large                     |         Rp 102.727         |")
        print("+=============================================================+")

        # Meminta pelanggan untuk memilih ukuran pizza
        ukuranPizza = str(input("Apa ukuran Pizza yang Anda inginkan: "))
        # Inisialisasi harga ukuran pizza
        personal = 0
        regular = 64455
        large = 102727
        # Memulai proses pemilihan ukuran pizza
        if ukuranPizza == "1":
            # Jika ukuran pizza yang dipilih adalah personal
            print("Anda telah memilih ukuran Pizza yang Personal")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 13.636? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 13636
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustSausage + personal + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustSausage + personal)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "2":
            # Jika ukuran pizza yang dipilih adalah regular
            print("Anda telah memilih ukuran Pizza yang Regular")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 16.364? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 16364
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y 
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustSausage + regular + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                 # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustSausage + regular)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "3":
            # Jika ukuran pizza yang dipilih adalah large
            print("Anda telah memilih ukuran Pizza yang Large")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 19.091? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 19091
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustSausage + large + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + stuffedCrustSausage + large)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        else:
            # Menampilkan jika ukuran pizza yang dipilih tidak tersedia
            print("Ukuran Pizza yang Anda pilih tidak tersedia")
    elif pilihanCrust == "4":
        # Jika crust yang dipilih adalah Cheese Bites
        print("Anda telah memilih Cheese Bites")
        # Menampilkan daftar ukuran pizza beserta harga
        print("Berikut adalah ukuran pizza yang tersedia beserta dengan harganya: ")
        print("+=============================================================+")
        print("| No |       Ukuran Pizza        |           Harga            |")
        print("+=============================================================+")
        print("| 1. | Personal                  |         Rp 0               |")
        print("| 2. | Regular                   |         Rp 66.364          |")
        print("| 3. | Large                     |         Rp 107.273         |")
        print("+=============================================================+")

        # Meminta pelanggan untuk memilih ukuran pizza
        ukuranPizza = str(input("Apa ukuran Pizza yang Anda inginkan: "))
        # Inisialisasi harga ukuran pizza
        personal = 0
        regular = 66364
        large = 107273
        # Memulai proses pemilihan ukuran pizza
        if ukuranPizza == "1":
            # Jika ukuran pizza yang dipilih adalah personal
            print("Anda telah memilih ukuran Pizza yang Personal")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 13.636? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 13636
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + cheeseBites + personal + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + cheeseBites + personal)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "2":
            # Jika ukuran pizza yang dipilih adalah regular
            print("Anda telah memilih ukuran Pizza yang Regular")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 16.364? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 16364
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + cheeseBites + regular + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + cheeseBites + regular)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "3":
            # Jika ukuran pizza yang dipilih adalah large
            print("Anda telah memilih ukuran Pizza yang Large")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 19.091? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 19091
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + cheeseBites + large + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + cheeseBites + large)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        else:
            # Menampilkan jika ukuran pizza yang dipilih tidak tersedia
            print("Ukuran Pizza yang Anda pilih tidak tersedia")
    elif pilihanCrust == "5":
        # Jika crust yang dipilih adalah Crown Crust
        print("Anda telah memilih Crown Crust")
        # Menampilkan daftar ukuran pizza beserta harga
        print("Berikut adalah ukuran pizza yang tersedia beserta dengan harganya: ")
        print("+=============================================================+")
        print("| No |       Ukuran Pizza        |           Harga            |")
        print("+=============================================================+")
        print("| 1. | Personal                  |         Rp 0               |")
        print("| 2. | Regular                   |         Rp 65.455          |")
        print("| 3. | Large                     |         Rp 104.545         |")
        print("+=============================================================+")

        # Meminta pelanggan untuk memilih ukuran pizza
        ukuranPizza = str(input("Apa ukuran Pizza yang Anda inginkan: "))
        # Inisialisasi harga ukuran pizza
        personal = 0
        regular = 65455
        large = 104545
        # Memulai proses pemilihan ukuran pizza
        if ukuranPizza == "1":
            # Jika ukuran pizza yang dipilih adalah personal
            print("Anda telah memilih ukuran Pizza yang Personal")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 13.636? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 13636
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + crownCrust + personal + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + crownCrust + personal)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "2":
            # Jika ukuran pizza yang dipilih adalah regular
            print("Anda telah memilih ukuran Pizza yang Regular")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 16.364? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 16364
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + crownCrust + regular + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + crownCrust + regular)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        elif ukuranPizza == "3":
            # Jika ukuran pizza yang dipilih adalah large
            print("Anda telah memilih ukuran Pizza yang Large")
            # Meminta pelanggan untuk memilih apakah ingin extra cheese atau tidak
            extraCheese = input("Apakah Anda ingin Extra Cheese dengan menambah uang sebesar Rp 19.091? y/n: ")
            # Inisialisasi harga tambah keju
            tambahKeju = 19091
            # Memulai proses pemilihan extra cheese
            if extraCheese == "y":
                # Jika extra cheese yang dipilih adalah y
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + crownCrust + large + tambahKeju)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
            else:
                # Jika extra cheese yang dipilih adalah n
                print("Jadi, total yang harus Anda bayar yaitu sebesar: ")
                 # Inisialisasi harga  pizza
                hargaPizza = (hargaTopping + crownCrust + large)
                # Menampilkan total harga pizza yang harus dibayar
                print("Rp", hargaPizza)
        else:
            # Menampilkan jika ukuran pizza yang dipilih tidak tersedia
            print("Ukuran Pizza yang Anda pilih tidak tersedia")
    else:
        # Menampilkan jika pilihan crust tidak tersedia
        print("Crust yang Anda pilih tidak tersedia, silahkan pilih crust yang tersedia.")
else:
    # Menampilkan jika menu yang dipilih tidak tersedia
    print("Menu yang anda pilih tidak tersedia / stock kosong")

# Menampilkan ucapan terima kasih telah melakukan pesanan di Pizza Hut
print("Terima kasih telah melakukan pesanan di Pizza Hut, see you next time.")
