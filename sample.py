<<<<<<< HEAD
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

=======
a=10
b=10
c=a+b
if(c==13):
    print("c is not(not)13")
else:
    print("c is not 13, it is ",c)
#this is a comment
>>>>>>> 833233ce9ad828f9ba8895aceef2ab99e64050c8
