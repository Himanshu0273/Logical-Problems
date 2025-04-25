from collections import deque
from queue import LifoQueue
#Stacks using List
def list_stack():
    lst = []
    lst.append(10)
    lst.append(3)
    lst.append(30)
    lst.append(14)

    print(lst)
    
    lst.pop()
    print(lst.pop())
    print(lst)
    lst.pop()
    
    
#Stack using deque
def deque_stack():
    stack = deque()
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    
    print(stack)
    
    stack.pop()
    print(stack.pop())
    print(stack)
    
    
#Stack using LifoQueue
def lifo_stack():
    stack = LifoQueue(maxsize=3)
    stack.put('a')
    stack.put('b')
    stack.put('c')
    
    # print(stack)
    print("Full: ", stack.full())
    print("Size: ", stack.qsize())
    
    print(stack.get())
    print(stack.get())
    print(stack.get())
    print("Empty: ", stack.empty())
    
#MAIN FUNCTION AREA
# list_stack()
# deque_stack()
lifo_stack()