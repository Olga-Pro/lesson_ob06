# Задание: Разработать консольную игру "Битва героев" на Python с использованием классов
# и разработать план проекта по этапам/или создать kanban доску для работы над данным проектом
#
# Общее описание:
# Создайте простую текстовую боевую игру, где игрок и компьютер управляют
# героями с различными характеристиками.
# Игра состоит из раундов, в каждом раунде игроки по очереди наносят урон друг другу,
# пока у одного из героев не закончится здоровье.
#
# Требования:
# Используйте ООП (Объектно-Ориентированное Программирование) для создания классов героев.
# Игра должна быть реализована как консольное приложение.
# Классы:
# Класс Hero:
#   Атрибуты:
#        Имя (name)
#        Здоровье (health), начальное значение 100
#        Сила удара (attack_power), начальное значение 20
#   Методы:
#        attack(other): атакует другого героя (other), отнимая здоровье в размере своей силы удара
#        is_alive(): возвращает True, если здоровье героя больше 0, иначе False
# Класс Game:
#   Атрибуты:
#       Игрок (player), экземпляр класса Hero
#       Компьютер (computer), экземпляр класса Hero
#   Методы:
#       start(): начинает игру, чередует ходы игрока и компьютера,
#       пока один из героев не умрет. Выводит информацию о каждом ходе
#       (кто атаковал и сколько здоровья осталось у противника) и объявляет победителя.

from abc import ABC, abstractmethod
import random
class Heroes(ABC):
    # абстрактрый класс для игрока
    @abstractmethod
    def attack(self, other):
        pass

    def is_alive(self):
        pass

class Games(ABC):
    # абстрактный класс для игры
    def start(self):
        pass

class Hero(Heroes):
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health -= self.attack_power
        print(f"\n{self.name} атакует {other.name}")
        print(f"У {self.name} здоровье = {self.health}. У {other.name} здоровье = {other.health}.")

    def is_alive(self):
        return self.health > 0

class Game(Games):
    def __init__(self, player, computer):
        self.player = Hero(player)
        self.computer = Hero(computer)

    def start_attack(self):
        # чтобы было не скучно - пусть игроки атакуют в случайном порядке
        num = random.randint(1,10)
        if num > 5:
            self.player.attack(self.computer)
        else:
            self.computer.attack(self.player)

    def start(self):
        print("Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            # пока у обоих игроков есть здоровье
            self.start_attack()

        if self.player.is_alive():
            print(f"{self.computer.name} выиграл. ")
        else:
            print(f"{self.player.name} выиграл. ")
        print("Конец игры!")

# test
player_name = input("Задайте имя для игрока: ")
computer_name = "CompHero"
game = Game(player_name, computer_name)
game.start()


