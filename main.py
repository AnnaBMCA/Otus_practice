# Создать класс User со следующими атрибутами:
# имя, фамилия, почтовый адрес, мобильный номер, пароль, животные
# Создать геттер и сеттер для пароля.
# Создайте класс Pet и добавьте к нему следующие атрибуты:
# кличка, порода, год рождения, хозяин (User)
# Добавьте список из Pet как атрибут экземпляра для User.
# Создайте несколько экземпляров класса User, добавьте к юзерам 1-4 домашнихж ивотных

class User:
    def __init__(self):
        self.name = ''
        self.surname = ''
        self.address = ''
        self.phone = ''
        self.pets = []
        self._password = 0

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, val):
        self._password = val

    @password.getter
    def password(self):
        return self._password


class Pet:
    def __init__(self, name, breed, year, user):
        self.name = name
        self.breed = breed
        self.year = year
        self.user = user


Cat = Pet('Varia', 'Snow Shoe', 2020, 'Anna')
Dog = Pet('Bob', 'Zpitz', 2019, 'Nick')

myUser = User()
myUser.pets = [Cat, Dog]

myUser.password = 56
print(myUser.password)
print(myUser.pets[0].name)
