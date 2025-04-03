from functools import reduce

dic1 = [
    {
        "Name": "Himanshu",
        "Age": 25,
        "City": "Chennai",
        "Salary": 25000
    },
    {
        "Name": "Aniket",
        "Age": 30,
        "City": "Kolkata",
        "Salary": 500
    },
    {
        "Name": "Karan",
        "Age": 23,
        "City": "Mumbai",
        "Salary": 2500
    },
    {
        "Name": "Premla",
        "Age": 23,
        "City": "Chennai",
        "Salary": 250
    },
    {
        "Name": "Premli",
        "Age": 22,
        "City": "Chennai",
        "Salary": 5000
    }
]


lst = [x for i in dic1 for x in i.values() if i["Age"]>=25]

print(lst)