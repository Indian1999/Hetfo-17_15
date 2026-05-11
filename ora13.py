#Task 1 - Szedjük ki egy 3. listába a két lista közös elemeit (metszet)
list_1 = [61, 5, 6, 28, 87, 52, 89, 51, 86, 29, 93, 26, 99, 16, 36, 53, 47, 95, 18, 54, 62, 37, 34, 11, 75, 90, 88, 24, 72, 76, 55, 44,  3, 50, 35, 17, 94,  7, 31,100, 42, 43, 74, 83, 82,  4, 10]
list_2 = [5, 9, 62, 79, 17, 68, 54, 50, 60, 89, 29, 41, 83, 77,  3, 86, 56, 13, 26, 52, 98, 81, 82, 74, 55, 66, 92, 61, 30, 37, 57, 91,  2, 71, 93, 35, 33, 24,100, 19, 65, 95, 90, 38, 88, 31, 80, 70, 25, 39, 15, 85, 42, 94, 11, 76, 32,  7, 48]
metszet = []
for item in list_1:
    if item in list_2:
        metszet.append(item)

print(metszet)

#Task 2 - Fűzzük össze az elemeket 1 számmá
numbers = [12, 54, 812] # 1254812
num = ""
for item in numbers:
    num += str(item)
num = int(num)
print(num)

# Task 3 - A két lista legyen egyforma (ha az egyikből hiányzik egy elem ami a másokból nem, akkor adjuk hozzá)
list_1 = [43, 70, 25, 39, 15, 85, 42, 94, 11, 76, 20,  36, 48]
list_2 = [ 36, 44, 20, 96, 69, 15, 27, 14, 87, 67, 97, 43,  8, 22]
for item in list_1:
    if item not in list_2:
        list_2.append(item)

for item in list_2:
    if item not in list_1:
        list_1.append(item)

# Helyben rendezi a listákat (növekvő sorrendbe)
list_1.sort()
list_2.sort()

print(list_1)
print(list_2)


# Task 5 - price of items in a shop
items = ["apple", "book", "bread", "cheese", "chicken", "curry sauce", "doughnut", "toilet roll", "socks", "toothpaste"]
prices = [1500, 1000, 700, 1600, 1900, 600, 800, 999, 500, 550]

# Melyik az a termék amelyik a legolcsóbb? (és mennyibe kerül)
min_index = 0
for i in range(len(prices)):
    if prices[i] < prices[min_index]:
        min_index = i
print(f"A legolcsóbb termék a '{items[min_index]}', {prices[min_index]} Ft-ba kerül")

# Sorold fel azokat a termékeket amelyek több mint 1000 forintba kerülnek (az árukkal együtt)
print("Az 1000 Ft-tól drágább termékek:")
for i in range(len(prices)):
    if prices[i] > 1000:
        print(f"{items[i]} - {prices[i]} Ft")

# Írd ki, mennyit kell fizetni, ha veszek 3 zoknit, 1 sajtot, 2 kenyeret és 3 könyvet.
kosar = ["socks", "socks", "socks", "cheese", "bread", "bread", "book", "book", "book"]
vegosszeg = 0
for item in kosar:
    for i in range(len(items)):
        if item == items[i]:
            vegosszeg += prices[i]
            break    # Kilépek a ciklusból

print(f"A kosár tartalma: {kosar}")
print(f"Végösszeg: {vegosszeg} Ft.")




# Task 8 - price of the translation
string = """Mr. and Mrs. Dursley, of number four, Privet Drive, were proud to say that they were perfectly
normal, thank you very much. They were the last people you’d expect to be involved in anything
strange or mysterious, because they just didn’t hold with such nonsense.
 Mr. Dursley was the director of a firm called Grunnings, which made drills. He was a big, beefy
man with hardly any neck, although he did have a very large mustache. Mrs. Dursley was thin
and blonde and had nearly twice the usual amount of neck, which came in very useful as she
spent so much of her time craning over garden fences, spying on the neighbors. The Dursleys
had a small son called Dudley and in their opinion there was no finer boy anywhere.
 The Dursleys had everything they wanted, but they also had a secret, and their greatest fear was
that somebody would discover it. They didn’t think they could bear it if anyone found out about
the Potters. Mrs. Potter was Mrs. Dursley’s sister, but they hadn’t met for several years; in fact,
Mrs. Dursley pretended she didn’t have a sister, because her sister and her good-for-nothing
husband were as unDursleyish as it was possible to be. The Dursleys shuddered to think what the
neighbors would say if the Potters arrived in the street. The Dursleys knew that the Potters had a
small son, too, but they had never even seen him. This boy was another good reason for keeping
the Potters away; they didn’t want Dudley mixing with a child like that.
 When Mr. and Mrs. Dursley woke up on the dull, gray Tuesday our story starts, there was
nothing about the cloudy sky outside to suggest that strange and mysterious things would soon be
happening all over the country. Mr. Dursley hummed as he picked out his most boring tie for
work, and Mrs. Dursley gossiped away happily as she wrestled a screaming Dudley into his high
chair.
 None of them noticed a large, tawny owl flutter past the window.
 At half past eight, Mr. Dursley picked up his briefcase, pecked Mrs. Dursley on the cheek, and
tried to kiss Dudley good-bye but missed, because Dudley was now having a tantrum and
throwing his cereal at the walls. """

# Task 9 - getting information from a person
name = ["Bob", "Wanda", "Jared", "Emma", "Lisa", "Fred", "George", "Noah", "Rachel"]
age = [26, 31, 35, 41, 58, 30, 46, 61, 25]
gender = ["male", "female", "male", "female", "female", "male", "male", "male", "female"]
job = ["web developer", "marketing director", "content creator", "human resources", "CEO", "software developer", "public relations manager", "tester", "sales representative"]
salary = [1500, 1500, 1400, 1300, 1400, 1500, 1400, 1300, 1500]








# Task 4 - Ellenőrizzük le, hogy egy lista rendezett e (növekvő vagy csökkenő)
list = [43, 70, 25, 39, 15, 85, 42, 94, 11, 76, 20,  36, 48]

# Task 6 - 100. Fibonacci number

# Task 7 - 400m running results
names = ["Bob", "Wanda", "Jared", "Emma", "Lisa", "Fred", "George", "Noah", "Rachel"]
times = [123.42, 67.15, 80.70, 118.40, 99.95, 68.22, 71.51, 102.68, 80.88]
