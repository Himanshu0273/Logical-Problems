class Node: 
    def __init__(self, data=None):
        self.data = data
        self.next = None
        

class Linked_List:
    
    def __init__(self):
        self.head = Node()
        
        
    def append(self, val):
        new_node = Node(val)
        curr = self.head
        while curr.next!=None:
            curr = curr.next
        
        curr.next = new_node
        
    def length(self):
        curr = self.head
        c=0
        while curr.next !=None:
            c+=1
            curr=curr.next
            
        return c
    
    def display(self):
        elements = []
        curr = self.head
        while curr.next!=None:
            curr = curr.next
            elements.append(curr.data)
            
        print(elements)
        
    def get(self, index):
        if index>=self.length():
            print("ERROR: Index out of bounds")
            return None
        
        curr=self.head
        c=0
        while True:
            curr = curr.next
            if c==index:
                print("Value found!!")
                return curr.data
            c+=1
            
    def erase(self, index):
        if index>=self.length():
            print("Error: Index out of Bounds!!")
            return 
        c=0
        curr = self.head
        while True:
            prev = curr
            curr = curr.next
            if c==index:
                prev.next = curr.next
                return
            c+=1

linked_list = Linked_List()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print(linked_list.length())
# linked_list.display()
# print(linked_list.get(2))
# linked_list.erase(3)
# linked_list.display()