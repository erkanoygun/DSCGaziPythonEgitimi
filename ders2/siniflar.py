# NESNE YÖNELİMLİ PROGRAMLAMA
'''
*Nesne yönelimli programlama bir çok farklı yazılım geliştirme yöntemlerinden birisidir
*Nesne yönelimli programlamayı kulanmak hiç bir zaman zorunlu tutulmaz.
*Nesne yönelimli programlamayı kullanmadanda bir çok faydalı yazılım geliştirebilirsiniz
*Nesne yönelimli programlamanın en temel ve kısa tabiriyle amacı çok fazla işi olabil-
diğince az kod yazarak yapmaya dayanır.
*Örneğin UI yani kullanıcı arayüzlü bir program geliştirecekseniz nesne yönelimli
programlamadan yararlanmalısınız aksi taktirde yazacağınız kod miktarı hem çok daha
fazla artacaktır hemde kodlarınızın okunurulluğu çok kötü hale gelecektir.
'''

# SINIFLAR
'''
*Nesne yönelimli programlamanın temelinde sınıf diye adlandırılan (class) bir
kavram vardır.
*En kaba ve basit tabiriyle sınıflar nesne üretmemizi sağlayan veri tipleridir.
*Sınıflar string, integer, list... gibi verileri değiştirmemizi manüpile etmemizi
sağlayan veri tipleridir.
'''

# ----------------------------------------------------------------------------------------------------
# SINIF TANIMLAMAK
'''
class MyClas():
    # Sınıf gövdesine tanımladığımız Erkan ve 542145 değerini atadığımız name ve no adlı değişkenler
    # birer sınıf niteliğidir (class attribute)
    name = 'Erkan'
    no = 542145
# SINIF YENİ DEĞER ATAMAK
MyClas.surname = 'Oygun'

# SINIF DEĞERİNE ERİŞMEK
print(MyClas.name)
# NOT: Doğrudan sınıf adını kullanarak öğelere eriştiğimizde kodlarımız tek kullanımlık olmuş olur!
'''
# ----------------------------------------------------------------------------------------------------
# SINIFLARDAN NESNE OLUŞTURMAK (ÖRNEKLEMEK)
'''
class MyClas():
    username = 'Erkan'
    surname = 'Oygun'

erkan = MyClas()
print(erkan.surname)
'''
# ----------------------------------------------------------------------------------------------------

# SINIF OBJESİ OLUŞTURURKEN OBJENİN NE TİP ÖZELLİKLERİNİN OLACAĞINI BELİRLEYİP ÖZELLİKLERİ TANIMLAMAK
'''
class MyClas():
    # Örnek niteliği tanımlarken  __init__() fonksiyonunu ve self araçlarını kullanacağız.
    def __init__(self,nickname):
        # Bu kısımda name adlı değişkene obje oluşturulurken verilen değerin atanmasını sağlıyoruz.
        self.nickname = nickname

# user1 adlı obje oluşturulurken erkan11 değeri parametre olarak veriliyor.
# obje oluşturulduğu anda __init__() fonksiyonu tetiklenir.
user1 = MyClas('erkan11')
# NOT: self kelimesi Python programlama dilinin söz diziminin gerektirdiği bir öğedir!
'''

# ----------------------------------------------------------------------------------------------------

# SINIF İÇERİSİNDE METOD OLUŞTURMAK
'''
class MyClas():
    def __init__(self,ogrenci_name,ogrenci_surname,ogrenci_no,not1,not2):
        self.ogrenci_name = ogrenci_name
        self.ogrenci_surname = ogrenci_surname
        self.ogrenci_no = ogrenci_no
        self.not1 = not1
        self.not2 = not2
        
    # Bir fonksiyon sınıf içerisinde tanımlanması durumunda metod olur.
    def ogrenciBilgi(self):
        return "{} adlı öğrenci {} değrinde numaraya sahiptir".format(self.ogrenci_name,self.ogrenci_no)

    def notOrtalamaHesapla(self):
        toplam = self.not1 + self.not2
        sonuc = toplam / 2
        return sonuc

    def notGuncelle(self,yeni_not=50):
        self.not1 = yeni_not

ogrenci1 = MyClas('Ahmet','Yılmaz',3214521,85,90)
bilgi = ogrenci1.ogrenciBilgi()
#print(bilgi)

ogrenci2 = MyClas('Mustafa','Kara',562311,70,100)
gelen_sonuc = ogrenci2.notOrtalamaHesapla()
#print(gelen_sonuc)

ogrenci3 = MyClas('Hasan','Eldiz',9854124,25,60)
print("Güncellenmeden önceki not 1: "+str(ogrenci3.not1))
ogrenci3.notGuncelle(80)
print("Güncellendikten sonraki not 1: "+str(ogrenci3.not1))
'''
# ----------------------------------------------------------------------------------------------------

# @classmethod BEZEYECİSİ ve cls
# Örnek metodlara sınıf adlarıyla erişmemiz mümkün değildir bir örnek metoda erişmek istiyorsak
# örnek metodun bulunduğu sınıftan bir nesne oluşturmalı ve o nesne aracılığıyla metoda erişilmelidir.
# @classmethod bezeyicisi ile tanımlanan bir örnek metoda doğrudan sınıf adı üzerinden erişebiliriz
'''
class MyClas():
    ogrenci = []
    def __init__(self,name,username):
        self.name = name
        self.username = username

    def ogrenciEkle(self):
        self.ogrenci.append([self.name,self.username])

    def eklenenOgrenci(self):
        print(self.ogrenci)
        return self.ogrenci

    @classmethod
    def nesneSayisi(cls):
        print(len(cls.ogrenci))

# ogrenci = MyClas('Erkan','Oygun')
# ogrenci.ogrenciEkle()
# ogrenci2 = MyClas('Ahmet','Yılmaz')
# ogrenci2.ogrenciEkle()
# ogrenci2.eklenenOgrenci()

# MyClas.nesneSayisi()
'''
# ----------------------------------------------------------------------------------------------------

# SINIFLARDA KALITIM (INHERITANCE)
'''
class User():
    def __init__(self,name,surname,phone_no):
        print("User sınıfının init metodu tetiklendi")
        self.name = name
        self.surname = surname
        self.phone_no = phone_no

    def userInfo(self):
        print(f'Kullanıcının adı: {self.name}\nKullanıcının soyadı: '
              f'{self.surname}\nKullanıcının Telefen Numarası: {self.phone_no}')


class Teacher(User):
    def __init__(self,name,surname,phone_no,e_mail):
        # print("Teacher sınıfının init metodu tetiklendi")
        # super() fonksiyonu ile name,surname,phone_no özelliklerini tekrar oluşturmayıp-
        # üst sınıftan miras aldık
        super().__init__(name,surname,phone_no)
        self.e_mail = e_mail
        self.lessons = ['maths','biology','physics']

    def lessonsGiven(self):
        counter = 1
        for i in self.lessons:
            print('Verilen Ders: '+i)
            counter += 1


class Student(User):
    def __init__(self,name,surname,phone_no,scholl_no,note_average):
        #print("Student sınıfının init metodu tetiklendi")
        super().__init__(name,surname,phone_no)
        self.scholl_no = scholl_no
        self.note_average = note_average
        self.lessons = ['maths','Literature','Electronics']

    def lessonsLearned(self):
        counter = 1
        for i in self.lessons:
            print(f'Alınan Ders {counter}: '+i)
            counter += 1

#teacher1 = Teacher('Hasan','Yılmaz',55543251,'example@gg.com')
#print(teacher1.name)
student1 = Student('Mustafa', 'Kara', 54552147, 9987456, 87.6)
#print(student1.note_average)

#student1.lessonsLearned() # Kullanıcının aldığı dersleri listeleyelim
#student1.userInfo() # Kullanıcıya ait bilgileri üst sınıfta tanımlı metoda erişerek alalım
'''
# ----------------------------------------------------------------------------------------------------





