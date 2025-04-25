class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None
        
class DoublyLL:
    
    def __init__(self):
        self.head = Node()
        self.tail = self.head
        
    def forward_insert(self, val):
        new_node = Node(val)
        self.tail.next = new_node
        new_node.prev=self.tail
        self.tail = new_node
    
    def forward_traversal(self):
        curr = self.head.next
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
            
        print("None")

    def backward_traversal(self):
        curr = self.tail
        while curr != self.head:
            print(curr.data, end=" <- ")
            curr = curr.prev
            
        print("Head")
              
            
obj = DoublyLL()
obj.forward_insert(1)
obj.forward_insert(2)
obj.forward_insert(3)
obj.forward_insert(4)

obj.forward_traversal()
print()
obj.backward_traversal()