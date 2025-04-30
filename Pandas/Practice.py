import pandas as pd

dict1 = {
    "name": ["Himanshu", "Chirag", "Krish","Gaurav"],
    "marks": [96,95,94,90],
    "age": [21,22,20,21]
}

df = pd.DataFrame(dict1)
print(df)


#How to create a csv file using Pandas
# df.to_csv("friends.csv")
# df.to_csv("friends_no_index.csv", index=False) #Stores the data in a CSV File without adding the index row

print(df.describe())
print()

info = pd.read_csv("info.csv")
# print(info)
info["age"][0] = 25
print()
# print(info)
info.to_csv('info.csv', index=False)

print()
#Change index
info.index = ['1st', '2nd', '3rd', '4th']
print(info)