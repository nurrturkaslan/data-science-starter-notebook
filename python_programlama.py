#SAYILAR VE STRİNGLERE GİRİŞ
9 #integer
9.2 #float
#ikiside sayısal değişkendir. integer kesikli float süreklidir.
9+9
9*9
#python da oluşturduğumuz her şey bir nesnedir.

print("HELLO AI ERA")
'HELLO AI ERA'
#içerisine girdiğimiz ifadeyi console ekranına yazdırıyor.


type(9)
type(9.2)
type("HELLO AI ERA")
#içerisine girilen nesnenin bize tip bilgisini veriyor.



#STRİNGLERE YAKINDAN BAKALIM
""
''
123
type(123)
"123"
type("123") #tırnak işareti koyarak yazdığımızda python bunu string olarak görüyor.

"a"+"b" #iki ifadeyi bir araya getirmek için + kullanıyoruz
"a" "b" #yine bir araya getiriyor
"a" " b" #aralarına boşluk koymak istiyorsam harften önce koyulur.
"a" + "-b" # - ifadesi ile birleştirme fakat aradaki + yerine - koyamayız.

"a"*3 #3tane a ifadesini yanyana getiriyor.
"a"/3 #tip hatası verir böyle bir kullanım yok bölme ve çıkarma yok!


#STRİNG METODLAR-len
#UZUNLUK BİLGİSİNE ERİŞMEK: len METODU
gel_yaz = "gelecegi_yazanlar" #sağ tarftaki işlem eşittir sol taraftaki işlem dediğimizde atama işlemi gerçekleştiririz.
#del nur
a = 9
b = 10

a*b

len(gel_yaz) #uzunluğunu söylüyor 17 karakterden oluşuyormuş geleceği_yazanlar
len("gelecegi_yazanlar")



#BÜYÜK/KÜÇÜK HARF DÖNÜŞÜMLERİ
#UPPER&LOWER METODLARI
gel_yaz = ("gelecegi_yazanlar")
gel_yaz.upper() #büyük harflere çevirir
gel_yaz.lower() #küçük harflere çevirir

gel_yaz.islower() #zaten geleceği yazanlar ifadesinin hepsi küçük olduğunundan true yazdı
B = gel_yaz.upper()

B.islower() #küçük değil
B.isupper() # evet büyük



#KARAKTER DEĞİŞTİRME 
#REPLACE METODU
#elimizdeki stringlerin içerisindeki karakterlerde değişik yapmak istediğimşzde kullanılır.
gel_yaz = "gelecegi_yazanlar"
gel_yaz.replace("e","a")
gel_yaz.replace("a","i")



#KARAKTER KIRPMA İŞLEMİ
#STRİP METODU
#istenmeyen karakterleri kırpmak için kullanılır.

gel_yaz = " gelecegi_yazanlar "
gel_yaz.strip()

gel_yaz = "lgelecegi_yazanlarl"
#gel_yaz.strip()
#fonksiyonun ön tanımlı dğerlere göre işleme soktu
#gel_yaz.strip("*") #yıldızı siliyor
gel_yaz.strip("l")



#METODLARA GENEL BAKIŞ
gel_yaz = "gelecegi_yazanlar"
dir(gel_yaz)
#elimizdeki veri tipinin üzerine uygulanabilecek metodlara gitmektedir.

gel_yaz.capitalize() #ilk baş harf büyüyor
gel_yaz.title() # baş harferi büyütüyor



#KARAKTER DİZİLERİNDE ALT KÜME İŞLEMLERİ
#SUBSTRİNG İŞLEMLERİ

gel_yaz = "gelecegi_yazanlar"
gel_yaz[1]
#python köşeli parantez yaptığımızda bir seçim işlemi gerçekleştireceğimizi anlar.
#seçim işlemlerini yapabilmek adına indexlerden yararlanıyoruz
#index: string ifadenindeğerlerine erişmek istediğimiz oradaki değerleri ifade ediyor.
#0 hep balangıç noktası
gel_yaz[16]
gel_yaz[0:3]
# : soldan sağdaki ifadeye kadar seçim yap demek
gel_yaz[3:7]



#DEĞİŞKENLER
a = 9
b = "ali_uzaya_git"
#atama işemleri üzerinden farklı işlemler gerçekleştirebiliyoruz.
c = a*2

a/c
a*c 
a*5

type(100)
type(100.2)
type(1+2j) #complexbirinci_sayi = input()


a = 100.2



#TYPE_DÖNÜŞÜMLERİ


#input kullanıcıdan bilgi almak için kullanılır
toplama_bir = input()
toplama_iki = input()

type(toplama_bir)
toplama_bir + toplama_iki
#iki ifadeyi string anlamda birleştirdi

int(toplama_bir) + int(toplama_iki)
#matematiksel anlamda toplama işlemini int ile yaptı

#ondalıklı değişkeni integera çevirme

11.0
int(11.0)

12
float(12)

type(str(12))
#str(12) #etrafına tırnak atarak strin yapıyor çıktıda




#print()

print("HELLO AI ERA")

print("GELECEGİ","YAZANLAR",sep="_")
#sep geleceği yazanlar ifadesini alttre ile birleştirmiş oldu
#fonk genel amaçlarını biçimlendirmek için kullanılan alt görev belirticilere argüman denir
#sep argümandır


print()

type()

?print #fonksiyonların dökümanlarına detaylı bilgilere erişmek istediğimizde yazarız consoleda yazar





#VERİ YAPILARI
#LİSTELER

#VERİ YAPILARI ÇEŞİTLERİ İHTİYAÇLARIMIZA GÖRE PROG. DİLLERİNDEN İSTEDİKLERİMİZİ YERİNE GETİREBİLME İMKANI SAĞLIYOR
#listeler: python önemli veri yapılarından biri. değiştirilebilir, sıralıdır, farklı tipte verileri bir arada tutar index işlemi yapılabilir

#[]
#list()


#type list (bu bir veri yapısı)
# köşeli parantezin içindekiler integer ama variable explorerda veriler bir listtir bunun nedeni
# tipi list görünüyor bu bir nesnedir.
#liste tipinde bşr nesne veri yapısıdır.
#önemli liste bir üst tiptir. bir veri yapısıdır
#bu veri y. içerisinde string ve sayısal numerik float tipte değerlerde olabilir.

notlar = [90,80,70,50]
type(notlar)

#birbirinden farklı tip oluşturan lis oluşturalım

liste = ["a",19.3,90]
list_genis = ["a",19.3,90,notlar] #liste çerisine liste tanımladık

len(list_genis) #4 farklı tipte nesne vardır

#LİSTE İÇİ TİP SORGULAMA

type(list_genis)
#elamana erişmek istediğimizde []
type(list_genis[0]) #str
list_genis[3]
list_genis[1]
list_genis[2]

type(list_genis[3]) #list
type(list_genis[2]) #integer
type(list_genis[1]) #float

tum_liste = [liste, list_genis]
#listeleri birleştirerek oluşturma

#silme işlemi
#del tum_liste


#LİSTE ELEMANLARINA ERİŞMEK
#[]

liste = [10,20,30,40,50]
liste[1]
liste[0]

liste[0:2]

liste[:2] #o ı yazmasakta aynı üsttekiyle
liste[2:]

yeni_liste = ["a",10,[20,30,40,50]]
yeni_liste

yeni_liste[2]

yeni_liste[0:2]

yeni_liste[2][1]

#listenin bir elemanının içindeki başka elamna erişmek istedğimizde
#çıktı 30 a eriştik



#LİSTELERE ELEMAN EKLEME, ELEMAN DEĞİŞTİRME, SİLME 

liste = ["ali", "veli","berkcan","ayse"]
#listedeki veli ifadesini velinin babası şeklinde değiştirme
liste[1] = "velinin_babasi" #eleman degistirme

#birden fazla elemana erişim benzer şek,ilde değişik yapma
liste[1] = "veli"
liste[0:3] = "alinin_babasi", "velinin_babasi","berkcanin_babasi"
#amaç 3 elemanın babalarını da buraya koymak

#listeye yeni eleman ekleme
liste
liste =  ["ali", "veli","berkcan","ayse"]

liste = liste + ["kemal"]

#liste içerisinden eleman silme
 del liste[2] #berkcanı sildi
 liste
 
#LİSTE METODLARI
 
 liste = ["ali","veli","isik"]
 
 dir(liste)

liste
#append : eleman ekleme
liste.append("berkcan")
#liste değiştirilebilir bir veri yapısı olduğundan metotlar yardımıyla berkcanı ekledik değişiklik yapabildik
liste
#bazı metodlar yapıların üzerinde kalıcı değişikler yapabilirken bazıları yapmaz
#berkcanı listeden silme
liste.remove("berkcan")
liste

#indekse göre eleman ekleme ve silme
#insert ve pop

#insert
liste = ["ali","veli","isik"]
liste

liste.insert(0,"ayse")
liste

#nottttt:önceden yaptığımızda liste[0]="ayse" dediğimizde ali yi slip ayse getiriyordu

#sonuncu elemana eklemek istersek
liste.insert(3, "mehmet")
liste

liste.insert(5,"berk")
liste

#eleman saydırma işlemi yapalım
len(liste)
#len listeyi kullanarakbir eleman ekleme işlemini otomatik olarak sona ayapacağız
liste.insert(len(liste), "beren")
liste
#listenin sonuna len(liste)ile veri ekledik



#pop metodu eleman silmek için kullanılır
liste.pop(0)
liste

liste.pop(2)
liste


#DİĞER LİSTE METODLARI
#count : sayma metodu

liste = ["ali","sıla","ali","sıla","yaren"]
liste
liste.count("ali")
liste.count("sıla")
liste.count("yaren")

#copy
liste_yedek = liste.copy()

#extend : iki listeyi birleştirmek için kullanılıyor

liste.extend(["a","b",10])
liste

#bir elemanın hangi indekste olduğu işlemi
liste.index("ali")

#revers : elemanları terse çevirme işlemi
liste.reverse()
liste

#sort metodu : sıralama yapmak için mkullanılı
#liste.sort() hata verecek çünkü farklı tiplerde olduğu için yeni bir liste olusturmam gerek

liste = [10,40,5,90]
liste
liste.sort()
liste

#clear liste içerisindeki elemanları temizleme,
liste.clear()
liste


#VERi YAPILARI - TUPLE

t = ("ali","veli",1,2,3.2,[1,2,3,4])

t = "ali","veli",1,2,3.2,[1,2,3,4]

#tuple()
#tek elemandan tuple oluşturma

#t = ("eleman")
t = ("eleman",)
type(t)
#tek elemanlı tuple oluştururken sonuna virgül atmamız gerek yoksa bize değeri str olarak verir 
#virgül koyduğumuzda tuple olarak verecektir typei

#tuple demet eleman işlemleri
t = ("ali","veli",1,2,3.2,[1,2,3,4])
t
t[1]
t[0:3]

t[2] = 99
#tuple değiştirilemez bir veri yapısıdır atama işleme yapılamaz


#sözlük(dictionary) olusturma
#kapsayıcıdır.birbirinden farklı tipi barındırır
# sırasızdır 
#değiştirilebilir.
#anahtar ifadeler ve anahtar ifadelerin karsılıklarının bir arada tutulduğu referanslı bir veri yapısıdır.
# key ve value
#{}
sozluk = {"reg":"regresyon modeli",
          "loj":"lojistik regresyon",
          "cart":"classification and reg"}
sozluk

len(sozluk)



#sözlük eleman seçme islemleri
#sozluk[0]
#hata aldık nedeni sırasız olduğunda indeksleme yapamadık
#yerine
sozluk["reg"]
sozluk["loj"]
sozluk["cart"]

sozluk = {"reg" : ["rms",10],
          "loj" : ["ljr",20],
          "cart" : ["see",30]}
sozluk["reg"]
#console da ['rms',10]


sozluk = {"reg" : {"rms":10,
                   "ljr":20,
                   "see":30},
          
          "loj" : {"rms":10,
                   "ljr":20,
                   "see":30},
          
          "cart" : {"rms":10,
                   "ljr":20,
                   "see":30}}
sozluk["loj"]["ljr"]

#sozluk eleman ekleme degistirme
#değiştirme işlemi
sozluk = {"reg":"regresyon modeli",
          "loj":"lojistik regresyon",
          "cart":"classification and reg"}

sozluk["gbm"] = "gradient boosting mac"
sozluk
#key=value
sozluk["reg"] = "coklu regresyon modeli"
sozluk

#sozluk[1] #hata verdi

sozluk[1]= "yapay sinir agları"
sozluk


l = [1]
l
sozluk[l] ="yeni bir sey" #tip hatası verdi sözlüklerde key değerleri ancak sadece sabit veri yapıları ile olusturuyabilir
#key sabitliğinden endişe etmemeiz gereken referans değerlerdir

t = ("tuple",)
sozluk[t] = "yeni bir sey"
sozluk


#set(küme) olusturma

#sırasız. indeksiz, setler içerisindeki değerler essiz tekrare den değer yok.
#setler değiştirilebilir ve farklı veri tip barındırabilir
#performans odaklı veri tipi
#hız istediğimizde veri yapıları iht. olduğunda kullanılır
#mat. kümelere benzer

s = set()
s


l = [1,"a","ali",123]
l

s = set(l)
s

t =  ("a","ali")
s = set(t)
s


ali = "ata_bakma_uzaga_git"
type(ali)

s = set(ali)
s
#tekrar eden harfleri getiriyor

l = ["ali","lutfen","ata","bakma","uzaga","git","ali","git"]
s = set(l)
s
#hepsinden bir tane alıyor

len(s)
#6 elamnı var
# setler hızlı ve performans odaklı olmayı sağlıyor


#sıra durumu sorgulama
l[0]
s[0] #sırarsız olduğundan indeks işlemi gerçekleştrmez eşsiz değerlerden olusuyor


#set eleman ekleme ve çıkarma

l = ["gelecegi","yazanlar"]

s = set(l)
s

dir(s)

s.add("ile")
s

s.add("gelecege_git")
s

#eklediğimiz sıradan bağımsız bir şekilde ekleme islemini gerceklestirdi
#sırasızlıgını ifade ediyor

s.add("ile")
s
#tekrar var olan bir değeri ekleyemiyoruz çünkü var 

#eleman silmek istersek remove
s.remove("ile")
s

#setlerde fark islemleri
#difference&symmetric islemleri

# =============================================================================
# difference() ile iki kümenin farkını ya da "-" ifadesi
# intersection() ile iki küme arasındaki kesişimi & ifadesi
# union() ile iki kümenin birleşimi
# symmetric_fifference ile ikisindede olmayanlar
# =============================================================================



#difference
set1 = set([1,3,5])
set2 = set([1,2,3])

set1.difference(set2)#set1 de olup set 2 de olmayan
set2.difference(set1) #set2 de olup set1 de olmayan

#symmetric_difference
set1.symmetric_difference(set2)

set1-set2 #5
set2-set1 #3

#intersection: kesisim

set1.intersection(set2)
set2.intersection(set1)

set1&set2 #operatör ile yaptıgımızda
#saklamak istersek 

kesisim = set1 & set2
kesisim

set1.union(set2)
set2.union(set1)
#birleşimde aynı olandan bir tane yazılır


birlesim = set1.union(set2)
birlesim

set1.intersection_update(set2)
set1
#kesisimde yer alan ifadeler set1in ifadeleri olmustur


# setlerde kümelerde sorgu islemleri

set1 = set([7,8,9])
set2 = set([5,6,7,8,9,10])

#iki kümenin kesisiminin bos olup olmadıgını sorgu.
set1.isdisjoint(set2)

# bir kümenin bütün elemanlarının başka bir küme içerisinde yer alıp olmadığına baakacagz
set1.issubset(set2)

#bir küme diğerini kapsıyor mu
set2.issuperset(set1)


#fonksiyonlara giriş ve fonksiyon okuryazarlığı

print()
print

#fonksiyon : bazı görevleri yerine getirmek üzere genel amaçlar tanıyan görevciler işleçlerdir

?print
#buna fonk. dökümantasyonu denir
#fonk. genel amaçlarını biçimlendirir


print("a","b", sep = "_")
#fonk. genel amaçlarını biçimlendirerek
#kullanılan belirteçler argümandır sep bir argümandır

print()

#len() bu sekilde kullanıldığında hata verir içinde bir argüman olmak zorundadır
len("a")

#fonksiyon nasıl yazılır

#matematiksel işlemler
4*4
4/4
4-2
4+3

#♥kare alma
4**2
3**2

#ben pythonda fonk. tanımlıyorum demenin yolu def kullanmaktır

def kare_al(x):
    print(x**2)

kare_al(3)

#bilgi notuyla çıktı öğrenmek

def kare_al(x):
    print("girilen sayının karesi: " + str(x**2))
    
kare_al(3)

#hem karesi alınan sayıyı hem de çıktıyı görmek istiyorsam:

def kare_al(x):
    print("girilen sayı: "
          + str(x) +
          ", karesi: " +
          str(x**2))

kare_al(3)

#iki argümanlı fonk. tanımlamak

def carpma_yap(x,y):
    print(x*y)

carpma_yap(2, 3)


#ne zaaman fonk. yazılır?

#programlama dilleri içinde tekrar eden görevleri yerine getirmek için var olan işlemleri 
#daha programatik bir şekilde gerçekleştirmeye yarar.

#sokak lambaları örneği
#veriler isi,nem,sarj

def lamba_hesap(isi,nem,sarj):
    print((isi+nem)/sarj)

lamba_hesap(25, 40, 70)

#fonksiyonun çıktısını girdi olarak kullanma : return

def lamba_hesap(isi,nem,sarj):
    return(isi+nem)/sarj

lamba_hesap(25, 40, 70)
cikti = lamba_hesap(25, 40, 70)
cikti
print(cikti)

lamba_hesap(25, 40, 70)



def lamba_hesap(isi,nem,sarj):
    return
    (isi+nem)/sarj

lamba_hesap(25, 40, 70)    

#fonk return ifadesine geldiği zaman durur diğer kısımla ilgilenmez


# local ve global değişkenler

x=10
y=20 #☺global değişkenlerdir

def carpma_yap(x=2, y=1):
    return(x*y)
carpma_yap(2,3)

# def carpma_yap(x=2, y=1):
    # return(x*y)     LOCAL ETKİ ALANI

# local etki alanından global etki alanını değiştirme

x = []
def eleman_ekle(y):
    x.append(y)
    print(str(y) + "  ifadesi eklendi.")
    
eleman_ekle("nur")
eleman_ekle("hatice")

x

#karar kontrol yapıları
#true-false sorgulamaları

#mantıksal sorgulamalar demektir

sinir = 5000

sinir == 4000

sinir == 5000


5 == 4
5 == 5

#°if yapısı

#eğer demek

sinir = 50000
gelir = 40000
gelir < sinir

if gelir < sinir:
    print("gelir sınırdan küçük")
    print((gelir*2))
 # if sorgusu true gelirse sorguyu çalıstırır
    

if gelir > sinir:
    print("gelir sınırdan büyük")



#else yapısı  #değilse
sinir = 50000
gelir = 40000  

if gelir > sinir:
    print("gelir sınırdan büyük") 
else:
    print("gelir sinirden kücük")

#diğer örn
    
sinir = 50000
gelir = 51000 

if gelir == sinir:
    print("gelir sınıra eşittir") 
else:
    print("gelir sinira esit degildir")


#elif yapısı
#birden fazla koşul kullanmak için kullanılır
    #değilse ama eğer böyleyse

sinir = 50000
gelir1 = 51000
gelir2 = 50000
gelir3 = 35000 

if gelir1 > sinir:
    print("tebrikler, hediye kazandınız") 
elif gelir1 < sinir:
    print("uyarı!")
else:
    print("takibe dewamke")



sinir = 50000
gelir1 = 51000
gelir2 = 50000
gelir3 = 35000 

if gelir3 > sinir:
    print("tebrikler, hediye kazandınız") 
elif gelir3 < sinir:
    print("uyarı!")
else:
    print("takibe dewamke")



sinir = 50000
gelir1 = 51000
gelir2 = 50000
gelir3 = 35000 

if gelir2 > sinir:
    print("tebrikler, hediye kazandınız") 
elif gelir2 < sinir:
    print("uyarı!")
else:
    print("dewamke")


#if ve input ile kullanıcı etkileşimli program
    

# mini uygulama
sinir = 50000
magaza_adi = input ("magaza adi nedir?")
gelir = int(input ("gelirinizi giriniz: "))

if gelir > sinir :
    print("tebrikler:" + magaza_adi + " promosyon kazandınız!")
elif gelir < sinir:
    print("uyari! cok düsük gelir!" + str(gelir))
else:
    print("takibe dewamke")



#döngüler
    
#for döngüsü
    
ogrenci = ["ali" ,"veli" ,"isik", "ayca"]

ogrenci[0]
ogrenci[1]


for i in ogrenci:
    print(i)


#for döngüsü örnek
    
maaslar = [1000,2000,3000,6000]

for i in maaslar:
    print(i)


# döngü ve fonksiyonların birlikte kullanımı
    
# maaslaa%20 zam yeni maas hesapla
    
#döngü yaz
#fonk yaz
    
maaslar = [2000,1000,5000,6000,3000]

def yeni_maas(x):
    print(x*20/100 + x)
for i in maaslar:
    yeni_maas(i)


#if for ve fonksiyonların birlikte kullanımı

#maası 3000 den yüksek %10 az olana %20

maaslar = [2000,1000,5000,6000,3000]

def maas_ust(x):
    print(x*10/100+x)
def maas_alt(x):
    print(x*20/100+x)
for i in maaslar:
    if i >= 3000:
        maas_ust(i)
    else:
        maas_alt(i)

#break ve continue
        
# =============================================================================
# döngüler içerisin de ne demekti döngü for mesela
# bazen belirli bir şartı sağlayan ifadeler yakalandığında
# ki nasıl yakalıyorduk if ler ile bu belirli şartları sağlayan ifadeler 
# yakalndığında döngü bitirilmek istenilir yada bu şartı sağlayan ifadeler görmezden gelmek istedir
# =============================================================================




#█5000 baz alacağız

# break

maaslar = [9000,8000,2000,5000,3000,1000,1500,7000]

dir(maaslar)

maaslar.sort()
maaslar

for i in maaslar:
    if i == 5000:
        print("kesildi")
        break
    print(i)






maaslar = [9000,8000,2000,5000,3000,1000,1500,7000]

dir(maaslar)

maaslar.sort()
maaslar

for i in maaslar:
    if i == 5000:
      continue
    print(i)


#while 
    
#olduğu sürece
#bu sart sağlandığı sürece demek
    

sayi = 1

#siniflara giris ve sinif tanimlamak

# class nedir : benzer ozellikler ortak amaclar tasiyan gruplar olusturmak icin kullanilir

class VeriBilimci():
    print("Bu bir siniftir.")

# sınıf ozellikleri
#class attributes
class VeriBilimci():
    bolum = " "
    sql = " "
    deneyim_yili = 0
    bildigi_diller = []
    
#siniflarin özelliklerine erismek istiyorsam
VeriBilimci.bolum
VeriBilimci.sql

#siniflarin özelliklerini degistirmek
VeriBilimci.sql = "hayır"
VeriBilimci.sql

#siniflarin örneklenmesi
ali = VeriBilimci()
ali.sql
ali.deneyim_yili
ali.bolum
ali.bildigi_diller.append("python")
ali.bildigi_diller


veli = VeriBilimci()
veli.sql
veli.bildigi_diller #birimden birime değişmesi lazım  Veli de python yok
#örnek özellikleri kavramıyla bu yanlısı düzeltecegiz

# örnek özellikleri

class VeriBilimci():
    bildigi_diller = ["pyhton","R"]
    def __init__(self):
        self.bildigi_diller = []
    
ali = VeriBilimci()
ali.bildigi_diller   


ali.bildigi_diller.append("python")
ali.bildigi_diller


veli = VeriBilimci()
veli.bildigi_diller   

veli.bildigi_diller.append("R")
veli.bildigi_diller

VeriBilimci.bildigi_diller

class VeriBilimci():
    bildigi_diller = ["R","pyhton"]
    bolum = " "
    sql = " "
    deneyim_yili = 0
def __init__(self):
    self.bildigi_diller = []
    self.bolum = " "
    
VeriBilimci.bolum
ali.bolum = "istatistik"
ali.bolum

VeriBilimci.bolum
veli.bolum = "ybs"
veli.bolum


#örnek metodları
# örnekler üzerinde çalısan fonksiyonları çalıstırma
class VeriBilimci():
      calisanlar = []
      def __init__(self):
          self.bildigi_diller = []
          self.bolum = []
          
      def dil_ekle(self, yeni_dil):
          self.bildigi_diller.append(yeni_dil)
          
          
ali = VeriBilimci()
ali.bildigi_diller
ali.bolum

veli = VeriBilimci()
veli.bildigi_diller
veli.bolum

dir(VeriBilimci)
# VeriBilimci.dil_ekle hata üretir

ali.dil_ekle("R")
ali.bildigi_diller

veli.dil_ekle("pyhton")
veli.bildigi_diller


#miras yapısı
class employees():
  def __init__(self):
    self.firstname = " "
    self.lastname = " "
    self.address = " "

class datascience(employees):
    def __init__(self):
        self.programing = " "

class marketing(employees):
    def __init__(self):
        self.storytelling = " "
        
        

data = datascience()
data.firstname = 1


mar1 = marketing()
mar1.firstname = 3

# not: fonsiyon yapıda da tanımlayabilirz

class employees_yeni():
    def __init__(self,firstname,lastname,address):
        self.firstname = firstname
        self.lastname =lastname
        self.address = address
    
ali = employees_yeni("a", "b", "c")
ali.address


#fonksiyonel programlamaya giriş

#fonksiyonlar dilin baştacıdır
# birinci sınıf nesnelerdir
# tüm etkisiz fonks. (stateless, girdi-çıktı)
# yüksek seviye fonk
# vektorel operayonlar


#yan etkisiz fonk örnek1

# örnek 1 : yan etki

A = 9

def impure_sum(b):
    return b + A  #saf olmayan


def pure_sum(a,b):
    return a + b #saf
impure_sum(6)
pure_sum(3, 4)

#yan etkisiz fonk örnek 2

# ornek2 olumcul yan etkiler

#oop 

class LineCounter:
    def __init__(self, filename):
        self.file = open(filename, "r")
        self.lines = []
        
    def read(self):
        self.lines = [line for line in self.file]
        
    def count(self):
        return len(self.lines)
    
lc = LineCounter("deneme.txt")

print(lc.lines)
print(lc.count())

lc.read()

print(lc.lines)
print(lc.count())


#fonsiyonel prog.

def read(filename):
    with open(filename, "r") as f:
        return [line for line in f]
    
def count(lines):
    return len(lines)

example_lines = read("deneme.txt")
lines_count = count(example_lines)
lines_count


#isimsiz fonk
def old_sum(a,b):
    return a + b

old_sum(4, 5)

new_sum = lambda a,b: a + b
new_sum(4,5)


sirasiz_liste = [("b",3),("a",8),("d",12),("c",1)]
sirasiz_liste

sorted(sirasiz_liste, key =lambda x: x[1])


#vektörel operasyonlar

a = [1,2,3,4]
b = [2,3,4,5]

ab = []
range(0, len(a)) 
for i in range(0, len(a)):
    ab.append(a[i]*b[i])

ab

#FP
import numpy as np
a = np.array([1,2,3,4])
b = np.array([2,3,4,5])

a*b

#map,filter ve reduce fonk

liste = [1,2,3,4,5]

for i in liste:
    print(i+ 10)


list(map(lambda x: x + 10, liste))

# =============================================================================
# map: verilen vektörün içerisinde tanımlanacak fonk çalıstırma imkanı verir
# lambda isimsisz fonk.
# =============================================================================

#filter: benzer şekilde fonk iteratif nesne olarak çalışır
liste = [1,2,3,4,5,6,7,8,9,10]

#2 ye bölün. 0 kalan

list(filter(lambda x: x % 2 == 0, liste))

#reduce
#map ve filter a benzer falan indirgeme demektir indirgeme işlemi yapar

from functools import reduce

liste = [1,2,3,4]
reduce(lambda a,b: a + b, liste)

#modül oluşturmak


#hatalar(istisnalar)

#exceptions
# ZeroDivisionError hatası
a = 10
b = 0

a/b

try:
    print(a/b)
except ZeroDivisionError:
    print("paydada sıfır olmaz")

#tip hatası
a = 10
b = "2"    

a/b

try:
    print(a/b)
except TypeError:
    print("sayı ve string problemi")




a = 10
b = 2    

a/b

try:
    print(a/b)
except TypeError:
    print("sayı ve string problemi")




