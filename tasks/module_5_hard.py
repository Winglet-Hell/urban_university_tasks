import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    def hash_password(self, password):
        return hash(password)

    def __eq__(self, other):
        return self.nickname == other.nickname and self.password == other.password

    def __repr__(self):
        return f"User({self.nickname}, {self.age})"


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __repr__(self):
        return (
            f"Video({self.title}, {self.duration}s, "
            f'{"18+" if self.adult_mode else "All Ages"})'
        )


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        hashed_password = hash(password)
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                print(f"Пользователь {nickname} вошел в систему.")
                return
        print("Неверный логин или пароль.")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} зарегистрирован и вошел в систему.")

    def log_out(self):
        self.current_user = None
        print("Вы вышли из системы.")

    def add(self, *videos):
        for video in videos:
            if video.title not in [v.title for v in self.videos]:
                self.videos.append(video)
                print(f'Видео "{video.title}" добавлено на платформу.')
            else:
                print(f'Видео "{video.title}" уже существует.')

    def get_videos(self, search_term):
        search_term = search_term.lower()
        return [
            video.title for video in self.videos if search_term in video.title.lower()
        ]

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                while video.time_now < video.duration:
                    video.time_now += 1
                    print(video.time_now, end=" ")
                    time.sleep(1)
                print("Конец видео")
                video.time_now = 0
                return

        print(f'Видео "{title}" не найдено.')


# Проверочный код
ur = UrTube()
v1 = Video("Лучший язык программирования 2024 года", 10)
v2 = Video("Для чего девушкам парень программист?", 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos("лучший"))
print(ur.get_videos("ПРОГ"))

# Проверка на вход пользователя и возраст
ur.watch_video("Для чего девушкам парень программист?")
ur.register("vasya_pupkin", "lolkekcheburek", 13)
ur.watch_video("Для чего девушкам парень программист?")
ur.register("urban_pythonist", "iScX4vIJClb9YQavjAgF", 25)
ur.watch_video("Для чего девушкам парень программист?")

# Проверка входа в другой аккаунт
ur.register("vasya_pupkin", "F8098FM8fjm9jmi", 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video("Лучший язык программирования 2024 года!")
