# WHILE DONGUSU
'''
While döngüsü, koşul gerçekleştiği sürece çalışan bir döngü çeşididir. Genellikle döngünün kaç defa
çalışacağı belirli değilse while döngüsü tercih edilir. Ancak koşullar verilerek de while döngüsünün
belirli sayıda çalışması sağlanabilir. Döngülerde koşullu ifadelerde olduğu gibi blok yapısı
kullanılmaktadır. while ifadesinden sonra koşul durumu yazılır, ardından iki nokta işareti konularak
alt satıra geçilir. Koşul durumu sağlandığı sürece çalışacak kodlar bir blok içeriden çalışır.
'''

# Sonsuz döngü oluşturmak
# while True:
#     print("Dongü Çalışıyor")

# Koşula bağlı döngü tanımlamak
# a = 0
# while a <= 5:
#     a += 1
#     print(a)

# Şart ile döngüyü kırmak (bitirmek).
# a = 0
# while True:
#     a += 1
#     if a == 5:
#         print(f"Döngü kırıldı a değeri: {a}")
#         break

# İçiçe while döngüsü tanımlamak
# i = 1
# while i <= 3:
#     print(f'\nİ\'nin değeri: {i}\n')
#     j = 0
#     while j < 5:
#         print(f'J\'nin değeri: {j}')
#         j += 1
#     print('------------------------')
#     i += 1

# Ornek
# while True:
#     islem = int(input("Yapmak istediğin işlem (1-Topla / 2-Çıkar / 3-Çıkış): "))
#     if islem == 1:
#         sayi1 = int(input("Birinci sayıyı giriniz: "))
#         sayi2 = int(input("İkinci sayıyı giriniz: "))
#         sonuc = sayi1 + sayi2
#         print(f'Sonuç = {sonuc}')
#     elif islem == 2:
#         sayi1 = int(input("Birinci sayıyı giriniz: "))
#         sayi2 = int(input("İkinci sayıyı giriniz: "))
#         sonuc = sayi1 - sayi2
#         print(f'Sonuç = {sonuc}')
#     elif islem == 3:
#         print("Çıkış Yapılıyor")
#         break
#     else:
#         print("Çıkış Yapılıyor")
#         break







# FOR DÖNGÜSÜ

'''
For döngüsü, Python’da genellikle döngünün tekrar sayısı programcı tarafından
belirlenmiş veya öngörülmüş ise kullanılır.
For döngüsü daha çok belirli sayıdaki işlemi gerçekleştirmek için kullanılır. Bunun
yanında Python’da for döngüsünün iterasyon denilen önemli bir özelliği
bulunmaktadır. İterasyon işlemi sayesinde karakter dizileri ve listeler üzerinde
gezinme işlemi, yani ilk elemandan son elemana kadar işlem yapabilmektedir. For
döngüsü kullanmak için “in” işlecinden faydalanmak gerekmektedir. 
'''

# For döngüsü tanımlamak
# for i in range(0,5):
#     print(i)


# For döngüsü ile liste elemanları üzerinde gezinmek
# listem = ['Erkan','Ahmet','Selin','Ayşe','Hasan']
# for i in listem:
#     print(i)


# İçiçe for döngüsü
# listem1 = ['Erkan','Ahmet','Mustafa','Ayhan','Hasan']
# listem2 = ['Kamil','Ahmet','Selin','Ayşe','Ali']
# listem3 = ['Ece','Ahmet','Erkan']
# listeler = [listem1,listem2,listem3]
# for i in range(0,3):
#     for j in listeler[i]:
#         if j == 'Erkan':
#             print(f'{i+1}. liste içerisinde Erkan var')


# Continue ifadesinin kullanımı
# for i in range(0,6):
#     if i == 2:
#         continue
#     print(i)


















