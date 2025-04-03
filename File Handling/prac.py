import json

data={
    "Name": "Alice",
    "Age": 25,
    "City": "NYC",
    "Skills": ["C++", "Python", "SQL"]
}


with open ("File Handling\data.json", "w") as file:
    json.dump(data, file, indent=4)
    

with open("File Handling\data.json") as file:
    data = json.load(file)
    print(data)
    
    
data["Country"] = "USA"

with open ("File Handling\data.json", "w") as file:
    json.dump(data, file, indent=4)
    
    
    
json_str = '{"Name":"Bob", "Age":30, "City": "LA"}'
data = json.loads(json_str)
print(data["Name"])

# import os

# if os.path.exists("File Handling\data.json"):
#     os.remove("File Handling\data.json")
# else:
#     print("Enter VALid filename")