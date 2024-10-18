from threading import Thread, Lock
from time import sleep
import queue
from random import randint


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def __str__(self):
        return self.name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *args):
        self.queue = queue.Queue()
        self.tables = list(args)

    def guest_arrival(self, *guests):
        for people in guests:
            table_use = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = people
                    print(f'{people.name} сел(-а) за стол номер {table.number}')
                    people.start()
                    table_use = True
                    break
            if not table_use:
                self.queue.put(people)
                print(f'{people.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f'{table.guest} покушал(-а) и ушёл(ушла)')
                    table.guest = None
                    print(f'Стол номер {table.number} свободен')
                if not self.queue.empty():
                    table.guest = self.queue.get()
                    print(f'{table.guest} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()



tables = [Table(numb) for numb in range(1, 6)]
guests_names = ['Ромашка', 'Лариса', 'Виталя', 'Злой Юрий', 'Килза', 'Ия', 'Ирусик']
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()
