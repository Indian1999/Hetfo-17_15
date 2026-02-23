# Szóbehelyettítgetős játék

tárgy1 = input("Mondj egy tárgyat: ")
tárgy2 = input("Monj még egy tárgyat: ")
tulajdonság = input("Mondj egy tulajdonságot: ")
zene = input("Mondj egy zenét: ")
híresség = input("Mondj egy híres embert: ")
érzés = input("Adj meg egy érzést: ")
ige = input("Mondj egy igét: ")
helyszín = input("Adj meg egy helyszínt: ")
étel = input("Mondj egy ételt: ")
személy = input("Mondj egy személyt: ")

print(f"""Most érkeztem haza egy pizza partyról {személy}-val.
Egy hihehetlenül {tulajdonság} pizzát ettünk {helyszín}-ben.
Mindenki kiválaszthatta a saját feltétjét. Én {étel} és {tárgy1} pizzát ettem.
Ezek a kedvenc feltéteim, és még a széleit is megtöltötték {tárgy2}-vel.
Ha a a hihetetlen pizza nem lett volna elég, a mellettünk lévő asztalnál
ült {híresség} aki evés közben {zene}-t énekelte nekünk.
Annyira jó volt az előadása, hogy evés közben mindketten felkeltünk és elkezdtünk
{ige}-ni. Az egész estétől {érzés} lettem. Jó lenne máskor is megismételni.""")