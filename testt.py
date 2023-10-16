from prettytable import PrettyTable

pilihrasa = PrettyTable(["Angka", "Rasa", "Harga"])

pilihrasa.add_row(["0", "chocolate", "10000" ])
pilihrasa.add_row(["1", "vanilla", "10000" ])
pilihrasa.add_row(["2", "strawberry", "12000" ])
pilihrasa.add_row(["3", "mango", "12000" ])
pilihrasa.add_row(["4", "watermelon", "12000" ])
pilihrasa.add_row(["5", "melon", "12000" ])
pilihrasa.add_row(["6", "cotton candy", "15000" ])
pilihrasa.add_row(["7", "oreo", "15000"])
pilihrasa.add_row(["8", "milo", "15000"])

print('1. pembeli')
print('2. admin')
role = int(input('anda pembeli atau admin:'))
if role == 1:
    print(pilihrasa)
    pesan = int(input("pilih menu yang anda inginkan:"))
    if pesan == 0:
        a = int(input('berapa piece yang anda inginkan:'))
        print('anda memesan ice cream rasa chocolate sebanyak', a)
        b = 10000*a
        print('jumlah harga pesanan anda', b)
        print('terimakasih sudah berbelanja disini')
    elif pesan == 1:
        a = int(input('berapa piece yang anda inginkan:'))
        print('anda memesan ice cream rasa vanilla sebanyak', a)
        b = 10000*a
        print('jumlah hasil pesanan anda', b)
        print('terimakasih sudah berbelanja disini')
    elif pesan == 2:
        a = int(input('berapa piece yang anda inginkan:'))
        print('anda memesan ice cream rasa strawberry sebanyak', a)
        b = 12000*a
        print('jumlah hasil pesanan anda', b)
        print('terimakasih sudah berbelanja disini')
    elif pesan == 3:
        a = int(input('berapa piece yang anda inginkan:'))
        print('anda memesan ice cream rasa mango sebanyak', a)
        b = 12000*a
        print('jumlah hasil pesanan anda', b)
        print('terimakasih sudah berbelanja disini')
    elif pesan == 4:
        a = int(input('berapa piece yang anda inginkan:'))
        print('anda memesan ice cream rasa watermelon sebanyak', a)
        b = 12000*a
        print('jumlah hasil pesanan anda', b)
        print('terimakasih sudah berbelanja disini')
    elif pesan == 5:
        a = int(input('berapa piece yang anda inginkan:'))
        print('anda memesan ice cream rasa melon sebanyak', a)
        b = 12000*a
        print('jumlah hasil pesanan anda', b)
        print('terimakasih sudah berbelanja disini')
    elif pesan == 6:
        a = int(input('berapa piece yang anda inginkan:'))
        print('anda memesan ice cream rasa cotton candy sebanyak', a)
        b = 15000*a
        print('jumlah hasil pesanan anda', b)
        print('terimakasih sudah berbelanja disini')
    elif pesan == 7:
        a = int(input('berapa piece yang anda inginkan:'))
        print('anda memesan ice cream rasa oreo sebanyak', a)
        b = 15000*a
        print('jumlah hasil pesanan anda', b)
        print('terimakasih sudah berbelanja disini')
    elif pesan == 8:
        a = int(input('berapa piece yang anda inginkan:'))
        print('anda memesan ice cream rasa milo sebanyak', a)
        b = 15000*a
        print('jumlah hasil pesanan anda', b)
        print('terimakasih sudah berbelanja disini')
    else:
        print('maaf, tidak ada di menu')
elif role == 2:
    print(pilihrasa)
    print('1. menambah menu')
    print('2. mengubah menu')
    print('3. menghapus menu')
    print()
    fitur = int(input('fitur berapa yang ingin anda lakukan:'))
    if fitur == 1:
        menu_baru = str(input('menu apa yang ingin anda tambahkan:'))
        harga_menu = int(input('berapa harga menu tersebut:'))
        nomor_menu = int(input('menu tersebut menjadi data ke berapa:'))
        pilihrasa.add_row([nomor_menu, menu_baru, harga_menu])
        print(pilihrasa)
        
    elif fitur == 2:
        nomor_menu = int(input('menu apa yang ingin anda ubah:'))
        pilihrasa.del_row(nomor_menu)
        menu_baru = (input('menu baru:'))
        harga_menu = int(input('harga menu baru:'))
        pilihrasa.add_row([nomor_menu, menu_baru, harga_menu])
        print(pilihrasa)
        
    elif fitur == 3:
        hapus_menu = int(input('pilih menu yang ingin anda hapus:'))
        pilihrasa.del_row(hapus_menu)
        print(pilihrasa)
    else:
        print('maaf, pilihan tidak ada di menu')
else:
    print('maaf, pilihan tidak ada di menu')