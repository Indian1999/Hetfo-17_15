print("Hello Világ!")

name = "John Doe"

print(name) # John Doe
print(type(name)) # <class 'str'> string típusú (karakterlánc / szöveg)

print("Hello", name, "!") # Hello John Doe !
# "Hello" + "John Doe" + "!" -> "HelloJohn Doe!"
print("Hello " + name + "!") # Hello John Doe!
print(f"Hello {name}!") # Hello John Doe!
print("Hello {name}!") # Hello {name}! 

age = 37
hourly_wage = 18.3
married = True

print(age)                  # 37
print(type(age))            # <class 'int'> Integer (Egész szám)
print(hourly_wage)          # 18.3
print(type(hourly_wage))    # <class 'float'> Floating point unit (Lebegőpontos szám)
print(married)              # True
print(type(married))        # <class 'bool'> Boolean - Logikai érték (True/False)

print("Szia " + name + "!")
#print(age + " éves vagy.") # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# Hiba oka, stringet és intet nem lehet összeadni    5 + "kiscica" = TYPE ERROR
# str(age) = "37"   string típusú
print(str(age) + " éves vagy.")  # str + str -> str
print("Az órabéred " + str(hourly_wage) + " $.")
print("Házas: " + str(married)) # Házas: True

if married:
    print("Házas vagy.")
else:
    print("Hajadon vagy.")



