import sys

def glavniMeni():
    print()
    print(''' LISTA ZA TRGOVINU

Odaberite broj za ono što želite napraviti:
1. Pogledaj listu.
2. Dodaj namirnicu na listu.
3. Makni namirnicu sa liste.
4. Provjeri ako je namirnica na listi.
5. Provjeri koliko je namirnica na listi.
6. Isprazni listu.
7. Izađi
''')

odabir=input("Odaberi:")
if odabir == "1":
    pass
elif odabir== "2":
    pass
elif odabir== "3":
    pass
elif odabir== "4":
    pass
elif odabir== "5":
    pass
elif odabir== "6":
    pass
elif odabir== "7":
    sys.exit()
else:
    print("Niste izabrali validnu opciju.")

lista_trgovina=["jagoda", "lubenica", "jabuka", "mrkva", "rajčica", "čokolada"]
glavniMeni()




