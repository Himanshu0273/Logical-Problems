class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLL:
    
    def __init__(self):
        self.head = Node()
        
    def append(self, data):
        new_node = Node(data)
        curr = self.head
        while curr.next!=None:
            curr=curr.next
            
        curr.next = new_node
        
    def delete_node(self, index):
        curr = self.head
        c=0
        while curr.next!=None:
            prev=curr
            curr=curr.next
            if c==index:
                prev.next = curr.next
                return
            c+=1
    
    def get(self, index):
        curr=self.head
        c=0
        while curr.next is not None:
            curr = curr.next
            if c==index:
                return curr.data
            c+=1
            pass
    
    def length(self):
        curr = self.head
        c=0
        while curr.next is not None:
            c+=1
            curr=curr.next
        
        return c
    
    def display(self):
        curr = self.head
        while curr.next!=None:
            curr=curr.next
            print(curr.data)
            

obj = SinglyLL()
obj.append(1)        
obj.append(2)        
obj.append(3)
print(obj.get(1))
obj.delete_node(1)
obj.display()        
print("Length: ", obj.length())