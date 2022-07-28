#1.Soru#
'''sayi=int(input("Bir Sayı Giriniz: "))
if sayi<0:
    print("Negatif(-)")
elif sayi==0:
    print("Sıfır")
else:
    print("Pozitif(+)")

#2.Soru#
mat=int(input("Matematik Notunuzu Giriniz"))
mat2=int(input("Matematik 2.Notunuzu Giriniz"))
tr=int(input("Türkçe Notunuzu Giriniz"))
tr2=int(input("Türkçe 2.Notunuzu Giriniz"))
ort=((mat+mat2)/2)+((tr+tr2)/2)
print(ort)
if ort>=50:
    print("Geçtin")
elif ort<50:
    print("Kaldın")

#3.Soru#
a=int(input("1.sayi gir"))
b=int(input("2.Sayi gir"))
if a>b:
    print("A>B")
elif a==b:
    print("A=B")
elif a<b:
    print("A<B")

#5.Soru#
sayi1=12
sayi2=60
toplam=0
if sayi1<=sayi2:
    if sayi1%2==0:
        sayi1=sayi2
        toplam=sayi1+sayi2
    else: toplam=sayi2-sayi1
toplam+=toplam
print(toplam)

#6.Soru#
0

#7.Soru#
a="Merhaba"
b="Hoşgeldin"
c="BayBay"
d="Nasılsın"
cevap=input("1 DEN 4 E KADAR BİR SAYI TUTUNUZ")
if cevap=="1":
    print(a)
if cevap=="2":
    print(b)
if cevap=="3":
    print(c)
if cevap=="4":
    print(d)

#8.Soru#
k1=int(input("1.Kenar Uzunluğunu Giriniz"))
k2=int(input("2.Kenar Uzunluğunu Giriniz"))
k3=int(input("3.Kenar Uzunluğunu Giriniz"))
k4=int(input("4.Kenar Uzunluğunu Giriniz"))

if k1==k2==k3==k4:
    print("Kare")
if k1==k2 and k4==k3 or k1==k3 and k2==k4 or k1==k4 and k2==k3:
    print("Dikdörtgen")

#9.Soru#
k1=int(input("1.Kenar Uzunluğunu Giriniz"))
k2=int(input("2.Kenar Uzunluğunu Giriniz"))
k3=int(input("3.Kenar Uzunluğunu Giriniz"))

if k1==k2==k3:
    print("Eşkenar Üçgen")
elif k1==k2 or k1==k3:
    print("İkiz Kenar")
elif k1!=k2 or k1!=k3:
    print("Çeşit Kenar")

#10.Soru#
boy=float(input("Boyunuzu Giriniz: "))
kilo=int(input("Kilonuzu Giriniz: "))
toplam=kilo/(boy**2)
print(toplam)
if toplam<= 18.5:
    print("Zayıf")
elif toplam<=25:
    print("Normal")
elif toplam>=25:
    print("Obez")

#Ek Soru 1#
sayi1=int(input("Bİr sayi giriniz"))
if sayi1%2==0:
    print("çift")
else:
    print("Tek")'''