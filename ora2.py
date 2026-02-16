name = "John Doe"
city = "Budapest"
profession = 'software developer'
story = "A cica felmászott a fára, de most nem tud lejönni..."

print(f"A '{city}' karakterláncban {len(city)} karakter szerepel.")
print(f"A '{name}' karakterláncban {len(name)} karakter szerepel.")

print(profession.split(" ")) # ['software', 'developer']
print(profession.split('e')) # ['softwar', ' d', 'v', 'lop', 'r']

# " = '
print(f"A '{profession}' karakterlánc {profession.count(' ') + 1} szóból áll.")
print(f"A '{story}' karakterlánc {story.count(' ') + 1} szóból áll.")

print(city.find("p")) # 4, mert a 4. karakter az első p betű a 'Budapest' szövegben
print(city.find("b")) # -1
print(city.find("B")) # 0
print(city.find("ape")) # 3
print(profession.find('e')) # 7 'software developer'

# String függvények eldöntendő kérdésekre:
print(city.startswith('a')) # False
print(city.startswith("B")) # True
print(city.endswith('t')) # True
print(city.endswith("T")) # False

#age = input("Add meg az életkorod: ")
age = "32"
if age.isdecimal(): # Egész szám van-e a stringben
    age = int(age)
    print(f"{2026-age}-ben születtél.")
else:
    print("Hahó! Ez nem egy szám!")

print("57".isnumeric()) # True
print("57.32".isnumeric()) # False
print("A13B".isnumeric()) # False

print("sadasd".isalpha()) # True
print("sada32sd".isalpha()) # False
print("asdasd".isupper()) # False
print("asdasd".islower()) # True


print("szia".upper())           # SZIA
print("szia".capitalize())      # Szia
print("a cica és a fa".title()) # A Cica És A Fa
print("SzIa".lower())           # szia


story = "A cica felmászott a fára, de most nem tud lejönni..."

# Számoljuk meg, hogy hány a betű van a szövegben.
story_lower = story.lower()
#print(story_lower)
print(f"A story-ban {story_lower.count('a')} 'a' betű szerepel.")



# 1. feladat: Kérj be a felhasználótól egy nevet, majd írd, ki hogy hány karakterből áll.
#name = input("Add meg a neved: ")
print(f"A neved {len(name)} karakterből áll")

# 2. feladat: Kérj be egy mondatot, és számold meg, hogy hány szóból áll
#mondat = input("Írj egy mondatot: ")
mondat = "sad"
print(f"A mondatod {mondat.count(' ') + 1} szóból áll.")

# 3. feladat: Kérj be egy számot és írd ki az ötszörösét! Ha nem számot írt be a felhasználó, ne crasheljen ki a program!

#number2 = input("Adj meg egy számot:")
number2 = "32"
if number2.isdecimal():
   number2 = int(number2)
   print(5*number2)
else:
    print("Ez nem egy szám!")

# 4. feladat: Kérj be egy e-mail címet, és döntsd el, hogy megfelelő-e!
# Tartalmaznia kell '@' és '.'
# betűvel kell kezdődnie és végződnie is
#email = input("Add meg az emailedet: ")
email = "asd@asd.hu"
if email.find("@") != -1 and email.find(".") != -1 and email[0].isalpha() and email[-1].isalpha():
    print("Jó e-mail cím.")
else:
    print("Rossz e-mail cím")

# 5. feladat: Kérj be egy mondatot és számold meg, hogy hány 'e' betűvel kezdődő szó van benne!

mondat = "Eme hely neve Epres eredmények kertje, melnyek helye Debrecen, eme elme eleresztette ezt."
mondat = mondat.lower()
e_szo = mondat.count(" e")
if mondat.startswith("e"):
    e_szo += 1
print(e_szo)

###########################
#       ELÁGAZÁSOK        #
###########################

# if, elif, else

if 8 > 3:
    print("Bizony, a 8 nagyobb mint a 3.")
else:
    print("A 8 nem nagyobb mint a 3")

a = 0
if a > 0:
    print(f"{a} egy pozitív szám.")
elif a < 0:
    print(f"{a} egy negatív szám.")
else:
    print(f"{a} = 0")
