import json
class Osoby:
    def __init__(self, jmeno, telefon, email):
        self.jmeno = jmeno
        self.telefon = telefon
        self.email = email
    
    @classmethod
    def z_json(cls, data):
        if not isinstance(data, dict):
            raise ValueError("Data musí být slovník!")
        if 'jmeno' not in data or 'telefon' not in data or 'email' not in data:
            raise ValueError("Data musí obsahovat klíče 'jmeno', 'telefon' a 'email'!")
        return cls(data['jmeno'], data['telefon'], data['email'])

if __name__ == "__main__":
    osoby=[]
    with open("osoby.json", "r") as f:
        data = json.load(f)
        for osoba_data in data:
            osoby.append(Osoby.z_json(osoba_data))
            print(f"Jméno: {osoby[-1].jmeno}, Telefon: {osoby[-1].telefon}, Email: {osoby[-1].email}")