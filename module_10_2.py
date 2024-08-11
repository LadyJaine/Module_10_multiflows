from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self,name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        days = 0
        x = 100 #количество врагов
        while x != 0:
            x -= self.power
            days += 1
            print(f'{self.name} сражается {days} день(дней) , осталось {x} воинов.')
        else:
            print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()