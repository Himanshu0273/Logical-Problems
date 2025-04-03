#Each line in a separate file

input_file = "Question 4/errorlog.txt"

with open (input_file, "r") as file:
    output_file=["Question 4/Error1.txt", "Question 4/Error2.txt", "Question 4/Error3.txt", "Question 4/Error4.txt"]
    c=0
    for i in file:
        s = open(output_file[c], "w")
        c+=1
        s.write(i.strip())