# Elágazások

szam1 = 18
szam2 = 35

if szam1 > 10:
    print("Hűha, ez egy nagy szám.")

if szam2 > 10:
    print(f"Hűha a {szam2} egy nagy szám!")

if szam1 > 10:
    print(f"Hűha a {szam1} egy nagy szám!")
else:
    print(f"{szam1} egy pici szám!")

# Feladat: Írjunk egy programot ami beolvas 2 számot és eldönti, hogy melyik a nagyobb.

szam1 = 34 #int(input("Add meg az első számot: "))
szam2 = 12 #int(input("Add meg a második számot: "))

if szam1 > szam2:
    print(f"{szam1} a nagyobb")
elif szam2 > szam1:
    print(f"{szam2} a nagyobb")
else:
    print(f"A két szám egyenlő")

# Írjunk egy programot ami eldönti egy számról, hogy hány számjegyből áll

szam = 12 # int(input("Adj meg egy számot: "))

if szam < 10:
    print("Egy számjegyű")
elif szam < 100:
    print("Két számjegyű")
elif szam < 1000:
    print("Három számjegyű")
elif szam < 10000:
    print("Négy számjegyű")
elif szam < 100000:
    print("Öt számjegyű")
elif szam < 1000000:
    print("Hat számjegyű")
else:
    print("Hát ez nagyon sok számjegy....")

# Kicsit okosabb megoldás:
szam = "123" #input("Adj meg egy számot: ")  # pl.: "123"
print(f"{len(szam)} számjegyből áll.")

# Feladat: Olvassuk be egy háromszög 3 oldalának a hosszát.
print("Add meg a háromszög oldalainak a hosszát:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

# a, Döntsük el, hogy szerkeszthető-e a háromszög!
# b, Ha szerkeszhető, nézzük meg, hogy milyen háromszög
# (egyenlő szárú, szabályos, derékszögű)

if a + b > c and a + c > b and b + c > a:
    print("Szerkeszthető a háromszög.")
    if a == b and b == c:
        print("Szabályos háromszög")
    elif a == b or b == c or a == c:
        print("Egyenlő szárú háromszög")
    
    print("a**2 + b**2 =", a**2 + b**2)
    print("c**2 =", c**2)
    if a*a + b*b == c*c or b*b + c*c == a*a or a**2 + c**2 == b**2:
        print("Derékszögű háromszög")
    if round(a**2 + b**2, 14) == round(c**2, 14):
        print("Derékszögű háromszög (kerekítéssel)")
    if round(a**2 + c**2, 14) == round(b**2, 14):
        print("Derékszögű háromszög (kerekítéssel)")
    if round(c**2 + b**2, 14) == round(a**2, 14):
        print("Derékszögű háromszög (kerekítéssel)")

else:
    print("Ilyen háromszög nem szerkeszthető.")
