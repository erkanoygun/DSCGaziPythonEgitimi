# MODÜLLER
import math
import random
import datetime
import os

# math MODÜLÜ

# -------------------------------------------------------------------------------------------------
# sayi = 35.06
# yuvarlanmis_sayi = math.ceil(sayi) # Verilen ondalık sayıyı bir üst sayıya çevirir.
# print(yuvarlanmis_sayi)
# -------------------------------------------------------------------------------------------------
# sayi = -35
# mutlak_sayi = math.fabs(sayi) # Verilen sayının mutlak değerini alır.
# print(mutlak_sayi)
# -------------------------------------------------------------------------------------------------
# sayi = 4
# faktoriyel = math.factorial(sayi) # Verilen sayının faktöriyelini verir.
# print(faktoriyel)
# -------------------------------------------------------------------------------------------------
# sayi = 21.65
# yuvarlanmis_sayi = math.floor(sayi) # Verilen ondalık sayıyı bir altındaki tam sayıya döndürür.
# print(yuvarlanmis_sayi)
# -------------------------------------------------------------------------------------------------
# sayi1 = 45
# sayi2 = 70
# ebob = math.gcd(sayi1,sayi2) # Verilen iki sayının EBOBU nu veriyor.
# print(ebob)
# -------------------------------------------------------------------------------------------------
# sayi = 16
# karekok = math.sqrt(sayi) # Verilen sayının karekökünü hesaplar.
# print(karekok)
# -------------------------------------------------------------------------------------------------
# sayi = 16
# log2 = math.log2(sayi) # Verilen sayının 2 tabanında logaritmasını hesaplar.
# print(log2)
# -------------------------------------------------------------------------------------------------
# sayi = 100
# log10 = math.log10(sayi) # Verilen sayının 10 tabanında logaritmasını hesaplar.
# print(log10)

# print(dir(math))
# -------------------------------------------------------------------------------------------------

# random MODÜLÜ
# sayi = random.randint(0,10) # Min ve max aralığında integer olan bir sayı döner.
# print(sayi)
# -------------------------------------------------------------------------------------------------
# liste = ['Ahmet','Mehmet','Ece','Hüseyin','Ayşe']
# secilen = random.choice(liste) # Liste içerisinden rastgele bir değer seçer
# print(secilen)
# -------------------------------------------------------------------------------------------------

# datatime MODÜLÜ
# suan = datetime.datetime.now() # Şuanki zamanı verir
# print(suan.month)
# print(suan.year)
# print(suan.day)
# print(suan.hour)
# print(suan.minute)

# os MODÜLÜ

# print(os.getcwd()) # içinde bulunulan dizini verir
# mevcut_dizin = os.getcwd()
# print(os.listdir(mevcut_dizin)) # Bulunduğumuz dizindeki dosyaların adını verir
# os.mkdir('denemeeee.txt') # Bulunulan klasör içerisine klasör oluşturur.
# os.rmdir('deneme') # Adı verilen klasörü siler.
# print(os.path.exists("deneme.txt")) # Adı verilen dosyanın bulunup bulunmadığını kontrol eder.





























