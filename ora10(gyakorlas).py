# Készítsünk egy átváltó programot, amely különböző mértékegységek között vált.
# g - kg
# km - mi   (1 km = 0.62137 mi)
# C° - F°   (F° = (C° * 1.8) + 32)
"""
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


# Számoljuk ki mennyi lesz az idő x perc múlva:
# pl.: 17:57  +  100 perc -> 19:37

time = input("Add meg a kezdeti időpontot (pl.: 17:30):")    # "14:32"
duration = int(input("Hány perces legyen az időzítő? ")) # 100
time = time.split(":") # ["14", "32"]
time = int(time[0]) * 60 + int(time[1]) # 872
end_time = time + duration # 972
hour = end_time // 60
days = hour // 24 # Hány nap múlva
hour = hour % 24
minute = end_time % 60
print(f"{duration} perc elteltével ennyi lesz az idő: {days} nap múlva {hour}:{minute}")


# Collatz-sejtés

n = int(input("Add meg a kezdő számot a Collatz-sejtéshez: "))
collatz = [n]
while n != 1:
    if n % 2 == 0: # páros
        n //= 2
    else:
        n = n * 3 + 1
    collatz.append(n)
print(collatz)
"""
# Írjunk egy programot, amely leellenőrzi, hogy egy jelszó elég erős-e
# Legyen benne kis és angybetű
# Legyen benne szám és betű is
# Legyen benne különleges karakter
# Minimum 8, maximum 20 karakterből álljon

password = input("Add meg a jelszavad: ")
correct_length = len(password) >= 8 and len(password) <= 20
has_lower = False
has_upper = False
has_digit = False
has_special = False

for char in password:
    if char.islower():
        has_lower = True
    if char.isupper():
        has_upper = True
    if char in "0123456789":
        has_digit = True
    if char in ".,-;?!+_:<>#&@{}[]$×÷)(=/%)":
        has_special = True

if has_lower and has_upper and has_digit and has_special and correct_length:
    print("A jelszó elég erős")
else:
    if not correct_length:
        print("A jelszónak 8 és 20 karakter közöttinek kell lennie!")
    if not has_lower:
        print("A jelszóban szerepelnie kell kisbetűs karakternek!")
    if not has_upper:
        print("A jelszóban szereplnie kell nagybetűs karakternek!")
    if not has_digit:
        print("A jelszüban szereplnie kell számjegynek!")
    if not has_special:
        print("A jelszüban szerepelnie kell legalább 1 speciális karakternek!")