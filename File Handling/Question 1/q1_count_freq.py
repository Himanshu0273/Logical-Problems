#Count the frequency of each word in the file and print it in a separate file

import string

def freq(s):
    lst = s.split()
    dic={}
    for i in lst:
        dic[i] = dic.get(i,0)+1
    return dic

def result_text(f):
    file1=freq(f)
    output_path = r"File Handling\\Question 1\\res1.txt"
    with open(output_path, "w") as file:
        for word, cnt in file1.items():
            file.write(f"{word}:{cnt}\n")
    return output_path

s=open("File Handling\\Question 1\sample1.txt", "r")
text = s.read()
text=text.translate(str.maketrans('','',string.punctuation))
result_text(text)