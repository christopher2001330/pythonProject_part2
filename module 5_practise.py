class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль
    """

    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password
        else:
            self.password = None  # Добавляем значение None, если пароли не совпадают


if __name__ == "__main__":
    database = Database()
    while True:
        choice = input("Приветствую! Выберите действие: \n1 - Вход\n2 - Регистрация\n ")

        if choice == "1":  # Исправляем сравнение строки
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            if login in database.data:
                if password == database.data[login]:
                    print(f"Вход выполнен, {login}")
                    break
                else:
                    print("Неверный пароль")
            else:
                print("Пользователь не найден")

        elif choice == "2":  # Исправляем сравнение строки
            username = input("Введите логин: ")
            password = input("Введите пароль: ")
            password_confirm = input("Повторите пароль: ")

            user = User(username, password, password_confirm)

            if user.password:  # Проверяем, установился ли пароль (значит пароли совпали)
                database.add_user(user.username, user.password)
                print(f"Пользователь {user.username} успешно зарегистрирован")
            else:
                print("Пароли не совпадают. Попробуйте ещё раз.")

        else:
            print("Неверный выбор, пожалуйста, выберите 1 или 2.")
