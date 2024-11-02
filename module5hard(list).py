# Задание "Свой YouTube"
import time

class UrTube:
    users = []
    videos = []

    def __init__(self):
        self.current_user = None

    def log_in(self, *args):
        user = User(*args)
        for m in self.users:
            if user.nickname == m.nickname and hash(user.password) == m.password:
                print(f'Пользователь {user.nickname} залогинился')
                self.current_user = user
            else:
                print('Пароль неверен')
        else:
            print('Такой логин отсутствует')

    def register(self, *args):
        new_user = User(*args)
        f = False
        for l in self.users:
            if new_user == l:
                f = True
                break
        if f == False:
            self.users.append(new_user)
            self.current_user = new_user
        else:
            print(f'Пользователь {new_user.nickname} уже существует')

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        films = (args)
        for k in films:
            if k not in self.videos:
                self.videos.append(k)

    def get_videos(self, kinopoisk):
        f = 0
        film_list = []
        for i in self.videos:
            if kinopoisk.lower() in str(i).lower():
                film_list.append(str(i))
                f += 1
        if f == 0:
            film_list.append('Такого фильма не найдено')
        return film_list

    def watch_video(self, title):
        if self.current_user != None:
            f = 0
            for i in self.videos:
                if title == i.title:
                    f += 1
                    if self.current_user.age >= 18 or i.adult_mode == False:
                        for j in range(i.duration):
                            i.time_now = j
                            time.sleep(1)
                            print(j + 1, end=' ')
                        i.time_now = 0
                        print('Конец видео')
                    else:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                        break
            if f == 0:
                print('Такого фильма не найдено')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


class Video():
    all_objects = []
    def __init__(self, title, duration, *, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __contains__(self, item):
        return any(item.title == obj.title for obj in UrTube.videos)

    def __eq__(self, other):
        return self.title == other.title


class User:
    all_objects = []
    def __init__(self, name, password, age):
        self.nickname = name
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __contains__(self, item):
        return any(item.nickname == obj.nickname for obj in UrTube.users)

    def __eq__(self, other):
        if other == None:
            return False
        else:
            return self.nickname == other.nickname



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

# Тесты
print('Все фильмы: ')
for i in ur.videos:
    print(str(i))
print('Все пользователи: ')
for i in ur.users:
    print(str(i))

