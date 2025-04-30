class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.val)
        
        
#           1
#       2       3
#     4   5   10

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

#Recursive:
#Pre order

def preorder(node):
    if node == None:
        return
    
    print(node, end=" ")
    preorder(node.left)
    preorder(node.right)
    
def postorder(node):
    if node == None:
        return 
    
    postorder(node.left)
    postorder(node.right)
    print(node, end=" ")

def inorder(node):
    if not node:
        return
    
    inorder(node.left)
    print(node, end=" ")
    inorder(node.right)
    
print("Recursive Preorder: ", end=" ")    
preorder(A)
print()
print("Recursive Postorder: ", end=" ")    
postorder(A)
print()
print("Recursive Inorder: ", end=" ")    
inorder(A)
print()
print()

#Iterative
#DFS
def pre_order(node):
    if not node:
        return
    
    stk = [node]
    lst = []
    while stk:
        top = stk.pop()
        lst.append(top.val)
        if top.right:
            stk.append(top.right)
        if top.left:
            stk.append(top.left)
            
    return lst

def in_order(root):
    stack = []
    curr = root
    res=[]
    while curr or stack:
        while curr:
            stack.append(curr)
            curr=curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res

def post_order(root):
    if not root:
        return 
    
    stk1 = [root]
    stk2 = []
    while stk1:
        node = stk1.pop()
        stk2.append(node.val)
        if node.left:
            stk1.append(node.left)
        if node.right:
            stk1.append(node.right)

    res=[]
    while stk2:
        res.append(stk2.pop())
    
    return res

#BFS
from collections import deque
def level_order(node):
    q = deque()
    q.append(node)
    lst=[]
    while q:
        front = q.popleft()
        lst.append(front.val)
        if front.left:
            q.append(front.left)
        
        if front.right:
            q.append(front.right)
            
    return lst

print("Iterative Preorder:  ", pre_order(A))
print("Iterative Inorder:   ", in_order(A))
print("Iterative Postorder: ", post_order(A))
print("Iterative LevelOrder:", level_order(A))