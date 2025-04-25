# from queue import Queue

# q = Queue(maxsize=3)
# q.put('a')
# q.put('b')
# q.put('c')
# print('Full: ', q.full())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.empty())
# q.put(1)
# q.put(3)
# q.put(2)
# q.put(4)
# print(q.get())


from collections import deque

q = deque()
q.append(1)
q.append(3)
q.append(2)
print(q)

print(q.popleft())
print(q.popleft())
print(q.popleft())
# print(q.popleft())
print(q)