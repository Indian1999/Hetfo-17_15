# Készítsünk egy átváltó programot, amely különböző mértékegységek között vált.
# g - kg
# km - mi   (1 km = 0.62137 mi)
# C° - F°   (F° = (C° * 1.8) + 32)

print("Milyen mértékegységet szeretnél váltani?")
print("1: gramm - kilogramm")
print("2: kilométer - mérföld")
print("3: Celsius - Fahrenheit")
mode = input("Add meg a menüpont számát: ")

if mode == "1":
    print("Miből mibe szeretnél váltani?")
    print("1: Grammból Kilogrammba")
    print("2: Kilogrammból Grammba")
    mode2 = input("Add meg a menüpont számát: ")
    if mode2 == "1":
        gramm = float(input("g = "))
        print(f"{gramm} g = {gramm / 1000} kg")
    elif mode2 == "2":
        kg = float(input("kg = "))
        print(f"{kg} kg = {kg * 1000} g")
    else:
        print("Érvénytelen menüpont")
elif mode == "2":
    print("Miből mibe szeretnél váltani?")
    print("1: Kilométerből mérföldbe")
    print("2: Mérföldből kilométerbe")
    mode2 = input("Add meg a menüpont számát: ")
    if mode2 == "1":
        km = float(input("km = "))
        print(f"{km} km = {km * 0.62137} mi")
    elif mode2 == "2":
        mi = float(input("mi = "))
        print(f"{mi} mi = {mi / 0.62137} km")
    else:
        print("Érvénytelen menüpont")
elif mode == "3":
    print("Miből mibe szeretnél váltani?")
    print("1: C°-ból F°-be")
    print("2: F°-ből C°-ba")
    mode2 = input("Add meg a menüpont számát: ")
    if mode2 == "1":
        c = float(input("C° = "))
        print(f"{c} C° = {c*1.8 + 32} F°")
    elif mode2 == "2":
        f = float(input("F° = "))
        print(f"{f} F° = {(f-32)/1.8} C°")
    else:
        print("Érvénytelen menüpont")
else:
    print("Érvénytelen menüpont!")