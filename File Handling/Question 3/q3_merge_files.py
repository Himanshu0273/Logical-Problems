#Merge 2 files line by line

import itertools
def copy_files(file1, file2):
    with open(file1, "r") as f1, open(file2, "r") as f2:
        l1 = f1.readlines()
        l2 = f2.readlines()
        
    # merged_lines = (line for pair in itertools.zip_longest(l1, l2, fillvalue="") for line in pair)
    merged_lines = (line if line.endswith('\n') else line+"\n" for pair in itertools.zip_longest(l1, l2, fillvalue="") for line in pair)
    
    with open (file1, 'w') as f1:
        f1.writelines(merged_lines)

file1 = "Question 3/t1.txt"
file2 = "Question 3/t2.txt"

copy_files(file1, file2)
# print(f"Content of {file1} is copied to {file2}")
