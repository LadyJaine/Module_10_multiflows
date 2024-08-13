import random
import threading
from threading import Thread, Lock
from time import sleep

class Bank:
    def __init__(self):
        self.balance = 500
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            try:
                x = random.randint(50,500)
                self.balance += x
                print(f"Пополнение: {x}. Баланс: {self.balance}.")
                sleep(0.001)
            finally:
                if self.balance > 500 and self.lock.locked():
                    self.lock.release()
    def take(self):
        for i in range(100):
            try:
                y = random.randint(50,500)
                print(f"Запрос на {y}")
                if y <= self.balance:
                    self.balance -= y
                    print(f"Снятие: {y}. Баланс: {self.balance}")
                    sleep(0.001)
                else:
                    print("Запрос отклонён, недостаточно средств")
                    self.lock.acquire()
            except:
                print("Запрос отклонён, недостаточно средств")

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print()
print(f"Итоговый баланс: {bk.balance}")
