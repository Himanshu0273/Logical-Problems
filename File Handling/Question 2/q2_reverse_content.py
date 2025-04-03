import string

text=""
with open("File Handling\\Question 2\sample.txt") as file:
    s=file.read()
    s=s.translate(str.maketrans('','',string.punctuation))
    lst = s.split()
    lst.reverse()
    text = ' '.join(lst)
    

output_file = "File Handling\\Question 2\\res.txt"
with open (output_file, "w") as file:
    file.write(text)
    