import csv

def prepare_data(wartosc):

    wartosc = wartosc.replace("$", "")
    wartosc = wartosc.replace(",", "")
    kwota = float(wartosc)
    # print(type(kwota))

    if isinstance(kwota, float):
        return kwota

    #pass

def analisis(lista):
    srednia = sum(lista)/len(lista)
    return srednia

def wyciagnij_srednia(csv_file):
    lista = []
    for row in csv_file:
        # print(row["balance"])
        wartosc = row["balance"]
        kwota = prepare_data(wartosc)
        lista.append(kwota)

    wynik = analisis(lista)

    return round(wynik, 2)

def wypisz_wiersze(csv_file):
    for row in csv_file:
        print(row["balance"])

with open("../resources/data.csv") as plik:
    csv_file = csv.DictReader(plik)

    print(wyciagnij_srednia(csv_file))

