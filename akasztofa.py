
letters = "öüóqwertzuiopőúűasdfghjkléáíyxcvbnm"
capital_letters = letters.upper()

puzzle = "Brian's life"
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
    print("Élererő:", life)
    print(my_solution)
    tipp = input("Tippelj egy karaktert: ")

    found_letter = False
    for i in range(len(puzzle)):
        if puzzle[i] == tipp:
            my_solution[i] = puzzle[i]
            found_letter = True

    
