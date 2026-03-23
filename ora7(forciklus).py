# For ciklus

# A működése ugyan az mint más nyelveknél a foreach ciklus

for i in range(10): # i: 0-tól, 10-ig, de a 10 nincs benne (9-ig)
    print(i, end=" ") # 0 1 2 3 4 5 6 7 8 9 
print() # enter

for i in range(2, 10): # i: 2-től, 10-ig (de a 10 nincs benne) (9-ig)
    print(i, end=" ") # 2 3 4 5 6 7 8 9 
print()

for i in range(2, 20, 3): # i = 2, 5, 8, 11, 14, 17
    print(i, end=" ") # 2 5 8 11 14 17
print()

for i in range(2, 10, -1): # i: 2-től 10-ig -1-esével
    print(i, end= " ") # semmi, mert már a 2 is kisebb mint 10
print()

for i in range(10, 2, -1): # 10-től 2-ig hátrafele
    print(i, end=" ") # 10 9 8 7 6 5 4 3    (2 nincs benne)
print()

# Képzeljük el úgy: range(2, 10) visszaad egy listát:
# [2,3,4,5,6,7,8,9]

for i in [11, 6, 10, 8, 5]:
    print(i, end= " ") # 11 6 10 8 5
print()

nevek = ["András", "Béla", "Cecil", "Dénes"]
for i in nevek:
    print(i, end=" ") # András Béla Cecil Dénes
print()

szöveg = "Helló Világ!"
for i in szöveg:
    print(i, end=" ") # H e l l ó   V i l á g !
print()

for alma in range(1, 10):
    print(alma, end=" ")
print()

# feladat: Határozzuk meg, a kétjegyű pozitív számok összegét.
összeg = 0
for i in range(10, 100):
    összeg += i
print(f"A kétjegyű pozitív számok összege: {összeg}") # 4905

# feladat: Hány darab 5-tel osztható pozitív egész szám van, ami 100-tól kisebb?
szamlalo = 0
for kisauto in range(1, 100):
    if kisauto % 5 == 0:
        szamlalo += 1
print(f"{szamlalo} db 5-tel osztható pozitív egész szám létezik, ami 100-tól kisebb.") # 19

# Feladat: Adott egy lista, ami 10 ember fizetését tartalmazza
fizetesek = [380000, 470000, 290000, 390000, 550000, 870000, 338000, 480000, 560000, 850000]
print(fizetesek)
# Mekkora az emberek átlag fizetése?
összeg = 0
for item in fizetesek:  # item = 380000, 470000, ..., 850000
    összeg += item
atlag = összeg / len(fizetesek)
print(f"Az átlag fizetés: {round(atlag)} Ft") # 517800 Ft

# Mekkora a legnagyobb fizetés (és melyik indexen található)?
legnagyobb = fizetesek[0]
for item in fizetesek:
    if item > legnagyobb:
        legnagyobb = item
# Ezzel a megoldással, az a probléma, hogy az indexhez nem férünk hozzá.
print(f"A legnagyobb fizetés {legnagyobb} Ft") # 870000 Ft

# Ha a lehetséges indexet nézzük végig, akkor runi fogjuk az értéket és az indexet is.
max_index = 0
for i in range(1, len(fizetesek)): # i = 1, 2, ..., 9
    if fizetesek[i] > fizetesek[max_index]:
        max_index = i
print(f"A legnagyobb fizetés {fizetesek[max_index]} Ft, a {max_index}. indexen található.")

# Hány olyan ember van aki az átlag alatt keres?
szamlalo = 0
for i in range(len(fizetesek)): # i = 0, 1, 2, ..., 9
    if fizetesek[i] < atlag:
        szamlalo += 1

print(f"{szamlalo} ember keres az átlag alatt.")

# Feladat: Írjunk egy programot, ami egy szöveget kódol.
# A páratlan számú karakterek az elejére, a párosak a végére kerülnek.
# pl.: A cica felmászott a fára    -> Acc emsotafr iaflázt  áa

szöveg = "A cica felmászott a fára"
kódolt = ""
for i in range(0, len(szöveg), 2): # i = 0, 2, 4, ..., 22
    kódolt += szöveg[i]
for i in range(1, len(szöveg), 2): # i = 1, 3, 5, ..., 23
    kódolt += szöveg[i]
print(kódolt) # Acc emsotafr iaflázt  áa

# Feladat: Írjunk egy programoz, ami egy ilyen módszerrel kódolt szöveget dekódól!

kódolt = "A nksuó eé zn sngo zrtm etnmfkt mtnmseee.zé iatmfhrsíűé aynseee,mr e eeeai e zrtk"
dekódolt = ""
fele = len(kódolt) // 2
print(f"Kódolt szöveg hossza: {len(kódolt)}") # 81
print(f"A fele: {fele}") # 40

for i in range(len(kódolt) // 2):
    dekódolt += kódolt[i] + kódolt[i + fele + 1]

print(dekódolt)



# Caeaser kódolás

szöveg = "óo sz wüfóhgáy trúsé foűzj sf zóunaz forérgry, yrég zry trwrgr óyüg zry forérgrw."

abc = "aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz"

# ctrl + alt + le
# alt + katt
for eltolás in range(1, len(abc)):
    kódolt = ""
    for char in szöveg.lower():
        hanyadik = 0
        for i in range(len(abc)):
            if char == abc[i]:
                hanyadik = i
        if char in abc:
            kódolt += abc[(hanyadik + eltolás) % len(abc)]
        else:
            kódolt += char
    print(kódolt)

