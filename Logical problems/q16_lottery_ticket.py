def lottery_result(lst):
    tickets = lst[0]
    k = lst[1]
    c=0
    for t in tickets:
        s,x = t
        # for i in s:
        #     val = ord(i)
        #     if(val==x):
        #         c+=1
        #         break
        if any(ord(c)==x for c in s):
            c+=1
        
        
    return "Winner!!!" if c>=k else "Loser!"

n=int(input("Enter number of entries: "))
print()
# tickets = [input("Enter the string and number: ").split() for _ in range(n)]
# tickets = [[x[0], int(x[1])] for x in tickets]
tickets=[]
for _ in range(n):
    code = input("Enter Code: ")
    val = int(input("Enter Value: "))
    print()
    tickets.append([code, val])

k = int(input("Enter second value: "))
lst = [tickets, k]

print(lottery_result(lst)) 