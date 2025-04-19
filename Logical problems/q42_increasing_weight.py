#Increasing weight of words

def weight(word):
    s=sum(ord(i) for i in word if i.isalpha())
    return s

def increasing_order(s):
    lst = s.split()
    prev=0
    for i in lst:
        if weight(i)<prev:
            print("False")
            return
        prev=weight(i)
    print("True")
        
s = input("Enter a sentece to check for increasing order of weight: ")
increasing_order(s)