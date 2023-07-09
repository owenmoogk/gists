from collections import deque
import time, threading

class Queue:
    
    def __init__(self):
        self.collection = deque()

    def queue(self, data):
        self.collection.appendleft(data)

    def dequeue(self):
        element = self.collection.pop()
        return(element)

    def isEmpty(self):
        if len(self.collection) == 0:
            return(True)
        return(False)

def placeOrders(orders):
    for order in orders:
        orderQ.queue(order)
        time.sleep(0.5)

def serveOrders():
    while True:
        time.sleep(2)
        print(orderQ.dequeue())
        if orderQ.isEmpty():
            break

orderQ = Queue()
orders = ['pizza','samosa','pasta','biryani','burger']

t1 = threading.Thread(target=placeOrders, args=(orders,))
t2 = threading.Thread(target=serveOrders)
t1.start()
t2.start()
t1.join()
t2.join()
print("done")