#list() - aynı dizide farklı tiplerde değer tutabilir

notlar=[90,80,70,60]
liste=["a", 9.20,90,notlar]
len(liste)

type(liste[0])


liste[3][2] #alt dizinin elamanına ulaşır

#eleman değişirme

notlar[1]=30
notlar[2:]=40,50

#listeye yeni eleman ekleme

notlar=notlar+[100]
notlar.append(90)
notlar.insert(0, 20)
notlar.insert(len(notlar), 70)
notlar.extend([90,80,70]) #birleştirme yapar, aynı dizinin üzerine


#listeden eleman silmek

#del notlar[0]
#notlar.remove(90)
#notlar.pop(5)

#count

notlar.count(40)


#copy

notlar2=notlar.copy()


#index - eleman dizide kaçıncı sırada

notlar.index(30)

#reverse - diziyi terse çevirme

notlar.reverse()


#sort - dizide sıralama yapar

notlar.sort()


#tuple - listeler gibi kapsayıcıdır, sıralıdır, DEĞİŞTİRİLEMEZ.
#(parantez olmadan da oluşturulur)

t= ("ali", "veli", 1,2,3.3,[1,2,3,4])


t1=("eleman",) # , eklenmez ise tuble olarak değil string olarak değer oluşturur.

#dictionary (sözlük) - kapsayıcıdır, değiştirilebilir, SIRASIZDIR.
# key değerleri sabit veri yapıları(int,str,tuple) olabilir örn list OLAMAZ.

sozluk={"REG" : ["Regresyon Modeli",20],
        "LOJ" : "Lojistik Regresyon",
        "CART" : "Classification and Reg.",
        "SSE" : {"RMSE" : 10,
                 "MSE" : 30}}

sozluk["REG"][1]
sozluk["SSE"]["RMSE"]

sozluk[1]="Yapay Sinir Ağları"

t=("tuple",)
sozluk[t]="yeni"

#set - sırasızdır, değerleri eşsizdir, değiştirilebilirler,
#farklı tipler barındırabilir. performans odaklıdır.

s=set(notlar) #tekrar edenleri tek eleman olarak alır.

ali="ali işini düzgün yap!"
s1=set(ali) #string değeri harflere ayırarak elemanları oluşturur, 
#tekrar eden olmaz.

s1.add("kitap oku")
s1.discard("kitap oku") #değeri arar varsa siler yoksa hata vermeden işlemlere
#devam eder


#difference - iki kümenin farkını alır

set1=set([1,3,5])
set2=set([1,2,3])

set1.difference(set2)
set2.difference(set1)
set1-set2
set1.symmetric_difference(set2) #ikisi arasındaki farkları verir


#intersection - kesişim

set1.intersection(set2)
set1&set2

#union birleşim

set1.union(set2)

set1.isdisjoint(set2) #iki kümenin kesişimi boş mu?

set1.issubset(set2) #set1 set2 nin alt kümesi mi?

set1.issuperset(set2) #set1 set2 nin kapsayıcısı mı?


