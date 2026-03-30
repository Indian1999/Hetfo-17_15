import random

puzzles = [
    "Harry Potter", "Gyűrűk ura", "Trónok harca", "Breaking Bad", "Stranger Things",
    "Walking Dead", "Csillagok között", "Eredet film", "Sötét lovag", "Vissza jövőbe",
    "Karib tenger kalózai", "Jurassic Park", "Reszkessetek betörők", "Fekete párduc",
    "Doktor Strange", "Vasember film", "Amerika kapitány", "Thor Ragnarok",
    "Pókember hazatérés", "Bosszúállók végjáték",

    "matematika", "informatika", "történelem", "földrajz óra", "biológia óra",
    "kémia labor", "fizika óra", "irodalom óra", "nyelvtan óra", "angol nyelv",
    "német nyelv", "programozás", "algoritmusok", "adatbázisok", "mesterséges intelligencia",

    "asztalos munka", "villanyszerelő", "gépészmérnök", "szoftverfejlesztő",
    "rendszergazda", "marketinges szakember", "pénzügyi tanácsadó", "építészmérnök",
    "grafikus tervező", "projektmenedzser", "adatkutató szakember", "orvosi asszisztens",
    "gyógyszerész szakma", "állatorvos szakma", "tanár pedagógus",

    "kalapács szerszám", "csavarhúzó készlet", "számítógép egér", "billentyűzet mechanikus",
    "monitor kijelző", "fejhallgató vezetékes", "okostelefon készülék",
    "televízió készülék", "mikrohullámú sütő", "hűtőszekrény nagy", "mosógép automata",
    "porszívó készülék", "kávéfőző gép", "kenyérpirító gép", "vízforraló készülék",

    "Minecraft", "Fortnite battle royale", "Counter Strike Global Offensive",
    "League of Legends", "Call of Duty Modern Warfare", "Grand Theft Auto",
    "Red Dead Redemption", "The Witcher Wild Hunt", "Cyberpunk 2077",
    "Assassins Creed Odyssey", "Battlefield", "Overwatch",
    "Dota Underlords", "Valorant shooter", "Apex Legends battle",

    "Barátok közt", "Szomszédok", "Dr House",
    "Agymenők", "Modern család", "Vészhelyzet",
    "Dexter", "Narcos",
    "Better Call Saul", "Sherlock",
    "WandaVision", "The Mandalorian", "House of Cards",

    "csokoládé torta", "eperlekvár házi", "narancslé frissen", "almafa ültetés",
    "kertészkedés hobbi", "virágcsokor ajándék", "karácsonyfa díszítés",
    "születésnapi buli", "nyaralás tengerpart", "kirándulás hegyekben",

    "oktatási platform", "digitális tanulás", "online kurzusok", "videós tartalom",
    "mobil alkalmazás", "webfejlesztés alapjai", "frontend fejlesztés",
    "backend fejlesztés", "adatvizualizáció", "felhőszolgáltatás",

    "közösségi média", "tartalomgyártás", "videószerkesztés", "fotószerkesztés",
    "grafikai tervezés", "animáció készítés", "hangszerkesztés program",
    "zeneprodukció alapok", "podcast készítés", "streaming szolgáltatás",

    "sporttevékenység", "labdarúgás játék", "kosárlabda edzés",
    "kézilabda mérkőzés", "úszás technika", "futóverseny maraton",
    "kerékpározás túra", "hegymászás kaland", "síelés téli sport",

    "pénzügyi tervezés", "befektetési stratégia", "költségvetés készítés",
    "vállalkozás indítás", "üzleti modell tervezés", "startup fejlesztés",
    "piackutatás módszertan", "értékesítési stratégia", "marketing kampány",

    "utazási iroda", "repülőjegy foglalás", "szállásfoglalás online",
    "turisztikai látványosság", "városnézés program", "idegenvezetés szolgáltatás",

    "egészséges életmód", "táplálkozási tanácsadás", "fitnesz edzésprogram",
    "jóga gyakorlatok", "meditáció technika", "mentális egészség",

    "környezetvédelem", "újrahasznosítás program", "fenntartható fejlődés",
    "klímaváltozás hatásai", "zöld energia forrás", "napenergia rendszer",

    "autóvezetés tanfolyam", "jármű karbantartás", "közlekedési szabályok",
    "biztonsági öv használat", "vezetési gyakorlat", "parkolási technika",

    "tudományos kutatás", "laboratóriumi vizsgálat", "kísérleti eredmények",
    "publikáció készítés", "akadémiai tanulmány", "kutatási módszertan"
]

letters = "öüóqwertzuiopőúűasdfghjkléáíyxcvbnm"
capital_letters = letters.upper()

puzzle = random.choice(puzzles)
my_solution = ""

for char in puzzle:
    if char in letters or char in capital_letters:
        my_solution += "*"
    else:
        my_solution += char

life = 10
correct = []
incorrect = []

while life > 0 and puzzle != my_solution:
    print()
    print("Élererő:", life)
    print(my_solution)
    tipp = input("Tippelj egy karaktert: ")

    if len(tipp) != 1:
        print("Egy betűt (karaktert) adj meg!")
        continue # A következő ciklus iterációra ugrik

    if tipp in correct or tipp in incorrect:
        print("Ezt a betűt már próbáltad!")
        continue

    if not tipp.lower() in letters:
        print("Ez nem egy betű. Mindenképpen betűt tippelj!")
        continue

    found_letter = False
    for i in range(len(puzzle)):
        if puzzle[i].lower() == tipp.lower():
            my_solution = my_solution[:i] + puzzle[i] + my_solution[i+1:]
            found_letter = True

    if found_letter:
        correct.append(tipp)
    else:
        incorrect.append(tipp)
        life -= 1
        print(f"Helytelen betű! {life} életed maradt.")
    print("Helyes betűk:", correct)
    print("Helytelen betűk:", incorrect)

if life > 0:
    print(f"Gratulálok! {len(correct) + len(incorrect)} lépésből kitaláltad, hogy a megoldás: '{puzzle}'")
else:
    print(f"Ez most nem jött össze. A megoldás '{puzzle}' volt.")

    
