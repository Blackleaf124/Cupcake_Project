import csv
from abc import ABC, abstractmethod
from pprint import pprint

def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)

read_csv("cupcakes.csv")

class Cupcake(ABC):
    size = "regular"
    def __init__(self, flavor, name, price, filling, glutenFree):
        self.flavor = flavor
        self.name = name
        self.price = price
        self.filling = filling
        self.glutenFree = glutenFree
        self.sprinkles = []

    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

    def calculate_price(self, quantity):
        return quantity * self.price

class Mini(Cupcake):
    size = "mini"
    def __init__(self, flavor, name, price, glutenFree):
        self.flavor = flavor
        self.name = name
        self.price = price
        self.glutenFree = glutenFree
        self.sprinkles = []

cupcake_1 = Mini("Triple Chocolate", "Chocolate Overkill", 2.99, False)

cupcake_1.add_sprinkles("White Chocolate", "Dark Chocolate", "Vanilla")

cupcake_2 = Mini("Vanilla cinnamon", "Lil' Spicy", .50, False)

cupcake_2.add_sprinkles("Cinnamon")

cupcake_3 = Mini("Vanilla Strawberry", "Strawberry Short cup", .50, True)

cupcake_3.add_sprinkles("Strawberry", "Vanilla")

cupcake_4 = Mini("Chocolate Chip", "Choco chip", 2.99, False)

cupcake_5 = Mini("Red Velvet", "Scarlet Mountain", 2.99, True)

cupcake_5.add_sprinkles("White Chocolate", "Dark Chocolate", "Vanilla")


cupcake_list = [
    cupcake_1,
    cupcake_2,
    cupcake_3,
    cupcake_4,
    cupcake_5
]


def write_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "flavor", "name", "price", "filling", "glutenFree", "sprinkles"]
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

        writer.writeheader()

        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({"size": cupcake.size, "flavor": cupcake.flavor, "name": cupcake.name, "price": cupcake.price, "filling": cupcake.filling, "glutenFree": cupcake.glutenFree, "sprinkles": cupcake.sprinkles})
            else:
                writer.writerow({"size": cupcake.size, "flavor": cupcake.flavor, "name": cupcake.name, "price": cupcake.price, "glutenFree": cupcake.glutenFree, "sprinkles": cupcake.sprinkles})

write_csv("cupcakes.csv", cupcake_list)

def add_cupcake(file, cupcakes):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "flavor", "name", "price", "filling", "glutenFree", "sprinkles"]
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({"size": cupcake.size, "flavor": cupcake.flavor, "name": cupcake.name, "price": cupcake.price, "filling": cupcake.filling, "glutenFree": cupcake.glutenFree, "sprinkles": cupcake.sprinkles})
            else:
                writer.writerow({"size": cupcake.size, "flavor": cupcake.flavor, "name": cupcake.name, "price": cupcake.price, "glutenFree": cupcake.glutenFree, "sprinkles": cupcake.sprinkles})

def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader

def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
    return None

def add_cupcake_dictionary(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "flavor", "name", "price", "glutenFree", "sprinkles"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)