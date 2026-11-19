def bin_to_dec(binarni_cislo):
    # funkce spocita hodnotu predavaneho binarniho cisla (binarni_cislo muze byt str i int!!!)
    # 111 -> 7
    # "101" -> 5
    if binarni_cislo == 0 or binarni_cislo == "0":
        return 0
    else:
        if isinstance(binarni_cislo, str):
            binarni_cislo = int(binarni_cislo)
        dec = 0
        i = 0
        while binarni_cislo > 0:
            dec += (binarni_cislo % 10) * (2 ** i)
            binarni_cislo //= 10
            i += 1
        return dec
    
def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    print(bin_to_dec(0))
    assert bin_to_dec(1) == 1
    print(bin_to_dec(1))
    assert bin_to_dec("100") == 4
    print(bin_to_dec("100"))
    assert bin_to_dec(101) == 5
    print(bin_to_dec(101))
    assert bin_to_dec("010101") == 21
    print(bin_to_dec("010101"))
    assert bin_to_dec(10000000) == 128
    print(bin_to_dec(10000000))

if __name__ == "__main__":
    test_bin_to_dec()