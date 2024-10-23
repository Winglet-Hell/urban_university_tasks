class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = (
            "/Users/winglet/Yandex.Disk.localized/Study/urban_university/tasks/"
            "module_7_1/products.txt"  # Путь к файлу
        )

    def get_products(self):
        file = open(self.__file_name, "r")  # Открытие файла для чтения
        products = file.read()
        file.close()  # Закрытие файла после чтения
        return products

    def add(self, *products):
        current_products = self.get_products()  # Список существующих продуктов

        file = open(self.__file_name, "a")  # Открытие файла для записи
        for product in products:
            if product.name not in current_products:
                file.write(str(product) + "\n")  # Записываем продукт, если его ещё нет
            else:
                print(
                    f"Продукт {product.name}, {product.weight}, "
                    f"{product.category} уже есть в магазине"
                )
        file.close()  # Закрытие файла после записи


# Пример использования:
s1 = Shop()
p1 = Product("Potato", 50.5, "Vegetables")
p2 = Product("Spaghetti", 3.4, "Groceries")
p3 = Product("Potato", 5.5, "Vegetables")

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
