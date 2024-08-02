from threading import *
from time import sleep
class VIT(Thread):
    def run(self):
        for i in range(5):
            print("VIT")
            sleep(1)


class CSE(Thread):
    def run(self):
        for i in range(5):
            print("CSE")
            sleep(1)
t1=VIT()
t2=CSE()

t1.start()
sleep(0.2)
t2.start()
t1.join()
t2.join()
print("Students")
