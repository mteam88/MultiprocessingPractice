import multiprocessing as mp
import math
import os


"""
Task: Print the square root of every element in a list.
"""
INPUT_LIST = list(range(40))

class Task:
	def exec(self, elem):
		raise Exception

class Task_PrintSqrt(Task):
	def exec(self, num):
		print(math.sqrt(num))

def worker(inpt, task):
	while True:
		task.exec(inpt.get(True))
		inpt.task_done()

inpt = mp.JoinableQueue()
for num in INPUT_LIST:
	inpt.put(num)

pool = mp.Pool(4, worker, (inpt, Task_PrintSqrt()))
inpt.join()