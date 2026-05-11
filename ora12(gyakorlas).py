# Feladat: Olvassunk be számokat, egész addig, amíg a felhasználó üres
# stringet nem ír be, és utána tároljuk el egy listába.

lista = []
while True:
    break
    szam = input("Adj meg egy egész számot: ") # "32"
    if szam.isdigit():
        lista.append(int(szam))
    else:
        break
    print(lista)
lista = [1,2,3,4,5]
# Az elemek összegét
összeg = 0
for i in range(len(lista)):
    összeg += lista[i]
print(f"A lista elemeinek az összege: {összeg}")

# Írjuk ki ennek a listának az átlagát
atlag = összeg / len(lista)
print(f"A lista elemeinek az átlaga: {round(atlag, 2)}")

# Páros számok számát
páros_darab = 0
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        páros_darab += 1
print(f"Páros számok számára: {páros_darab}")

# A legnagyobb/legkisebb elemet, terjedelmet ( max - min)
max_index = 0
min_index = 0
for i in range(len(lista)):
    if lista[i] > lista[max_index]:
        max_index = i
    if lista[i] < lista[min_index]:
        min_index = i
maximum = lista[max_index]
minimum = lista[min_index]
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Terjedelem: {maximum - minimum}")

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


# Feladat: Adott egy lista, ha egy elem többször szerepel a listában, akkor vegyük ki a duplikációt

lista = [4, 9, 1, 2, 2, 1, 9, 8, 6, 7, 2, 3, 6, 3, 1, 2, 7, 9]
halmaz = []
for i in range(len(lista)):
    if lista[i] not in halmaz:
        halmaz.append(lista[i])
print(halmaz)

# Extend függvény
# Feladat, adott két lista, füzzük össze őket
lista1 = [1,2,3]
lista2 = [4,5,6]   # -> [1,2,3,4,5,6]

lista = lista1[:]
lista.append(lista2)
print(lista) # [1, 2, 3, [4, 5, 6]]

lista = lista1[:]
lista.extend(lista2) # Nem muszáj hogy a lista2 lista legyen 
print(lista) # [1, 2, 3, 4, 5, 6]

lista = lista1 + lista2 # Ha mind a kettő lista
print(lista) # [1, 2, 3, 4, 5, 6]

lista = [1,2, 3]
lista.extend((4,5,6))
lista.extend("kiskutya")
print(lista)

# print([1,2,3] + "kiskutya") ERROR

