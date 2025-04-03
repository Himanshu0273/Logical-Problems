def copy_files(file1, file2):
    with open(file1, 'r') as src, open(file2, 'a') as dest:
        dest.write("\n"+src.read())

file1 = "Question 3/t1.txt"
file2 = "Question 3/t2.txt"

copy_files(file1, file2)
print(f"Content of {file1} is copied to {file2}")
