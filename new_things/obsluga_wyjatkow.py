zmienna_1 = input("Podaj liczbe : ")
zmienna_2 = input("Podaj liczbe : ")
try:
    a = int(zmienna_1)
    b = int(zmienna_2)
    print(f"Suma licz to {a+b}.")
except Exception:
    print("to nie liczba")

print("koniec")