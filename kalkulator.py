print("1 - Dodawanie, 2 - Odejmowanie, 3 - Mnożenie, 4 - Dzielenie, 5 - Potęgowanie")

def kalkulator():
    menu = int(input("Wybierz operatora: "))
    while menu not in [1, 2, 3, 4, 5]:
        print("Nieprawidłowy operator! Wybierz ponownie")
        menu = int(input("Wybierz operatora: "))
    if menu == 1:
        a = int(input("Podaj pierwszą cyfrę działania: "))
        b = int(input("Podaj drugą cyfrę działania: "))
        print(a+b)
        return a+b
    if menu == 2:
        a = int(input("Podaj pierwszą cyfrę działania: "))
        b = int(input("Podaj drugą cyfrę działania: "))
        print(a-b)
        return a-b
    if menu == 3:
        a = int(input("Podaj pierwszą cyfrę działania: "))
        b = int(input("Podaj drugą cyfrę działania: "))
        print(a*b)
        return a*b
    if menu == 4:
        a = int(input("Podaj pierwszą cyfrę działania: "))
        b = int(input("Podaj drugą cyfrę działania: "))
        print(a/b)
        return a/b
    if menu == 5:
        a = int(input("Podaj cyfrę działania: "))
        b = int(input("Potęga: "))
        print(a**b)
        return a**b

kalkulator()