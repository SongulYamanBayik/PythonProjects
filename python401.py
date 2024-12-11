#class

class VeriBilimci():
    bolum=''
    sql='evet'
    deneyim_yili=0
    bildigi_diller=[]
    

VeriBilimci.sql="hayır"


# örnek özelikler

class developer():
    def __init__(self): #örneklemedir. temsilcidir.
        self.programing_language=[] #her örneğe özel kaydı tutar.
        
ali=developer()
ali.programing_language.append("Python")
ali.programing_language

veli=developer()
veli.programing_language.append("C#")
veli.programing_language


#method ile class örneği

class department():
    person=[]
    def __init__(self):
        self.programing_language=[]
        self.experience=''
    def create_language(self,new_language):
        self.programing_language.append(new_language)
        
        
department.person.append("Ayse")
department().person.append("Fatma")

Ayse=department()
Ayse.create_language("C#")
Ayse.experience=2
Ayse.programing_language  


Fatma=department()
Fatma.create_language("Python")
Fatma.experience=1
Fatma.programing_language


#inheritance - miras yapıları

class employees(department()): #departman sınıfındaki tüm özellikleri çalışanlar
# sınıfına aktarır.


#fonksiyonel programlama

#birinci sınıf nesnelerdir.
#yan etkisiz foksiyonlardır. (stateless, girdi-çıktı)
#yüksek seviye foksiyonlardır.
#vektörel operasyonlar

#yan etkisiz fonksiyon (pure functions)

A=5

def impure_sum(b): #dışarıya bağımlılığı var.
    return b+A

def pure_sum(a,b): #girdi değiştiğinde sonuç değişir.
    return a+b


#isimsiz fonksiyonlar (anonymous functions)

sum=lambda a,b: a+b #sum isminde fonksiyon oluşturuldu, a ve b değişkenleri alıyor
# ve o sayıları topluyor


sirasiz_liste=[('b',3),('a',8),('d',12),('c',1)]

sorted(sirasiz_liste,key=lambda x: x[1])

#vektörel operasyonlar

import numpy as np
a=np.array([1,2,3,4])
b=np.array([2,3,4,5])

a*b


#map - filter - reduce

liste=[1,2,3,4,5,6,7,8,9,10]

list(map(lambda x: x+10, liste)) #verilen bir nesnenin üzerinde tanımlanacak
#fonksiyonu çalıştırma imkanı verir. isimsizdir.


list(filter(lambda x: x%2==0,liste)) # 2ye tam bölünenleri filtreledi


from functools import reduce # functools modülünden reduce fonksiyonu indirdi

reduce(lambda a,b: a+b,liste)


#modül(kütüphane) oluşturma
import HesapModulu as hm

hm.yeni_maas(3500)
                                    #iki kullanımda aynıdır.
from HesapModulu import yeni_maas
yeni_maas(3500)


#exceptions - hatalar/istisnalar

try:
    print(a/b)
except ZeroDivisionError:
    print("payda da sıfır olamaz!")
    
    
try:
    print(a/b)
except TypeError:
    print("sayı ve string problemi")
    
