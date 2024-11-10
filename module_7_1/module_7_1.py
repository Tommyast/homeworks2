import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'
    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        existing_products = []
        try:
            existing_products = self.get_products().splitlines()
        except FileNotFoundError:
            pass
        existing_names = {line.split(', ')[0] for line in existing_products}

        for i in products:
            if i.name in existing_names:
                print(f"Продукт {i.name} уже есть в магазине")
            else:
                file = open(self.__file_name, 'a')
                file.write(str(i) + '\n')
                file.close()




s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())


