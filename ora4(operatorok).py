# Operátorok (Műveletek)

##########################################
#         ARITMETIKAI OPERÁTOROK         #
##########################################

print(7 + 8)   # 15
print(13 - 8)  # 5
print(3 * 7)   # 21
print(2 ** 10) # 1024
print(type(6 ** 10)) # <class 'int'>
print(type(9 ** 0.5)) # <class 'float'>
print(20 / 5)  # 4.0
print(type(20/5)) # <class 'float'>

# Egész osztás / Maradék nélküli osztás
# Eredménye mindig integer
print(20 // 5) # 4
print(74 // 5) # 14

# Maradékos osztás
print(83 % 10)   # 3
print(83.0 % 10) # 3.0

print("cica" + "kutya") # cicakutya
#print("cica" + 4) # TypeError: can only concatenate str (not "int") to str
#print("cica" * "kutya") # TypeError: can't multiply sequence by non-int of type 'str'
print("cica" * 5) # cicacicacicacicacica



##########################################
#           ÉRTÉKADÓ OPERÁTOROK          #
##########################################

# Az = jel illetve, minden ami aritmetikai plussz = jel

a = 10
print(a) # 10
a += 5
print(a) # 15
a -= 3
print(a) # 12
a *= 2
print(a) # 24
a %= 7
print(a) # 3
a **= 2
print(a) # 9
a /= 3
print(a) # 3.0
a //= 0.37
print(a) # 8.0

szöveg = "alma"
szöveg += "fa"
print(szöveg) # almafa

##########################################
#        ÖSSZEHASONLÍTÓ OPERÁTOROK       #
##########################################

# Relációs jelek
# AZ összehasonlító operátorok kinete egy bool érték (logikai érték)
# True/False
print(6 > 3) # True
print(8>=8)  # True
print(3 < 7) # True
print(3 <=2) # False
print(2==2)  # True
print(2!=2)  # False

# 'is' operátor
# A két operandusa ugyan az az objektum-e [A memóriában ugyan az az érték]
print(5 is 5)               # True
print(12345678 is 12345678) # True
print(4 is 5)               # False

lista1 = [1,2,3]
lista2 = [1,2,3]
lista3 = lista1

print("lista1:", lista1)
print("lista2:", lista2)
print("lista3:", lista3)

print(f"lista1 == lista2: {lista1 == lista2}") # True
print(f"lista1 is lista2: {lista1 is lista2}") # False

print(f"lista1 == lista3: {lista1 == lista3}") # True
print(f"lista1 is lista3: {lista1 is lista3}") # True

lista1[0] = "szia"
print(lista1) # ['szia', 2, 3]
print(lista3) # ['szia', 2, 3]


##########################################
#            AZ 'in' OPERATOR            #
##########################################

# Egy elem része-e egy adatszerkezetnek

print("a" in "almafa")  # True
print("a" in "citrom")  # False
print(5 in [1,2,3])     # False
print(5 in [4,5,6])     # True


##########################################
#           LOGIKAI OPERÁTOROK           #
##########################################

# és, vagy, nem
# and, or, not

print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False

print(True or True)   # True
print(True or False)  # True
print(False or True)  # True
print(False or False) # False

print(not True)  # False
print(not False) # True



# Az 'escape karakter' (fordított per jel)
# alt gr + Q -> \
# Az escape karakter megváltoztaja az előtte lévő karakter jelentését

# \n -> enter karakter
# \" -> "

szöveg = "Egy.\nEgy almafa." 
print(szöveg)
#Egy.
#Egy almafa.

szöveg = "Ez \"egy\" idézőjel" 
print(szöveg) # Ez "egy" idézőjel

szöveg = "Tabulátor\tvalami" 
print(szöveg) # Tabulátor       valami

szöveg = "finom\\nyami" 
print(szöveg) # finom\nyami

szöveg = "Hello\rasd" # A \r az elejére ugrik, és onnan írja az 'asd'-ot
print(szöveg) # asdlo

# 1. feladat: Jelenítsünk meg egy a * b oldalhosszúságú téglalapot

# pl.: a = 5, b = 8

# # # # # # # #
#             #
#             #
#             #
# # # # # # # #
a = int(input("a = "))
b = int(input("b = "))

sor = "# " * b + "\n" 
print(sor * a)

print("# " * b)
sor = "# " + "  "*(b-2)  + "#\n"
print(sor * (a-2), end="")
print("# " * b)

# 2. feladat: Olvassunk be egy szöveget és írjuk ki, hogy hány magánhangzó van benne.
szöveg = input("Írj egy szöveget: ")
maganhangzok = "öüóűúőoiueaéáíÓÜÖŰÚŐOIUEÁÉAÍ"

szamlalo = 0
for char in szöveg:
    if char in maganhangzok:
        szamlalo += 1
print(szamlalo, "db magánhangzó van a szövegben.")