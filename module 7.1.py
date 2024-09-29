class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                products = file.readlines()
            return ''.join(products).strip()  # Возвращаем всю информацию в виде строки
        except FileNotFoundError:
            return "Файл не найден."

    def add(self, *products):
        existing_products = self.get_products().splitlines()  # Получаем существующие продукты
        existing_names = [line.split(', ')[0] for line in
                          existing_products]  # Извлекаем названия существующих продуктов

        with open(self.__file_name, 'a') as file:  # Открываем файл в режиме добавления
            for product in products:
                if product.name in existing_names:
                    print(f"Продукт {product} уже есть в магазине")
                else:
                    file.write(f"{product}\n")  # Записываем продукт в файл
                    print(f"Добавлен продукт: {product}")


# Пример работы программы
if __name__ == "__main__":
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    # Первый запуск
    s1.add(p1, p2, p3)
    print(s1.get_products())

    # Второй запуск
    s1.add(p1, p2, p3)  # Пробуем добавить снова
    print(s1.get_products())
