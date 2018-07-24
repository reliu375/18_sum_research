import threading
from threading import Lock, Thread

xList = []
lock = Lock()

def modify_list():
	global xList
	lock.acquire()
	xList.append(3)
	lock.release()
	return

def change_list():
	global xList

	xList.append(7)

	return

thread1 = Thread(target = modify_list)
thread1.start()

thread2 = Thread(target = change_list)
thread2.start()

thread1.join()
thread2.join()

print(xList)