# **************************** LİSTELER ***********************************

# ----Elemana erişmek
# liste[0]

# listem = ['Erkan','Mehmet',25,36.85]
# print(listem)

# ----Eleman eklemek
# liste.append('değer')

# listem = ['Erkan','Ahmet']

# print("Erkan değişmeden önce liste: ",end='')
# print(listem)
#
# listem.append(50)
# listem[1] = 'Mehmet'
#
# print("Erkan değiştikten sonra liste: ",end='')
# print(listem)

# ----Belirtilen bir indexe eleman eklemek
# liste.insert(2,'değer')

# listem = ['Ece','Mustafa']
#
# listem.insert(1,'Kamil')
# print(listem)

# ----Listeden eleman silmek
# liste.remove('eleman')
# liste.pop()
# liste.clear()
# del liste

# listem = [68,'Selim','Hasan']
# print(listem)
# listem.remove('Hasan')
# print(listem)
# listem = [68,'Selim','Hasan','Erkan']
# print(listem)
# listem.clear()
# print(listem)
# listem.pop(2)
# print(listem)

# listem = [68,'Selim','Hasan','Erkan']
# del listem
# print(listem)


# ----Listeleri birleştirmek
# liste1 = liste1 + liste2
# liste1.extend(liste2)

# liste1 = [1]
# liste2 = [2]
# print("birleşmeden once liste 1: ",end='')
# print(liste1)
# liste1.extend(liste2)
# print("birleşmeden sonra liste 1: ",end='')
# print(liste1)

# ----Liste kopyalamak
# liste = liste2.copy()

# listem2 = [3,4]
# listem5 = listem2.copy()
# print(listem5)

# ----Liste elemanlarını sıralamak
# liste.sort()
# liste = ['z','c','a']
# liste.sort()
# print(liste)


# ----Belirli bir elemanın liste içerisindeki sayısını bulmak
# liste.count('a')
# len(liste)

# listem = ['Ahmet','Mehmet','Ahmet',5,8]
# print(listem.count('Mehmet'))
# print(len(listem))




# **************************** SÖZLÜK ***********************************

# ----Elemana erişmek
# sozluk['key']

# sozluk = {'adres' : 'Örnek adres','liste' : ['A','B']}
# print(sozluk['liste'][1])

# ----Sozluğe eleman eklemek
# sozluk['key'] = 'new value' ** Eğer zaten key değeri sozlukte varsa, mevcut değerinin üzerine yazar **
# sozluk = {'key1' : 'Ahmet', 'key2' : 'Mehmet'}
# print(sozluk)
# sozluk['key3'] = 'new value'
# print(sozluk)


# ----Sozlukleri birleştirmek
# soz1.update(soz2)
# sozluk1 = {'key1' : 'Ahmet', 'key2' : 'Mehmet'}
# sozluk2 = {'key3' : 'Halil', 'key4' : 'Kemal'}
# sozluk1.update(sozluk2)
# print(sozluk1)


# ----Anahtarlara erişmek
# sozluk.keys()
# sozluk1 = {'key1' : 'Ahmet', 'key2' : 'Mehmet'}
# print(sozluk1.keys())

# ----Değerlere erişmek
# sozluk.values()
# sozluk1 = {'key1' : 'Ahmet', 'key2' : 'Mehmet'}
# print(sozluk1.values())

# ---- Sozlukten eleman silmek
# sozluk.pop('key')
# sozluk.popitem() **son elemanı siler **
sozluk1 = {'key1' : 'Ahmet', 'key2' : 'Mehmet'}
# print(sozluk1)
# sozluk1.pop('key2')
# print(sozluk1)
# print(sozluk1)
# sozluk1.popitem()
# print(sozluk1)
# ----Sozluk içini tamamen silmek
# sozluk.clear()
# sozluk1.clear()
# print(sozluk1)




# **************************** DEMETLER ***********************************

# ----Tek elemanlı demet oluşturmak
# demet = ('value', )
# demet = ('değerim','değerim2')
# print(demet[0])

# ----Elemana erişmek
# demet[0]
# demet = ('değerim','değerim2')
# print(demet[0])

# ----tuple() fonksiyonunu kullanarak demet oluşturmak
# demet = tuple(('value1','value2'))

# ----Demet içerisinde arama yapmak
# if 'aranan değer' in demet:
    # bloğa girerse değer var demektir.

# demet = ('değerim','değerim2')
# if 'değerim3' in demet:
#     print("evet var")

# ----Belirli bir elemanın index numarasına erişmek
# demet.index('value')
# demet = ('değerim','değerim2')
# print(demet.index('değerim'))

# ----Belirli bir elemandan kaç adet olduğunu bulmak
#demet.count('value')
# demet = ('değerim','değerim2','değerim2','değerim2')
# print(demet.count('değerim'))


# **************************** KÜMELER ***********************************

# kume = {'Python','Flutter','Flutter'}
# print(kume)

# ----Kümeye eleman eklemek
# kume.add('value')
# kume = {'Python','Flutter'}
# kume.add('Dart')
# print(kume)

# ----Tek seferde birden fazla eleman eklemek
# kume = {'Python','Flutter'}
# kume.update(['v1','v2'])
# print(kume)

# ----Kümeden eleman silmek
# kume = {'Python','Flutter'}
# kume.pop()
# #kume.pop() #** en sondaki elemanı sile **
# print(kume)

# ----Küme içerisini tamamen temizlemek
# kume = {'Python','Flutter'}
# kume.clear()
# print(kume)

# ---Küme kopyalamak
# yenikume = kume.copy()
# kume = {'Python','Flutter'}
# yenikume = kume.copy()
# print(yenikume)

# ----İki farklı kümeyi birleştirmek
# kume1 = {'Python','Flutter'}
# kume2 = {'C++','C#'}
# kume3 = kume1.union(kume2)
# print(kume3)

# ---Küme elemanları üzerinde gezinmek
# for i in kume:
    # print(i)

# ----Belirli bir elemanın kümede olup olmadığını kontrol etmek
# 'aranan değer' in kume













