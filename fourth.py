
def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    aktualni_pozice = figurka["pozice"]
    typ = figurka["typ"]

    # 1. Ověření šachovnice
    if not (1 <= cilova_pozice[0] <= 8 and 1 <= cilova_pozice[1] <= 8):
        return False

    # 2. Ověření obsazenosti
    if cilova_pozice in obsazene_pozice:
        return False

    # 3. Pravidla pohybu
    if typ == "král":
        figurka_mozny_tah = (
            abs(aktualni_pozice[0] - cilova_pozice[0]) <= 1
            and abs(aktualni_pozice[1] - cilova_pozice[1]) <= 1
        )

    elif typ == "jezdec":
        figurka_mozny_tah = (
            abs(aktualni_pozice[0] - cilova_pozice[0]) == 2
            and abs(aktualni_pozice[1] - cilova_pozice[1]) == 1
        ) or (
            abs(aktualni_pozice[0] - cilova_pozice[0]) == 1
            and abs(aktualni_pozice[1] - cilova_pozice[1]) == 2
        )

    else:
        return False

    return figurka_mozny_tah and aktualni_pozice != cilova_pozice


if __name__ == "__main__":
    kral = {"typ": "král", "pozice": (4, 4)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    obsazene_pozice = {(4, 4), (5, 5), (3, 5)}

    # Testy pro krále
    print(je_tah_mozny(kral, (5, 5), obsazene_pozice))  # False (obsazeno)
    print(je_tah_mozny(kral, (5, 4), obsazene_pozice))  # True (o 1 pole dolů)
    print(je_tah_mozny(kral, (6, 6), obsazene_pozice))  # False (příliš daleko - o 2 pole)
    print(je_tah_mozny(kral, (0, 4), obsazene_pozice))  # False (mimo šachovnici)

    # Testy pro jezdce
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # True (tvar L: 2 nahoru, 1 doprava)
    print(je_tah_mozny(jezdec, (5, 5), obsazene_pozice))  # False (obsazeno)
    print(je_tah_mozny(jezdec, (4, 5), obsazene_pozice))  # True (tvar L)
    print(je_tah_mozny(jezdec, (10, 3), obsazene_pozice)) # False (mimo šachovnici)
