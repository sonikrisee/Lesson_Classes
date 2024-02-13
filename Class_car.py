import random


class Car:
    rust = "Да"

    def __init__(self, year, color, price, brand, condition, max_speed, rate):
        self.year = year
        self.color = color
        self.price = price
        self.brand = brand
        self.condition = condition
        self.max_speed = max_speed
        self.rate = rate

    def drag(self):
            speed = float(random.uniform(3.0, 4.0))
            print(f"Разгон до 100 км/ч за {speed} секунд")
            print(f"Расход на 100 км: {self.rate} литров")

    def print_info(self):
        print(f"Год выпуска: {self.year}, Цвет:{self.color}, Цена: {self.price}, Марка: {self.brand}, Состояние: {self.condition}, Максимальная скорость: {self.max_speed}, Расход: {self.rate}, Ржавчина: {self.rust}")


first_car = Car(2010, "Red", 1000, "Audi", "Небита", 150, 10)
first_car.print_info()
first_car.drag()
