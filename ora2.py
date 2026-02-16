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

# 2. feladat: Kérj be egy mondatot, és számold meg, hogy hány szóból áll

# 3. feladat: Kérj be egy számot és írd ki az ötszörösét! Ha nem számot írt be a felhasználó, ne crasheljen ki a program!

# 4. feladat: Kérj be egy e-mail címet, és döntsd el, hogy megfelelő-e!
# Tartalmaznia kell '@' és '.'
# betűvel kell kezdődnie és végződnie is

# 5. feladat: Kérj be egy mondatot és számold meg, hogy hány 'e' betűvel kezdődő szó van benne!