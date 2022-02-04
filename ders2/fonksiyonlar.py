# FONKSİYON TANIMLAMAK VE ÇAĞIRMAK
'''
# fonk adında fonksiyonumuzu tanımlıyoruz.
def fonk():
    print("İlk fonksiyonum")

# fonk adındaki fonksiyonumuzu çağırıyoruz.
fonk()
'''

# ----------------------------------------------------------------------------------------
# FONKSİYONA PARAMETRE GÖNDERMEK
'''
def fonk(name):
    print("Merhaba "+name)

fonk('Erkan')
'''

# ----------------------------------------------------------------------------------------
# FONKSİYONLAR İLE GERİYE DEĞER DÖNDÜRMEK
'''
def fonk(sayi1,sayi2):
    toplam = sayi1 + sayi2

    return toplam
gelen_sonuc = fonk(5,6)
print(gelen_sonuc)
'''

# ----------------------------------------------------------------------------------------
# FONKSİYON İÇERİSİNDE FONKSİYON ÇAĞIRMAK
'''
def fonk1(dogum_yili):
    print("Birinci Fonksiyon Çalıştı")
    return 2022 - dogum_yili


def fonk2(dogum_yili):
    gelen_dogum_yili = dogum_yili
    yas = fonk1(gelen_dogum_yili)

    return yas

ahmet = fonk2(1997)
mehmet = fonk2(1985)
print("Ahmtein yaşı: "+str(ahmet))
print("Mehmetin yaşı: "+str(mehmet))
'''




