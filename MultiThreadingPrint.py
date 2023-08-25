import time
import threading
import datetime


class TestThreading(object):
    def __init__(self, interval=15):
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            # More statements comes here
            print(datetime.datetime.now().__str__() + ' : Start task in the background')

            time.sleep(self.interval)
            print(datetime.datetime.now().__str__() + ' : background loop ends')


tr = TestThreading()
time.sleep(5)
print(datetime.datetime.now().__str__() + ' : First output')
time.sleep(5)
print(datetime.datetime.now().__str__() + ' : Second output')
