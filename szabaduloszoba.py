"""
-1: log
10: Kijárat
6, 7, 13, 14: Oroszlán  -> 4
2, 4, 12: villannykörték -> 6
3, 8, 11: cica, bohóc   -> 8
5, 9: Bináris egyenlet  -> 6
"""

gameOn = True
rooms = []
items = []
solution = "4686"
win = False
chances = 3
correct_switches = "1010011"
switches = "0000000"

print("""Üdvözöllek a szabadulószobában! 14 ajtót látsz magad előtt, ezek küzül
az egyik rejti a szabadságod kapuját. Találd ki a 4 számjegyű kódot, amivel ki
tudsz innen jutni. Sok sikert!""")

while gameOn:
    room_number = input("Melyik ajtón szeretnél bemenni? (1-14, -1)\n")

    if room_number == "-1":
        print("Az eddigi történeted:")
        for i in range(len(rooms)):
            print(f"{rooms[i]}. szoba: {items[i]}")

    if room_number == "1":
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("Furcsa történet")
        print("""Egy könyvet találsz, amiben a következő történet szerepel:
    A boldog kis oroszlán egy napon elment villanykörtét venni, de útközben megállította egy
gonosz bohóc a csatlós kiscicáival. Az oroszlán nagyon megijedt, de eszébe jutott egy bináris egyenlet,
amit annyira nem értett a bohóc hogy sírva fakadt. Amíg nem figyelt, az oroszlán el tudott menekülni és
boldogan élt míg meg nem halt. Itt a vége fuss el véle.""")

    if room_number == "2":
        print(f"Ebben a szobában a következő számsorozatot látod a falra írva: {correct_switches}")
        if room_number not in rooms:
            rooms.append(room_number)
            items.append(f"Számok a falon: {correct_switches}")

    if room_number == "3":
        print("""A szobába belépve egy projektort találsz ami egy videót vetít ki a falra. A videón az
látható, hogy egy csapat cica egy jó nagy tálból eszeget. Figyelmesen megnézve a képsorozatot azt veszed
észre, hogy a macskák tálján egy 2-es számjegy van kirajzolva.""")
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("Cicák esznek 2-es tálból")

    if room_number == "4":
        if switches == correct_switches:
            print("A táblán lévő villanykörték egy 6-os alakzatot formálnak.")
            item = "6-os villanykörték"
            if item not in items:
                rooms.append(room_number)
                items.append(item)
        else:
            print("Egy táblát találsz villanykörtékkel, de nem világít mindegyik, különös...")
            if room_number not in rooms:
                rooms.append(room_number)
                items.append("Tábla villanykörtékkel")

    if room_number == "5":
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("x = 111011 - 110101")  # 59 - 53 = 6
        print("""Egy osztályterembe lépsz, ahol a táblán a következő egyenlet van felírva:
            x = 111011 - 110101""")

    if room_number == "6":
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("Oroszlán")
        if "4-es számjegy" in items:
            print("Az oroszlán még mindig a húst majszolgatja.")
        else:
            print("""Egy hatalmas oroszlán van a szobában és nagyon úgy néz ki, mintha valami fontosat őrizne.""")
            ans = input("Be merészelsz lépni az oroszlán szobájába? (igen/nem)\n")
            if ans == "igen":
                if "Hús" in items:
                    print("""A dobozban talált húst odadobod az oroszlánnak, ő pedi félrevonul megenni.
Azt veszed észre, hogy egy vázát őrzött amin egy 4-es számjegy szerepel.""")
                    rooms.append(room_number)
                    items.append("4-es számjegy")
                else:
                    print("Ez igen nagy hiba volt, az oroszlán azon nyomban felfal téged.")
                    win = False
                    gameOn = False
            else:
                print("Majd legközelebb...")

    if room_number == "7":
        if room_number not in rooms:
            print("""Ez a szoba szinte teljesen üres, csak egy balta van a falnak támasztva.
Elrakod, biztos jól fog még jönni...""")
            rooms.append(room_number)
            items.append("Balta")
        else:
            print("A szoba kong az ürességtől. Itt volt a balta.")

    if room_number == "8":
        print("""Ebben a szobában egy csomó festmény van. A legtöbb csak valami absztrakt kriksz-kraksz, de
az egyik kép elég furcsa, egy bohócot ábrázol az ijesztő mosolyával, ahogyan egy absztrakt képet fest miközben
a másik kezében 3 színes héliumos lufit tart.""")
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("Bohóc festmény 3 lufival")

    if room_number == "9":
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("Binárisból decimálisba")
        print("""A szobában egy cetlit találsz amire ennyi van írva:
              \"Válts binárisból decimálisba, hogy megleld az x faktort!\"""")
        
    if room_number == "10":
        print("""Ez az ajtó vezet a külvilágba, ha helyesen megadod a 4 számjegyű
kódot, akkor ki tudsz szabadulni, de vigyázz, mert ha háromszor elhibázod
örökre itt ragadsz!""")
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("Kijárat")
        tipp = input("Szeretnél most próbálkozni? (igen/nem)\n")
        if tipp == "igen":
            code = input("Add meg a 4 számjegyet (pl.: 1234): ")
            if code == solution:
                gameOn = False
                win = True
                break
            else:
                print("Helytelen kód!")
                chances -= 1
                if chances == 0:
                    gameOn = False
                    break
                print(f"Még {chances} próbálkozásod maradt.")
        else:
            print("Akkor majd legközelebb.")

    if room_number == "11":
        print("""A szobába belépve egy számítógépet találsz. Bekapcsolod és megnézed, hogy van-e rajta valami érdekes.
Az asztal szinte teljesen üres, csak az alap ikonok vannak rajta, de találsz egy videó fájlt amit meg is nyitsz.
A videón egy olyan jelenet látható ahol egy cirkuszban 2 bohóc próbál elkapni egy fürge kiscicát.""")
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("Videó: 2 bohóc kerget egy kiscicát")

    if room_number == "12":
        print(f"{len(correct_switches)} darab kapcsolót találsz a szobában egymás mellett elhelyezve, de látszólag nem csinálnak semmit.")
        if room_number not in rooms:
            rooms.append(room_number)
            items.append(f"{len(correct_switches)} kapcsoló")
        switches = input("Add meg, hogy milyen sorrendben akarod felkapcsolni a kapcsolókat (pl.: 1010101)\n")
    
    if room_number == "13":
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("Rozoga láda")
        if "Lezárt doboz" in items:
            print("Ebben a szobában már csak a láda deszkái vannak amit szétvertél.")
        else:
            if "Balta" in items:
                print("""A korábban talált baltád segítségével szétvered a rozoga ládikót.
A láda darabjainak félresöprése után találsz egy kulcsra zárt dobozt.""")
                rooms.append(room_number)
                items.append("Lezárt doboz")
                if "Kulcs" in items:
                    print("A korábban talált kulccsal kinyítod a ládát, és egy szelet húst találsz benne.")
            else:
                print("""Olyan mintha lenne valami fontos a ládában, de nem tudod kinyitni,
lehet valamelyik szobában találsz rá egy megoldást...""")
    
    if room_number == "14":
        if room_number not in rooms:
            print("""Ez a szoba kukk sötét, kapcsolgatod a villanyt de nem történik semmi. Odasétálsz
a villanykörtéhez, hogy megpróbáld megjavítani, de ahogy kicsavarod a foglalatból véletlen elejted.
A villanykörte széttörik de te valamilyen okból kifolyólag elkezdessz tapogatózni a szilánkok között.
Jól megvágod a kezed, de a szilánkok között találsz egy kulcsot.""")
            rooms.append(room_number)
            items.append("Kulcs")
            if "Lezárt doboz" in items:
                print("A kulccsal megkísérled kinyítni a korábban talált lezárt dobozt és egy szelet húst találsz benne.")
                rooms.append(room_number)
                items.append("Hús")
        else:
            print("Még mindig sötét a szoba, de cserébe még mostmár szilánkos az utóbbi látogatásod miatt.")

if win:
    print("Kijutottál! Szép volt!")
else:
    print("Hát ez most nem jött össze... Vesztettél!")