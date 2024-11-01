# Задание "Свой YouTube"
import time

class UrTube:
    users = {}
    videos = {}

    def __init__(self):
        self.current_user = None

    def log_in(self, *args):
        user = User(*args)
        if user.nickname in self.users.keys():
            if hash(user.password) == self.users[user.nickname][0]:
                print(f'Пользователь {user.nickname} залогинился')
                self.current_user = user.nickname
            else:
                print('Пароль неверен')
        else:
            print('Такой логин отсутствует')

    def register(self, *args):
        new_user = User(*args)
        if new_user.nickname not in self.users.keys():
            self.users[new_user.nickname] = (new_user.password, new_user.age)
            self.current_user = new_user.nickname
        else:
            print(f'Пользователь {new_user.nickname} уже существует')

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        films = (args)
        for k in films:
            if k.title not in self.videos.keys():
                self.videos[k.title] = [k.duration, k.time_now, k.adult_mode]

    def get_videos(self, kinopoisk):
        f = 0
        film_list = []
        for i in self.videos.keys():
            if kinopoisk.lower() in str(i).lower():
                film_list.append(i)
                f += 1
        if f == 0:
            film_list.append('Такого фильма не найдено')
        return film_list

    def watch_video(self, title):
        if self.current_user != None:
            f = 0
            for i in self.videos.keys():
                if title == i:
                    f += 1
                    if self.users[self.current_user][1] >= 18 or self.videos[i][2] != True:
                        for j in range(self.videos[i][0]):
                            self.videos[i][1] = j
                            time.sleep(1)
                            print(j + 1, end=' ')
                        self.videos[i][1] = 0
                        print('Конец видео')
                    else:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                        break
            if f == 0:
                print('Такого фильма не найдено')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


class Video():
    def __init__(self, title, duration, *, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class User:
    def __init__(self, name, password, age):
        self.nickname = name
        self.password = hash(password)
        self.age = age


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
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
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
