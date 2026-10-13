def cislo_text(cislo):
	jednotky = (
		"nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm",
		"osm", "devět", "deset", "jedenáct", "dvanáct", "třináct",
		"čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct",
	)
	desitky = {
		20: "dvacet", 30: "třicet", 40: "čtyřicet", 50: "padesát",
		60: "šedesát", 70: "sedmdesát", 80: "osmdesát", 90: "devadesát",
	}

	if cislo < 20:
		return jednotky[cislo]
	if cislo == 100:
		return "sto"

	desitka, zbytek = cislo//10, cislo % 10
	text_desitky = desitky[desitka * 10]
	return text_desitky if zbytek == 0 else f"{text_desitky} {jednotky[zbytek]}"


if __name__ == "__main__":
    print(cislo_text(0))      
    print(cislo_text(5))      