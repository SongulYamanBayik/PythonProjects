#upper-lower

gel_yaz="geleceği yazanlar"

u=gel_yaz.upper().title()
l=gel_yaz.lower()

u.isupper()
l.islower()


#replace

u=u.replace("I", "İ")


#strip(kırpma) - sadece başta ve sondaki belirtilen değerleri siler

gel_yaz.strip()
gel_yaz.strip("*")

#dir() - kullanılabilecek methodları listeler(gel_yaz.)

dir(gel_yaz)

#substring - 0 başlangıç, 3 e kadar demek. yani 0:i+1 olacak

u[3]
u[0:3]

#tür dönüşümü

number1=input() #kullanıcıdan değer alır
number2=input()

int(number1)+int(number2)


#print

print("geleceği", "yazanlar", sep="-")
#fonksiyonların genel amaçlarını biçimlendirmek için kullanılan
# alt görev belirteçlerine argüman denir.
