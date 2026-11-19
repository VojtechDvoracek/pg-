message = ["Jméno nesmí být prázdný řetězec nebo číslo!", "Telefon musí být 9místný číslo!", "Email musí být neprázdný řetězec obsahující '@'!"]
class InvalidData(Exception):
    def __init__(self, message):
        self.message = message
        print(self.message)

class Osoba:
    def __init__(self, jmeno, telefon, email):
        self.jmeno = jmeno
        self.telefon = telefon
        self.email = email
    
    @property
    def jmeno(self):
        return self._jmeno
    @jmeno.setter
    def jmeno(self, hodnota):
        if not isinstance(hodnota, str) or not hodnota.isalpha():
            raise InvalidData("Jméno nesmí být prázdný řetězec nebo číslo!")
        self._jmeno = hodnota
    
    @property
    def telefon(self):
        return self._telefon
    @telefon.setter
    def telefon(self, hodnota):
        if not isinstance(hodnota, str) or not hodnota.isnumeric() or len(hodnota) != 9:
            raise InvalidData("Telefon musí být 9místný číslo!")
        self._telefon = hodnota
    
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, hodnota):
        if not isinstance(hodnota, str) or not hodnota.strip() or "@" not in hodnota:
            raise InvalidData("Email musí být neprázdný řetězec obsahující '@'!")
        self._email = hodnota

if __name__ == "__main__":
    osoba = Osoba("Petr", "123456789", "petr@seznam.cz")
    osoba.jmeno = "Petr"
    osoba.telefon = "123456789"
    osoba.email = "petr@seznam.cz"

    for message in message:
        try:
            raise InvalidData(message)
        except InvalidData as e:
            print(e.message)