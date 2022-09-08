import multiprocessing as mp
import math
import os


"""
Task: Print the square root of every element in a list.
"""
INPUT_LIST = list(range(40))

def task_printsqrt(elem):
	print(math.sqrt(elem))

def worker(inpt, task):
	while True:
		task(inpt.get(True))
		inpt.task_done()

inpt = mp.JoinableQueue()
for num in INPUT_LIST:
	inpt.put(num)

pool = mp.Pool(4, worker, (inpt, task_printsqrt))
inpt.join()