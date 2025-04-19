#Sort the string according to the given template

def custom_sort(t, s):
    for i in t:
        if i in s:
            s=s.replace(i, "")
        
    print("The custom sorted string is: ", t+''.join(sorted(s)))

t = input("Enter the template: ")
s = input("Enter the string to sort: ")
custom_sort(t, s)