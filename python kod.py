shopping_list = []


def show_help():
    print('Što moramo kupiti u trgovini?')
    print("""
  Unesi 'STOP' kako biš prestao unositi proizvode.
  Unesi 'POMOĆ' za dodatne informacije.
  Unesi 'PRIKAŽI' kako bi se prikazala tvoja lista.
  """)


def add_to_list(item):
    shopping_list.append(item)
    print('{} je dodano na tvoju listu!'.format(item))
    print('Na tvojoj listi se nalaze {} proizvoda.'.format(len(shopping_list)))



def show_list():
    print('Moja Lista:')
    for item in shopping_list:
        print(item)


show_help()

while True:
    new_item = input('> ')

    
    if new_item == 'STOP':
        break
    
    elif new_item == 'POMOĆ':
        show_help()
        continue
    
    elif new_item == 'PRIKAŽI':
        show_list()
        continue

    
    add_to_list(new_item)

show_list()



