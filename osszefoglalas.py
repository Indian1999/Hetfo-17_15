import math

print("Hello World!")
print("Hello", "World", "Hola", "Mundo", sep=" ", end="!\n")
print("""Ezzel tudok
Szépen több sorba
kiirogatni dolgokat
\tezzel meg így akár tabolni
\tis tudok""")

# Számoljuk ki egy Kúp térfogatát:
# alapterület * magasság / 3
# alapterület = sugár^2  * pi
sugár = 3#int(input("Add meg a kúp sugarát: "))
magasság = 3#int(input("Add meg a kúp magasságát: "))
térfogat = (sugár**2 * math.pi) * magasság / 3
print(f"A kúp térfogata: {round(térfogat, 2)}")

# Két változó értékének megcserélése:
a = 12 
b = 20
print(f"a = {a}, b = {b}")

# Első opció: Minden nyelven működik
temp = a # Elmentem ide az a változó eredeti értékét
a = b
b = temp

print(f"a = {a}, b = {b}")

# Második opció:
a, b = b, a

print(f"a = {a}, b = {b}")

# 4. feladat: string műveletek

szamok = "4,3,2,3,5,5,39,3,5,3,5,6,7,4,34,5,6,54,5,34,43,5,54" #input("Adj meg számokat, vesszővel elválasztva:")
szamok = szamok.replace(" ", "")
lista = szamok.strip().split(",")  # ["5", "6", "32"]
for i in range(len(lista)):
    lista[i] = int(lista[i])
print(lista)

# 5. feladat: Válogassuk szét a listát, páros és páratlan listákra

paros_lista = []
paratlan_lista = []
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        paros_lista.append(lista[i])
    else:
        paratlan_lista.append(lista[i])
print(f"Páros számok: {paros_lista}")
print(f"Páratlan számok: {paratlan_lista}")

# 6. feladat:
nevek = ["András", "Béla", "Cecil", "Dóra", "Elemér", "Fanni", "Gábor", "Hanna"]
kártyák = [32, 19, 41, 9, 88, 70, 1, 59]
print(nevek)
print(kártyák)

# Átlagosan hány kártyája van egy embernek?

# Kinek van a legtöbb kártyája (és mennyi)?

# Készítsünk 2 új listát, az egyikben azoknak a nevei legyen, akiknek az átlagtól kevesebb,
# a másikban azok nevei akiknek az átlagtól több kártyájuk van.

# Kik azok akiknek a kártyáit egyenlően el- lehet osztani 4 felé?
print("Azok az emberek akiknek a kártyáit 4 felé lehet osztani:")
for i in range(len(nevek)):
    if kártyák[i] % 4 == 0:
        print(nevek[i])

# Hány kártyájuk van a lányoknak összesen?
lányok = ["Cecil", "Dóra", "Fanni", "Hanna"]

lányok_összeg = 0
for i in range(len(nevek)):
    if nevek[i] in lányok:
        lányok_összeg += kártyák[i]

print(f"A lányoknak összesen {lányok_összeg} kártyájuk van.")