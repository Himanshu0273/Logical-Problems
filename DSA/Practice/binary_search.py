def bin_search(s, target):
    lst = s.split()
    print(lst)
    lst = sorted(lst)
    print(lst)

input = "DSA\Practice\input.txt"
s=""
with open(input, "r") as file:
    for line in file:
        s+=(line).lower()
        
target = "Himanshu"
print(s)
bin_search(s, target)