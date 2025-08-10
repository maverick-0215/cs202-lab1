"""this file conatins data structures that are used frequently in python"""

from queue import Queue
from collections import deque
import heapq

#list operations
nums=[2,5,1,6]
nums.append(3)
nums.remove(6)
nums.sort()
print("list of numbers: ",nums)

#using a dictionary
roll_no={"alice":1, "bob":2, "charles":3,"dobby":4}
roll_no["emma"]=5
roll_no["fiona"]=6
print("dictionary of names and roll numbers: ",roll_no)

dq=deque(["a", "b", "c"])
dq.appendleft("z")
dq.append("y")
dq.append("d")
dq.pop()
dq.popleft()
print("Deque:", dq)

heap = [5,1,9,3]
heapq.heapify(heap)
heapq.heappush(heap, 2)
heapq.heappush(heap,8)
min_val = heapq.heappop(heap)
print("Heap after push & pop:", heap, "Min popped:", min_val)

q=Queue()
[q.put(i) for i in range(5)]
while not q.empty():
    print(q.get())