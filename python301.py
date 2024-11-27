#fonksiyon

def kare_al(x):
    return(x**2)
    

kare_al(3)

#----------------------

def topla(x,y):
    print(str(x) + " ve " + str(y) + " sayılarının toplamı: "+ str(x+y))
    
    
topla(5, 24)

#true&false

5==4 #false
5==5 #true

# if - elif - else

total=50000
shop_total=int(input("Mağaza gelirini giriniz"))

if shop_total>total:
    print("tebrikler!")
    
elif shop_total==total:
    print("sınırda kaldınız.")
    
else:
    print("çalışmaya devam!")
    
    
    
#mini uygulama (if, else, fonksiyon, for)

maaslar=[1000,2000,3000,4000,5000]

def maas_ust(x):
    print(x*10/100+x)
    
def maas_alt(x):
    print(x*20/100+x)  
    
for i in maaslar:
    if i>=3000:
        maas_ust(i)
    else:
        maas_alt(i)
        
#while

sayi=1

while sayi<10: #a kadar yani 10 dahidir.
    sayi+=1
    print(sayi)


# öğrendiklerime for döngüsü ekleyip örnek yapalım :) 

def not_hesapla(vize,odev,final):
    return((vize+odev+final)/3)

def not_hesapla_but(vize,odev,final,butunleme):
    return((vize+odev+final+butunleme)/4)

notlar=[]
vize=int(input("vize notunu giriniz: "))
notlar.append(vize)
odev=int(input("ödev notunuzu giriniz: "))
notlar.append(odev)
final=int(input("final notunuzu giriniz: "))
notlar.append(final)

sonuc=not_hesapla(vize, odev, final)

if sonuc<60:
    print("ortalama: "+ str(sonuc))
    print("üzgünüm geçemedin! bütünleme sınavına girmen gerekiyor.")
    butunleme=0
    notlar.append(butunleme)
    for i in notlar:
        if i==0:
            butunleme= int(input("bütünleme notu: "))
            sonuc=not_hesapla_but(vize, odev, final, butunleme)
            if sonuc<60:
                print("ortalama: "+ str(sonuc))
                print("üzgünüm geçemedin! gelecek yıl görüşürüz :D")
            else:
                print("ortalama: "+ str(sonuc))
                print("tebrikler! dersi geçtin")
    
else:
    print("ortalama: "+ str(sonuc))
    print("tebrikler! dersi geçtin")
    
    
# biraz fazla uydurmasyon oldu sanki ama neyse :D
    
