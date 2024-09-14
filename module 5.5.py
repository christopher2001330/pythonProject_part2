import hashlib
import time


class User:
    """
    Класс пользователя, содержащий атрибуты: nickname, password(в хэшированном виде), age
    """

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hashlib.sha256(password.encode()).hexdigest()  # Хешируем пароль
        self.age = age


class Video:
    """
    Класс видео, содержащий атрибуты: title, duration(секунды), time_now(начальная позиция), adult_mode
    """

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    """
    Класс UrTube, содержащий методы для регистрации, входа в систему, добавления и поиска видео.
    """

    def __init__(self):
        self.users = []  # Список пользователей
        self.videos = []  # Список видео
        self.current_user = None  # Текущий пользователь

    def log_in(self, nickname, password):
        # Хешируем введённый пароль для сравнения
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                print(f"Пользователь {nickname} вошёл в систему")
                return
        print("Неверные логин или пароль")

    def register(self, nickname, password, age):
        # Проверка на существующего пользователя
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        # Создаём нового пользователя и автоматически логиним
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} успешно зарегистрирован")

    def log_out(self):
        if self.current_user:
            print(f"Пользователь {self.current_user.nickname} вышел из системы")
            self.current_user = None
        else:
            print("Ни один пользователь не вошёл в систему")

    def add(self, *videos):
        for video in videos:
            # Проверка на существующее видео с таким же названием
            if video.title not in [v.title for v in self.videos]:
                self.videos.append(video)
                print(f"Видео '{video.title}' добавлено")
            else:
                print(f"Видео с названием '{video.title}' уже существует")

    def get_videos(self, search_word):
        search_word = search_word.lower()
        result = [video.title for video in self.videos if search_word in video.title.lower()]
        return result

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                print(f"Начинаем просмотр видео: {video.title}")
                for second in range(1, video.duration + 1):
                    print(second, end=' ')
                    time.sleep(0.1)  # Для демонстрации вместо 1 секунды используем 0.1 секунды
                print("\nКонец видео")
                video.time_now = 0  # Сбрасываем просмотр
                return
        print("Видео не найдено")


# Проверка

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 10)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
