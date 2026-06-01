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
