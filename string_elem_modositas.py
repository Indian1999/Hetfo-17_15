szöveg = "ábécé"

szöveg += "dé"

print(szöveg)

#szöveg[2] = "x" # TypeError: 'str' object does not support item assignment

# 1. opció
szöveg = szöveg[:2] + "x" + szöveg[3:]
print(szöveg)

# 2. opció
szöveg_lista = list(szöveg)
szöveg_lista[4] = "y"
szöveg = "".join(szöveg_lista)
print(szöveg)