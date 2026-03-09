import random

# Ciklusok
# Egy kód részletet bizsonyos alkalommal ismétlünk

# Elől tesztetlős ciklus (while)
# Amíg a feltétele igaz, ismétel

i = 1
while i < 10:
    print(i)
    i += 1

# feladat: Olvassunk be számokat a felhasználótól, egészen addig, amíg 
# üres stringet nem ad meg a felhasználó.
# Üres string megadása után, írjuk ki a számok átlagát

bemenet = input("Adj meg egy számot: ")
összeg = 0
darab = 0
while bemenet != "":
    összeg += int(bemenet)
    darab += 1
    bemenet = input("Adj meg egy számot: ")

if darab != 0:
    print(f"A számok átlaga: {összeg/darab}")

# Számoljuk meg hogy egy szám hány számjegyből áll!

num = 909632578324915234971253941659321653219238491
szamlalo = 0
while num != 0:
    num //= 10
    szamlalo += 1

print(szamlalo, "db számjegy")

#################################
#      SZÁMKITALÁLÓS JÁTÉK      #
#################################

# Gondoltam egy számra 1 és 100 között

print("Gondoltam egy számra 1 és 100 között. Találd ki mire gondoltam!")
num = random.randint(1, 100)
life = 7
print("7-szer tippelhetsz.")
tipp = int(input("Tippelj egy számot: "))

while tipp != num:
    if tipp > num:
        print("Ettől kisebb számra gondoltam!")
    if tipp < num:
        print("Ettől nagyobb számra gondoltam!")
    life -= 1
    if life == 0:
        break         # Kilép a ciklusból
    print(f"Még {life} tipped maradt!")
    tipp = int(input("Tipllej egy számot: "))

if tipp == num:
    print("Eltaláltad!")
else:
    print("Vesztettél!")


# A Fibonacci sorozat:

# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

n = int(input("Az első hány db fibonacci számot adjam meg? "))

szamlalo = 2
a = 1
b = 1

print(a, b, end=" ")
while szamlalo < n:
    print(f"{a+b}", end=" ")
    a, b = b, a+b
    szamlalo += 1
print()

# Feladat: Olvassunk be egy számot, és döntsük el, hogy prímszám-e!
# prím: csak 2 osztója van (1 és önmaga)
num = int(input("Adj meg egy számot: "))

prim = True
oszto = 2
while oszto < num:
    if num % oszto == 0:
        prim = False
    oszto += 1

if prim:
    print("Prímszám.")
else:
    print("Nem prímszám.")


