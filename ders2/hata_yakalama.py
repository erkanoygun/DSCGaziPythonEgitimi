# HATA YAKALAMA
'''
Beklenmedik durumlarda programın bir hata mesajı vermesi ve çalışmayı
durdurması yerine, hataya kullanıcının istediği şekilde cevap vermesini
sağlamanın bir yolu olarak adlandırılmaktadır.
Hata yakalama Python programlama dilinin önemli bir parçasıdır ve kaynak
kodunu çok karışık hâle getirmeden programınızın güvenilir bir şekilde
çalışmasını sağlar.
'''

# Olası herhangi bir hatayı yakalamak
'''
try:
    sayi = int(input('Bir sayı giriniz: '))
    sayi = sayi + 2
    print(f'Sonuç= {sayi}')
except:
    print("Hata meydana geldi")
'''

# Hata meydana gelmiş olmasına rağmen kodlar kaldığı yerden çalışmaya devam eder...
'''
try:
    sayi = int(input('Bir sayı giriniz: '))
    sayi = sayi + 2
    print(f'Sonuç= {sayi}')
except:
    print("Hata meydana geldi")

print("Bu kısım çalıştırıldı")
'''

# Hatayı tipine göre yakalamak
'''
# Ornek 1
s1 = int(input("Birinci Sayı :"))
s2 = int(input("İkinci Sayı :"))
try:
    sonuc = s1/s2
    print("Sonuc :",sonuc)
except ZeroDivisionError:
    print("Bir sayıyı sıfıra bölemezsiniz lütfen sıfır dışında bir sayı girin")
'''
# Ornek 2
'''
try:
    s1 = int(input("Birinci Sayı :"))
    s2 = int(input("İkinci Sayı :"))
    sonuc = s1/s2
    print("Sonuc :",sonuc)
except ZeroDivisionError:
    print("Bir sayıyı sıfıra bölemezsiniz lütfen sıfır dışında bir sayı girin")
except ValueError:
    print('Lütfen sayısal bir karakter girin..')
except:
    print("Beklenmeyen bir hata oluştu")
'''

# Kullanıcıya pythonun göndediği hata mesajını göstermek
'''
try:
    print("Ali" + 2)
except Exception as e:
    print(f"Hata meydana geldi hata türü: {e}")
'''

# Hata meydana gelsede gelmesede mutlaka çalışmasını istediğimiz kodları tanımlamak
'''
try:
    s1 = int(input("Değer Girin: "))
except:
    print("Hata meydana geldi")
finally:
    print("Bu kısım çalıştı")
'''
















