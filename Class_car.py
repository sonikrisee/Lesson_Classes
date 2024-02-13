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
            speed = round(random.uniform(3.0, 4.0), 2)
            print(f"Разгон до 100 км/ч за {speed} секунд")
            print(f"Расход на 100 км: {self.rate} литров")

    def print_info(self):
        print(f"Год выпуска: {self.year}, Цвет:{self.color}, Цена: {self.price}, Марка: {self.brand}, Состояние: {self.condition}, Максимальная скорость: {self.max_speed}, Расход: {self.rate}, Ржавчина: {self.rust}")


first_car = Car(2010, "Red", 1000, "Audi", "Небита", 150, 10)
first_car.print_info()
first_car.drag()



class Dog:
    @staticmethod
    def calculate_god_year(age):
        return age * 7

# dog_age = int(input("Введите возраст собаки: "))
# human_age = Dog.calculate_god_year(dog_age)
# print(f"Возраст собаки в человеческих годах: {human_age}")



class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Значение равно: {self.value}"

obj = MyClass(40)
print(str(obj))


class PowTwo:
    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration
for i in PowTwo(3):
    print(i)







