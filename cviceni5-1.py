
import sys

def inkrementuj_cisla(data):
    nova_data=[]
    for radek in data:
        rodeleny = radek.split(",")
        novy_radek = []
        for prvek in rodeleni:
            try:
                prvek = str(int(prvek) + 1)
            except ValueError:
                pass
            print(prvek)
        nova_data.append(",".join(novy_radek))
    return nova_data
def nacti_radky(file_name):
    radky = []
    with open(file_name, "r") as file:
        for line in file:
            radky.append(line.strip())
    return radky

def zapis_radky(file_name, data):
    with open(file_name, "w") as file:
        for line in data:
            file.write(line + "\n")

if __name__ == "__main__":

    if len(sys.argv) <= 1:
        print(f"Pouziti: python {sys.argv[0]} jmeno_souboru")
        sys.exit()

    file_name = sys.argv[1]
    try:
        data = nacti_radky(file_name)
        print(data)
    except FileNotFoundError:
        print(f"Soubor {file_name} neexistuje")
        sys.exit(1)

    # data = inkrementuj_cisla(data)

    file_name2 = "data2.txt"
    zapis_radky(file_name2, data)
