iller = input("Lütfen hesaplama yapacağınız ilin ismini giriniz: ")
tur = input("Lütfen ne faturası hesaplayacağınızı giriniz: ")
birim = int(input("Lütfen ne kadar kullandığınızı yazınız: "))



# buraya her şehrin su fiyatlarını yazıyoruz
istanbulSu = 5.56
ankaraSu = 7.92
izmirSu = 7.56
bursaSu = 6.22
antalyaSu = 7.26

# buraya her şehrin su fiyatlarını yazıyoruz
istanbulGaz = 2.35
ankaraGaz = 2.32
izmirGaz = 2.30
bursaGaz = 1.76
antalyaGaz = 2.79

# buraya her şehrin kw fiyatlarını giriyoruz

elektrik = 1.38 # sadece 1 değer yazmamın nedeni maalesef illere göre kw fiyatını bulamamam ama ileride değiştireceğim.
sonucElektrik = elektrik * birim

# buraya uğraşmamak için direk metni girdim
suFatura = "Su faturanıza yansıyacak miktar:"
gazFatura = "Gaz faturanıza yansıyacak miktar:"
elektrikFatura = "Elektrik faturanıza yansıyacak miktar:"

#SU HESAPLARI
if tur == "su" or "Su" and iller == "istanbul" or "İstanbul": # "su" or "Su" yazmamızın nedeni küçük büyük harf kullanabilmemiz.
    sonuc1 = istanbulSu * birim
    print(suFatura,sonuc1,"TL")
    
elif tur == "su" or "Su" and iller == "ankara" or "Ankara":
    sonuc2 = ankaraSu * birim
    print(suFatura,sonuc2,"TL")
    
elif tur == "su" or "Su" and iller == "izmir" or "İzmir":
    sonuc3 = izmirSu * birim
    print(suFatura,sonuc3,"TL")

elif tur == "su" or "Su" and iller == "bursa" or "Bursa":
    sonuc4 = bursaSu * birim
    print(suFatura,sonuc4,"TL")

elif tur == "su" or "Su" and iller == "antalya" or "Antalya":
    sonuc5 = antalyaSu * birim
    print(suFatura,sonuc5,"TL")

#GAZ HESAPLARI

elif tur == "gaz" or "Gaz" and iller == "istanbul" or "İstanbul":
    sonuc6 = istanbulGaz * birim
    print(gazFatura,sonuc6,"TL")

elif tur == "gaz" or "Gaz" and iller == "ankara" or "Ankara":
    sonuc7 = ankaraGaz * birim
    print(gazFatura,sonuc7,"TL")

elif tur == "gaz" or "Gaz" and iller == "izmir" or "İzmir":
    sonuc8 = izmirGaz * birim
    print(gazFatura,sonuc8,"TL")

elif tur == "gaz" or "Gaz" and iller == "bursa" or "Bursa":
    sonuc9 = bursaGaz * birim
    print(gazFatura,sonuc9,"TL")

elif tur == "gaz" or "Gaz" and iller == "antalya" or "Antalya":
    sonuc10 = antalyaGaz * birim
    print(gazFatura,sonuc10,"TL")

#ELEKTRİK HESAPLARI

elif tur == "elektrik" or "Elektrik" and iller == "istanbul" or "İstanbul":
    print(elektrikFatura,sonucElektrik,"TL")

elif tur == "elektrik" or "Elektrik" and iller == "ankara" or "Ankara":
    print(elektrikFatura,sonucElektrik,"TL")

elif tur == "elektrik" or "Elektrik" and iller == "izmir" or "İzmir":
    print(elektrik,sonucElektrik,"TL")

elif tur == "elektrik" or "Elektrik" and iller == "bursa" or "Bursa":
    print(elektrikFatura,sonucElektrik,"TL")

elif tur == "elektrik" or "Elektrik" and iller == "antalya" or "Antalya":
    print(elektrikFatura,sonucElektrik,"TL")

# python gelismis-fatura-hesaplama.py