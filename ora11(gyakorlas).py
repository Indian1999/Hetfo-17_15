# Addott egy-egy lista kereszt és vezetéknevekkel. Írjuk ki az összes lehetséges.
# vezetéknév-keresznév kombinációt.

vezetek = ["Kovács", "Kis", "Nagy", "Balogh", "Horváth"]
kereszt = ["László", "Csaba", "András", "Szilveszter", "József"]

for vez in vezetek:
    for ker in kereszt:
        print(vez + " " + ker)

# Van 8 barát, hányféle párt lehet belőlük kreálni?
# András - Béla, András - Cecil

print()
print("#"*47)
print("#" + " "*20 + "PÁROK" + " "*20 + "#")
print("#"*47)
print()

nevek = ["András", "Béla", "Cecil", "Dénes", "Elemér", "Ferenc", "Gábor", "Hanna"]

for i in range(len(nevek)):
    for j in range(i+1, len(nevek)):
        print(nevek[i] + " " + nevek[j])


# Adott két egész szám, írjuk ki a legkisebb közös töbszörösüket és
# a legnagyobb közös osztójukat

def factors(num):
    divisor = 2
    factors_list = []
    while num != 1:
        if num % divisor == 0:
            factors_list.append(divisor)
            num //= divisor
        else:
            divisor += 1
    return factors_list

def lnko(num1, num2):
    factors1 = factors(num1)
    factors2 = factors(num2)
    lnko_list = []
    for fact in factors1:
        if fact in factors2:
            lnko_list.append(fact)
            factors2.remove(fact)
    output = 1
    for factor in lnko_list:
        output *= factor
    return output

def lkkt(num1, num2):
    factors1 = factors(num1)
    factors2 = factors(num2)
    for fact in factors1:
        if fact in factors2:
            factors2.remove(fact)
    lkkt_list = factors1 + factors2
    output = 1
    for factor in lkkt_list:
        output *= factor
    return output
    
print(lnko(1024, 96))
print(lkkt(90, 210))


# Írd ki az első 50 prímszám szorzatát
# (Tipp: készíts egy is_prime(num) függvényt, ami True vagy False értékkel tér vissza)

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

primes = []

szam = 2
while len(primes) != 50:
    if is_prime(szam):
        primes.append(szam)
    szam += 1

szorzat = 1
összeg = 0
for prime in primes:
    szorzat *= prime
    összeg += prime

print(f"Az első 50 prímszám szorzata: {szorzat}") 
#19078266889580195013601891820992757757219839668357012055907516904309700014933909014729740190
print(f"Az első 50 prímszám összeg: {összeg}") # 5117

# Írj egy függvényt ami kiszámolja egy szám faktoriálisát
# 5! = 5 * 4 * 3 * 2 * 1
# n! = n * (n-1)!
# 0! = 1

def factorial(num):
    output = 1
    for i in range(1, num+1):
        output *= i
    return output

print(factorial(5)) # 120
print(factorial(52)) # 120

# Írj egy függvényt ami megadja az első n szám összegét

def sum_until(n):
    összeg = 0
    for i in range(1, n+1):
        összeg += i
    return összeg


print(f"Az első 20 természetes szám összege: {sum_until(20)}")



