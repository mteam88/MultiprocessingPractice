import multiprocessing as mp
import requests, math


"""
Task: Print the square root of every element in a list.
"""
INPUT_LIST = list(range(40))
REQ_URL_LIST = [
	"https://git-scm.com/book/en/v2/Git-Basics-Tagging",
	"https://github.com/mteam88/MultiprocessingPractice/tags",
	"https://stackoverflow.com/questions/31711378/python-multiprocessing-how-to-know-to-use-pool-or-process",
	"https://stackoverflow.com/questions/17241663/filling-a-queue-and-managing-multiprocessing-in-python",
	"https://stackoverflow.com/questions/31230241/queue-vs-joinablequeue-in-python",
	"https://git-scm.com/book/en/v2/Git-Basics-Tagging",
	"https://github.com/mteam88/MultiprocessingPractice/tags",
	"https://stackoverflow.com/questions/31711378/python-multiprocessing-how-to-know-to-use-pool-or-process",
	"https://stackoverflow.com/questions/17241663/filling-a-queue-and-managing-multiprocessing-in-python",
	"https://stackoverflow.com/questions/31230241/queue-vs-joinablequeue-in-python",
]

class Task:
	def exec(self, elem):
		raise Exception

class Task_PrintSqrt(Task):
	def exec(self, num):
		print(math.sqrt(num))

class Task_SendRequest(Task):
	def exec(self, url):
		res = requests.get(url)
		print(url, ":", res.status_code)
		

def worker(inpt, task):
	while True:
		task.exec(inpt.get(True))
		inpt.task_done()

inpt = mp.JoinableQueue()
for num in REQ_URL_LIST:
	inpt.put(num)

pool = mp.Pool(4, worker, (inpt, Task_SendRequest()))
inpt.join()