# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 10:19:41 2023

@author: fnsss
"""

"""
Python programalam dilinde girdiler değişken tanımlanır ama
diğer programlama dillerinden farklı olarak bu programalma dilinde
değişken tipini belirtmemize gerek yok
"""
"""a =5
print(a)"""
"""
Python programalama dilinde çıkış birimi olarak print komutunu
kullanırız.

Dip Not : Eğer ki varsayılan değerli bir değişken ataması yapıyorsak
"""
"""a=10
print(a)"""
"""
Eğer kullanıcıdan değer alarak işlem yapacak isek
"""
"""
isim = input("İsminizi Giriniz : ")
print ("Merhaba "+isim)
"""
""" Girilen İki Sayıyı Toplayan Programı Yazalım """
"""Sayi1= input("1. Sayıı Giriniz : ")
Sayi2= input("2. Sayıyı Giriniz : ")"""
"""
Ekrandan her aldığımız veri bize metin ifadesi olarak gelir
Metin ifadeleri programlamada herhangi bir şekilde matematiksel
işlemlere tabi tutulamaz.
"""
"""toplam = int(Sayi1)+int(Sayi2)"""
"""
tanımlanan her değişken varsayılan olarak string geldiği metinsel
ifade olduğu için bu metinsel ifadeyi formatlamamız gerekiyor
hangi değişkende formatlamak gerekiyorsa ona göre yapacağız.
"""
""""print("Sayıların Toplamı {0} ".format(toplam))"""
""" Girilen Vize ve Final Notu Ortalmasını Hesaplayan {} """
"""vize = input("Vize Notunu Giriniz : ")
final = input("Final Notunu Giriniz : ")
ortalama = (float(vize)*0.4)+(float(final)*0.6)
print ("Ortalama : {0}".format(ortalama))"""
""" Girilen 3 Sınavın ORtalamasını Bulan PRogramı Yazınız. """
"""y1=input("1. Yazılı : ")
y2=input("2. Yazılı : ")
y3=input("3. Yazılı : ")
ortalama= (float(y1)+float(y2)+float(y3))/3
print("Ortalama : {0}".format(ortalama))
"""
""" Yazılı ortalamasını girilen öğrencinin sınıfı geçme ve kalma
durumunu yazalım """
"""
ort=input("Ortalmanızı Giriniz : ")
if(int(ort)>=50):
    print("Geçtiniz")
else:
    print("Kaldınız")"""
""" Girilen sayının pozitif, negatif ve nötr olduğunu bulan
yazılımı yazcaz """
"""sayi=input("Sayı : ")
if(int(sayi)>0):
    print("Sayı Pozitif")
elif (int(sayi)<0):
    print("Sayı Negatif")
else:
    print("Sayı Nötr")"""
""" Yaşı girilen kişinin Ehliyet Alıp Alamadığını Bulan
Yazılımı Yazın """
"""yas = input("Lütfen yaşınızı giriniz : ")
if (int(yas)>=18):
    print("Ehliyet Alabilirsiniz.")
else:
    print("Ehliyet alamazsınız")"""
""" Kullanınının girdiği boy ve ağırlık değerlerine göre vücut kitle
indeksini (VKİ=agirlik/(boy*boy)) boymetre cinsinden hesapla
yan programı yazınız. """
"""boy = float(input("Boy (m): "))
kilo = float(input("Kilo (kg): "))
endeks = kilo/(boy*boy)
if endeks < 18:
    print("\n zayıf VKİ:{}".format(endeks))
elif endeks > 18 and endeks <= 25:
    print("\n kilolu VKİ:{}".format(endeks))
elif endeks > 25 and endeks <= 30:
    print("\n obez VKİ:{}".format(endeks))
elif endeks > 30:
    print("\n ciddi obez VKİ:{}".format(endeks))"""
"""email ="hasmet.tazegul@hotmail.com"
password="hasmet123456" 
girilenEmail= input("Email : ")
girilenPasswrod = input("Password : ")
if(girilenEmail==email):
    if(girilenPasswrod==password):
        print("Afferin doğru giriş yaptın")
    else:
        print("Bir işi doğru düzgün yapya")
else:
    print("Önce git kendini bul salak salak iş yapma")"""
deger = input("Giriş Yapmak için Evet(E) Çıkış Yapmak İçin Hayır(H)")
if (deger == "E" or deger=="e"):
    deger2 = input("Bak mal emin misin E/H")
    if deger2=="E" or deger2=="e":
        print("Git ne halin varsa gör")
    else:
        print("Aferin yola gel böyle aslan")
else:
    print("Bir yere gidemezsin program benim değil mi :D")