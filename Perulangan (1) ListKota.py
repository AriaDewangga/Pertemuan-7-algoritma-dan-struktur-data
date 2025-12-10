list_Kota =[
    'Jakarta','Surabaya','depok','Bekasi','Solo','Jogjakarta','semarang','Makasar'
    ]
for kota in list_Kota:
   print(kota)
else:
    print('Tidak ada lagi item yang tersisa')
    kotaYangDicari=input('ketik nama kota yang kamu cari:')
    for i, kota in enumerate(list_Kota):
        # kita ubah katanya ke lowercase agar
        # menjadi case insensitive
        if kota.lower()==kotaYangDicari.lower():
            print("kota yang anda cari berada pada indeks",i)
            break
        else:
            print('Maaf, kota yang anda cari tidak ada')  
    
