def je_prvocislo(cislo):
    if cislo < 2:
        return False

    for delitel in range(2, int(cislo ** 0.5) + 1):
        if cislo % delitel == 0:
            return False

    return True


def vrat_prvocisla(maximum):
    prvocisla = []

    for cislo in range(2, maximum + 1):
        if je_prvocislo(cislo):
            prvocisla.append(cislo)

    return prvocisla
