# Feladat: Olvassunk be számokat, egész addig, amíg a felhasználó üres
# stringet nem ír be, és utána tároljuk el egy listába.

lista = []
while True:
    szam = input("Adj meg egy egész számot: ") # "32"
    if szam.isdigit():
        lista.append(int(szam))
    else:
        break
    print(lista)

# Az elemek összegét
összeg = 0
for i in range(len(lista)):
    összeg += lista[i]
print(f"A lista elemeinek az összege: {összeg}")

# Írjuk ki ennek a listának az átlagát
atlag = összeg / len(lista)
print(f"A lista elemeinek az átlaga: {round(atlag, 2)}")

# Páros számok számát

# A legnagyobb/legkisebb elemet, terjedelmet ( max - min)

# módusz
max_index = 0
max_value = 0
for i in range(len(lista)):
    szamlalo = 0
    for j in range(len(lista)):
        if lista[i] == lista[j]:
            szamlalo += 1
    if szamlalo > max_value:
        max_value = szamlalo
        max_index = i
modusz = lista[max_index]
print(f"Módusz: {modusz}")

# Az adatok szórását

négyzet_összeg = 0
for i in range(len(lista)):
    négyzet_összeg += (lista[i] - atlag)**2

szoras = (négyzet_összeg / len(lista))**0.5   # 0.5. hatvány = gyökvonás
print(f"Szórás: {round(szoras, 2)}")

# Medián, alsó felső kvartilis
def median(lista):
    lista.sort() # rendezi a listát
    if len(lista) % 2 == 0: # páros elemszám
        # pl.: 10 hosszú lista esetén a 4. és 5. index kell
        szam1 = lista[len(lista) // 2]
        szam2 = lista[len(lista) // 2 - 1]
        return (szam1 + szam2) / 2
    else:
        # pl.: ha 7 hosszú a lista, akkor a 3. index kell
        return lista[len(lista) // 2]
    
print(f"Medián: {median(lista)}")
first_half = sorted(lista)[:len(lista) // 2]
second_half = sorted(lista)[len(lista) // 2:]
print(f"Alsó kvartilis: {median(first_half)}")
print(f"Felső kvartilis: {median(second_half)}")


# Task 2 - removing duplications from list

# Task 3 - extend command

# Task 4 - find integers in list

# Task 5 - largest gap in a list

# Task 6 - largest and second largest numbers

# Task 7 - sorting a list
