import queue
from time import sleep
from threading import Thread


class Table:
    def __init__(self, number, is_busy=False):
        self.number = number
        self.is_busy = is_busy


class Cafe:
    def __init__(self, table_list):
        self.queue = queue.Queue()
        self.tables = table_list

    def customer_arrival(self):
        for i in range(1, 21):
            print(f'Посетитель номер {i} прибыл')
            customer = Customer(i)
            self.serve_customer(customer)
            sleep(1)

    def serve_customer(self, customer):
        count = 0
        for table in self.tables:
            if not table.is_busy:
                customer.table = table
                customer.start()
                return
            else:
                count += 1
        if count == 3:
            print(f'Посетитель номер {customer.number} ожидает свободный стол')
            self.queue.put(customer)


class Customer(Thread):
    def __init__(self, number, table=None):
        self.number = number
        self.table = table
        super().__init__()

    def run(self):
        self.table.is_busy = True
        print(f'Посетитель номер {self.number} сел за стол {self.table.number}')
        sleep(5)
        print(f'Посетитель номер {self.number} покушал и ушел')
        self.table.is_busy = False


table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

cafe = Cafe(tables)

customer_arrival_thread = Thread(target=cafe.customer_arrival)

customer_arrival_thread.start()

customer_arrival_thread.join()
