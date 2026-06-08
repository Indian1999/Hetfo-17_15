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
        pass
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
        pass
    if room_number == "6":
        pass
    if room_number == "7":
        pass

    if room_number == "8":
        print("""Ebben a szobában egy csomó festmény van. A legtöbb csak valami absztrakt kriksz-kraksz, de
az egyik kép elég furcsa, egy bohócot ábrázol az ijesztő mosolyával, ahogyan egy absztrakt képet fest miközben
a másik kezében 3 színes héliumos lufit tart.""")
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("Bohóc festmény 3 lufival")

    if room_number == "9":
        pass

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
        pass
    if room_number == "14":
        pass

if win:
    print("Kijutottál! Szép volt!")
else:
    print("Hát ez most nem jött össze... Vesztettél!")