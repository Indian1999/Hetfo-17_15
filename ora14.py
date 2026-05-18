# 1. feladat: Hány napos vagyok?

def is_leap_year(year):
    if year % 4 != 0:
        return False
    else:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True

now_year = 2026
now_month = 5
now_day = 18
#birth_date = input("Add meg a születési dátumod! (pl.: 1999-02-10): ")
#birth_date = birth_date.split("-") # ["1999", "02", "10"]
#birth_year = int(birth_date[0])  # 1999
#birth_month = int(birth_date[1]) # 2
#birth_day = int(birth_date[2])   # 10
birth_year = 1999
birth_month = 2
birth_day = 10

months = ["0. hónap", 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

szamlalo = 0
while not (birth_year == now_year and birth_month == now_month and birth_day == now_day):
    if birth_day == 28 and birth_month == 2 and is_leap_year(birth_year):
        birth_day += 1
    else:
        if birth_day >= months[birth_month]:
            birth_day = 1
            if birth_month == 12:
                birth_month = 1
                birth_year += 1
            else:
                birth_month += 1
        else:
            birth_day += 1
    szamlalo += 1
print(f"Ennyi napos vagy: {szamlalo}")

# Bónusz szorgalmi: 1582-ben Október 4-ét Október 15 követte.
# Kr. e. 1 -et Kr. u 1 követi (nincs 0. év)

# 2. feladat: Anagramma-e?
# pl.: racecar, görög, Indul a görög aludni.

def is_anagramm(string):
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True

def clean_text(string):
    string = string.lower()
    special = " .,?!:;>-_*'+%/=()[]{}$Ł÷\|&#@<"
    for char in special:
        string = string.replace(char, "")
    return string

print(is_anagramm("görög")) # True
print(is_anagramm("török")) # False
print(is_anagramm("Indul a görög aludni.")) # False
print(is_anagramm(clean_text("Indul a görög aludni."))) # True

# 3. feladat: Kik lassítsanak?
speed = [96, 98, 72, 64, 93, 61, 95, 78, 54, 51, 52, 55, 47, 70, 68, 67, 79, 83, 59, 76, 45, 82, 87, 66, 89, 62, 69, 74, 75, 48, 88, 81, 86, 97, 94, 71, 46, 57, 50, 53]


# 4. feladat: Szavazás eredménye
burgers = ["Spicy Pinata", "Cheesy Dream", "Vegan Fluffy", "Fatty Boom", "Tortuga", "Pork Pie"]
votes = [95061, 93439, 98563, 90478, 90915, 97334]

# Melyik burger nyerte a szavazást, hány szavazattal?
max_index = 0
for i in range(1, len(votes)):
    if votes[i] > votes[max_index]:
        max_index = i

print(f"A szavazást a {burgers[max_index]} burger nyerte, {votes[max_index]} szavazattal.")

# Átlagosan hány szavazatot kapott egy burger?
összeg = 0
for i in range(len(votes)):
    összeg += votes[i]
átlag = összeg / len(votes)
print(f"Egy burger átlagosan {round(átlag)} szavazatot kapott.")

# Melyik burger kapta a legkevesebb szavazatot? (és hányat)
min_index = 0
for i in range(1, len(votes)):
    if votes[i] < votes[min_index]:
        min_index = i

print(f"A szavazáson a {burgers[min_index]} burger kapta a legkevesebb szavazatot, {votes[min_index]}-t.")

# Melyek azok a burgerek, amelyek az átlagtól kevesebb szavazatot kaptak?
print("Az átlagtól kevesebb szavazatot kapott burgerek a következők:")
for i in range(len(votes)):
    if votes[i] < átlag:
        print(f"{burgers[i]} - {votes[i]} szavazat")
