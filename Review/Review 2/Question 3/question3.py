import re
import json
from faker import Faker
import random

faker=Faker()
def generate_input():    
    time = faker.time()
    text = faker.text(max_nb_chars=50)
    choice = random.choice([1,2])
    if choice == 1:
        name = faker.first_name()
        return f"[{time}] {name}: {text}"
    else:
        name1 = faker.first_name()
        name2 = faker.first_name()
        return f"[{time}] {name1}->{name2}: {text}"
    
with open("chat.txt", "w") as file:
    for _ in range(1000):
        data = generate_input()
        file.write(data+"\n") 
    
input_file = "chat.txt"
output_file = "chat.json"
output = []
with open(input_file,"r") as file1:
    chats = file1.readlines()
    for chat in chats:
        dict = {}
        reply_val = dict.setdefault("time", "null")
        reply_val = dict.setdefault("sender", "null")
        reply_val = dict.setdefault("message", "null")
        reply_val = dict.setdefault("reply_to", "null")
        txt_lst = chat.split()
        # print(txt_lst)
        # names = ["Alice", "Bob"]
        time_pattern = r"^\[\d{2}:\d{2}\]$"
        if re.match(time_pattern, txt_lst[0]):
            dict["time"] = txt_lst[0][1:6]
        
        msg_start=2
        if "->" in txt_lst:
            msg_start=4
            dict["sender"] = txt_lst[1]
            dict["reply_to"] = txt_lst[3][:-1]
            
        else:
            dict["sender"] = txt_lst[1][:-1]
            
        txt_lst = txt_lst[msg_start: ]
        dict["message"] = ' '.join(txt_lst)
        output.append(dict)
        
with open(output_file, "w") as result:
    json.dump(output, result, indent=4)