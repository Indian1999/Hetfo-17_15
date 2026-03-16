lista = [] # Üres lista

lista = [78, 56, 13, 22, 8, 12, 9, 80]

print(lista) # [78, 56, 13, 22, 8, 12, 9, 80]
print(lista[0]) # 78
print(lista[1]) # 56

lista[4] = 72 # a 4-es indexű elemt átírjuk 72-re
print(lista)  # [78, 56, 13, 22, 72, 12, 9, 80]

lista.append(100) # A lista végére fűzi a 100-at
print(lista)  # [78, 56, 13, 22, 72, 12, 9, 80, 100]
lista.append(22) # [78, 56, 13, 22, 72, 12, 9, 80, 100, 22]

# Elemek törlése:

lista.remove(22) # A 22 első előfordulását törli
print(lista) # [78, 56, 13, 72, 12, 9, 80, 100, 22]

lista.pop()  # Törli az utolsó elemet
print(lista) # [78, 56, 13, 72, 12, 9, 80, 100]

lista.pop(2) # 2-es indexű elemet törli
print(lista) # [78, 56, 72, 12, 9, 80, 100]

del lista[2] # 2-es indexű elemet törli
print(lista) # [78, 56, 12, 9, 80, 100]


# Elemszám lekérdezése
print("A lista hossza:", len(lista)) # 6


# Feladat: Adott egy lista, ami egy osztály év végi matekjegyeit tartalmazza.

osztalyzatok = [5, 3, 2, 5, 1, 3, 4, 5, 4, 5, 3, 4, 2, 2, 3, 5, 5, 5, 4]
print("Matek jegyek év végén:", osztalyzatok)

# Hány tanuló van az osztályban?
print(f"Az osztályban {len(osztalyzatok)} tanuló van.")

# Mennyi volt az év végi osztályátlag?

összeg = 0
i = 0
while i < len(osztalyzatok): # i megy 0-tól 18-ig
    összeg += osztalyzatok[i]
    i += 1

atlag = összeg / len(osztalyzatok)
print(f"Az osztály matek osztályzatainak az átlaga: {round(atlag, 2)}")

# Hány tanuló kapott 5-öst év végén? Ez a tanulók hány százaléka?

szamlalo = 0
i = 0

while i < len(osztalyzatok):
    if osztalyzatok[i] == 5:
        szamlalo += 1
    i += 1

szazalek = szamlalo / len(osztalyzatok) * 100
print(f"{szamlalo} tanuló szerzett 5-öst. Ez az osztály {round(szazalek)} %-a.")

# Volt-e olyan tanuló aki megbukott?

volt_bukott = False
i = 0
while i < len(osztalyzatok):
    if osztalyzatok[i] == 1:
        volt_bukott = True
        break    # Kilép a ciklusból
    i += 1

if volt_bukott:
    print("Van olyan diák aki megbukott.")
else:
    print("Nem bukott meg senki.")

# Feladat: Adott egy lista ami egy osztály tanulóinak a magasságát tartalmazza.

magassagok = [157, 182, 190, 167, 180, 183, 177, 150, 148, 199, 187, 188, 205, 187]
print("Magasságok:", magassagok)

# Hány tanuló van az osztályban?
print(f"Ebben az osztályban {len(magassagok)} tanuló van.")

# Hány cm magas a legmagasabb diák?
max_index = 0
i = 1
while i < len(magassagok):
    if magassagok[max_index] < magassagok[i]:
        max_index = i
    i += 1

print(f"A legmagasabb diák {magassagok[max_index]} cm magas. A lista {max_index}. indexén található.")

# Mekkora az átlagos magasság? (Egész értékekre kerekíts!)
összeg = 0
i = 0
while i < len(magassagok):
    összeg += magassagok[i]
    i += 1

atlag = összeg / len(magassagok)
print(f"Az osztály átlagos magassága {round(atlag)} cm.")

# Hány cm magas a legalacsonyabb diák?
min_index = 0
i = 1
while i < len(magassagok):
    if magassagok[min_index] > magassagok[i]:
        min_index = i
    i += 1

print(f"A legalacsonyabb diák {magassagok[min_index]} cm magas. A lista {min_index}. indexén található.")

# Van-e 2 métertől magasabb diák az osztályban?

van_magasabb = False
i = 0
while i < len(magassagok):
    if magassagok[i] > 200:
        van_magasabb = True
        break
    i += 1

if van_magasabb:
    print("Van 2 métertől magasabb tanuló.")
else:
    print("Nincs 2 métertől magasabb tanuló.")
