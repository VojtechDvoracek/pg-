def vynasob_xty_prvek(seznam, cislo_prvku, nasobek):
    if cislo_prvku > len(seznam) or cislo_prvku < 0:
        print(f"{cislo_prvku} prvek se nenachází v seznamu")
    else:
        seznam[cislo_prvku-1]*= nasobek
    return seznam

def spocitej_prumer(seznam):
    if len(seznam) == 0:
        return None
    soucet = sum(seznam)
    prumer = soucet / len(seznam)
    return prumer

def formatuj_text(student):
    prumer = spocitej_prumer(student["znamky"])
    return f"Student {student['jmeno']} {student['prijmeni']}, Vek: {student['vek']}, Prumer: {round(prumer, 1)}"

if __name__ == "__main__":

    student = {
        "jmeno": "Jan",
        "prijmeni": "Novak",
        "vek": 21,
        "znamky": [1, 2, 1, 1, 3, 2]
    }
    print (formatuj_text(student))

    seznam= vynasob_xty_prvek([1,2,3,4,5],3,10)
    print(seznam)

    vysledek = sum(seznam)
    print(f"Součet prvků seznamu je {vysledek}")

    prumer = spocitej_prumer(seznam)
    print(f"Průměr prvků seznamu je {prumer}")

    vek = input("Zadej svůj věk: ")

    vek= int(vek)

    if vek >= 21:
        print("můžeš pít v USA")
    else:
        print("Dej si colu")
    print(f"Za rok ti bude {vek+1}")

    seznam1 = [1,2,3,"čtyři",5]
    print (seznam1)
    seznam1.append("ahoj")
    print(seznam1[2])

    print(f"Seznam ma {len(seznam1)} prvků")