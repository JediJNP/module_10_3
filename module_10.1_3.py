import threading
import random
import time


print('"Банковские операции"')
print('---------------------')


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            rand_count = random.randint(50, 500)
            self.lock.acquire()
            try:
                self.balance += rand_count
                print(f'Пополнение: {rand_count}. Баланс: {self.balance}')
                if self.balance >= 500:
                    return
            finally:
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            rand_count = random.randint(50, 500)
            print(f'Запрос на {rand_count}')
            self.lock.acquire()
            try:
                if rand_count <= self.balance:
                    self.balance -= rand_count
                    print(f'Снятие: {rand_count}. Баланс: {self.balance}')
                else:
                    print('Запрос отклонён, недостаточно средств')
            finally:
                self.lock.release()
            time.sleep(0.001)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')
