# import unittest
#
#
# class Car:
#     def __init__(self):
#         self.model = None
#         self.color = None
#         self.year = None
#
#
# class CarBuilder:
#     def __init__(self):
#         self.car = Car()
#
#     def set_model(self, model):
#         self.car.model = model
#
#     def set_color(self, color):
#         self.car.color = color
#
#     def set_year(self, year):
#         self.car.year = year
#
#     def get_car(self):
#         return self.car
#
#
# builder = CarBuilder()
# builder.set_model("Toyota")
# builder.set_color("Black")
# builder.set_year("1999")
# car = builder.get_car()
#
# print(f"Model: {car.model}, Color: {car.color}, Year: {car.year}")
#
#
# class TestCarBuilder(unittest.TestCase):
#
#     def test_car_builder(self):
#         builder = CarBuilder()
#         builder.set_model("Toyota")
#         builder.set_color("Black")
#         builder.set_year("1999")
#         car = builder.get_car()
#
#         self.assertEqual(car.model, "Toyota")
#         self.assertEqual(car.color, "Black")
#         self.assertEqual(car.year, "1999")
#
#
# if __name__ == '__main__':
#     unittest.main()


# class Pasta:
#     def pasta_type(self):
#         pass
#
#     def sauce(self):
#         pass
#
#     def filling(self):
#         pass
#
#     def toppings(self):
#         pass
#
#
# class Spaghetti(Pasta):
#     def pasta_type(self):
#         return "Spaghetti"
#
#     def sauce(self):
#         return "Tomato sauce"
#
#     def filling(self):
#         return "Meatballs"
#
#     def toppings(self):
#         return "Parmesan cheese"
#
#
# class Farfalle(Pasta):
#     def pasta_type(self):
#         return "Farfalle"
#
#     def sauce(self):
#         return "Pesto sauce"
#
#     def filling(self):
#         return "Cherry tomatoes"
#
#     def toppings(self):
#         return "Pine nuts"
#
#
# class Penne(Pasta):
#     def pasta_type(self):
#         return "Penne"
#
#     def sauce(self):
#         return "Cream sauce"
#
#     def filling(self):
#         return "Mushrooms"
#
#     def toppings(self):
#         return "Basil"
#
#
# class PastaFactory:
#     def create_pasta(self, pasta_type):
#         if pasta_type == "Spaghetti":
#             return Spaghetti()
#         elif pasta_type == "Farfalle":
#             return Farfalle()
#         elif pasta_type == "Penne":
#             return Penne()
#
#
# factory = PastaFactory()
# chosen_pasta = factory.create_pasta("Spaghetti")
# print(chosen_pasta.pasta_type())
# print(chosen_pasta.sauce())
# print(chosen_pasta.filling())
# print(chosen_pasta.toppings())


import copy


class Prototype:
    def clone(self):
        return copy.deepcopy(self)


class ConcretePrototype(Prototype):
    def __init__(self, field):
        self.field = field

    def __str__(self):
        return f"ConcretePrototype field: {self.field}"


original = ConcretePrototype("initial field")
print(original)

clone = original.clone()
print(clone)

print(original is clone)