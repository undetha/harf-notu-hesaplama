def not_hesapla(satir):

    satir = satir[:-1]

    liste = satir.split(",")

    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])

    sonuc = not1*(3/10) + not2*(3/10) + not3*(4/10)


    if (sonuc >= 90):
        harf_notu = "AA"
    elif (sonuc >= 85):
        harf_notu = "BA"
    elif (sonuc >= 80):
        harf_notu = "BB"
    elif (sonuc >= 75):
        harf_notu = "CB"
    elif (sonuc >= 70):
        harf_notu = "CC"
    elif (sonuc >= 60):
        harf_notu = "CD"
    else:
        harf_notu = "FF"

    return isim + "--------->" + harf_notu + "\n"





with open("bilgi.txt","r",encoding="utf-8") as dosya:

    eklenecekler_listesi = []

    for i in dosya:

        eklenecekler_listesi.append(not_hesapla(i))

    with open("harf_notları.txt","w",encoding="utf-8") as dosya2:

        for i in eklenecekler_listesi:

            dosya2.write(i)

    with open("kalanlar_listesi.txt","w",encoding="utf-8") as dosya3:

        kalanlar_listesi = []

        for i in dosya:

            kalanlar_listesi.append(not_hesapla(i))

































