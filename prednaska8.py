class Car:
    counter = 0

    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        Car.update_counter()
    def get_type(self):
        return f"{self.brand} {self.model} in {self.color}"

    @classmethod
    def update_counter(cls):
        cls.counter +=1


if __name__ == "__main__":
    car1 = Car("Toyota", "Camry", "blue")
    car2 = Car("Honda", "Civic", "red")
    
    print(car1.get_type())
    print(car2.get_type()) 

    Car.get_type(car1)
    Car.get_type(car2)

    print(car1.color)
    print(Car.counter)