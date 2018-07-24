# A test program to familiarize my understanding of the condition class

import random, time
import pdb
import threading
from threading import Condition, Thread

condition = Condition()

box = [] # an array keeping track of objects available for consumption.
consumption = [] # an arry keeping track of objects consumed.
num_items = 5

# producing a few objects.
# when production is in progress, the box is locked.
def produce(box, num_items):
	for i in range(num_items):
		time.sleep(2)

		# Lock up the box when production is in progress
		condition.acquire() 
		num = random.randint(1,10)
		box.append(num)

		# The thread will send notification regarding the change in state.
		condition.notify()
		print('Produced: ', num)

		# Unlock the box to allow consumption.
		condition.release()

def consume(box, consumption, num_items):
	for i in range(num_items):
		condition.acquire()

		# Wait for the box to be unlocked by production function.
		condition.wait()
		cspn = box.pop()
		consumption.append(cspn)

		print('%s: Acquired: %s' % (time.ctime(), cspn))

		# Release the box again for production
		condition.release()

# Declaring and starting the threads controlling each function, respectively.
thread1 = Thread(target = produce, args = (box, num_items))
thread1.start()

thread2 = Thread(target = consume, args = (box, consumption, num_items))
thread2.start()

# Join the threads
thread1.join()
thread2.join()

# Notifying the completion of the program
print('All Done.')



