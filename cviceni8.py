class Zapornyzustatek(Exception):
    pass
class BankovniUcet:
    def __init__(self):
        self.zustatek = 0
    @property
    def zustatek(self):
        return self._zustatek
    @zustatek.setter
    def zustatek(self, hodnota):
        if hodnota < 0:
            raise Zapornyzustatek("Zůstatek nemůže být záporný!")
        self._zustatek = hodnota

if __name__ == "__main__":
    ucet = BankovniUcet()
    print(ucet.zustatek)
    ucet.zustatek = 1000
    print(ucet.zustatek)
    try:
        ucet.zustatek = -1000
    except Zapornyzustatek as e:
        print(e)