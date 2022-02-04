# DOSYA OKUMA İŞLEMLERİ

# Dosya açma kipleri
'''

dosya = open("deneme.txt","r")

* 'r' modu: Dosyayı sadece okumak için açar. Bu mod varsayılan moddur.

* 'r+' modu: Dosyayı hem okumak hem de yazmak için açar. Eğer çağrılan dosya bulunamadıysa
yeni bir dosya oluşturulmaz.

* 'w' modu: Dosyayı sadece yazmak için açar. Varolan dosyanın üzerine yazma işlemini yapar.
Eğer çağrılan dosya bulunamadıysa yeni bir dosya oluşturur.

* 'a' modu: Dosyayı ekleme işlemi için açar. Eğer çağrılan dosya bulunursa, en sonundan eklemeye devam eder.
Eğer dosya yoksa sadece yazma işlemi yapacak yeni bir dosya oluşturur.

* 'a+' modu: Dosyayı hem ekleme hem de okuma işlemi için açar. Eğer çağrılan dosya bulunursa
en sonundan eklemeye devam eder. Eğer dosya yoksa yazma ve okuma işlemleri yapacak yeni bir dosya oluşturur.
'''

# Basit dosya açıp okuma örneği
'''
dosya=open("deneme.txt","r")
okunan = dosya.read()
print(okunan)
dosya.close() # açılan dosyayı kapatıyoruz
'''
'''
# Dosya açıp okuma örneği 2
with open("deneme.txt","r") as dosya:
    okunan = dosya.read()
    print(okunan)
'''

# Dosyayı hem okumak hem yazmak
'''
with open("deneme.txt","r+") as dosya:
    #dosya.write ("dosyaya yazıldı")
    print(dosya.read())
'''

# Dosyaya yazma işlemi (w)
'''
with open("deneme.txt","w") as dosya:
    dosya.write("dosya silinip yeniden yazildi")
'''

# Varolan dosyada satır sonuna ekleme işlemi (a)
'''
with open("deneme.txt","a") as dosya:
    dosya.write("dosya sonuna eklendi")
'''

# Ornek
'''
with open('deneme.txt', 'a',encoding='utf-8') as dosya:
    for i in range(0,3):
        dosya.write(f'Satır {i+1}\n')
'''

# Ornek 2 (dosyaya dizin yolundan erişmek)
'''
with open("veriler\\veri.txt","r") as dosya:
    print(dosya.read())
'''















