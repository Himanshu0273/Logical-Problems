import re
import json
from faker import Faker
import random 

#Faker
faker = Faker()
def generate_input():
    log_levels=["INFO", "WARNING", "ERROR"]
    date = faker.date()
    time = faker.time()
    lvl = random.choice(log_levels)
    user = random.choice([faker.email(), "admin"])
    # msg = random.choice()
    ip = faker.ipv4()
    # msg_choice = random.choice([1,2,3])
    if lvl=="INFO":
        return f"[{date} {time}] {lvl}: User {user} logged in from {ip}"
    elif lvl=="ERROR":
        return f"[{date} {time}] {lvl}: Failed login for user {user} from IP {ip}"
    else:
        return f"[{date} {time}] {lvl}: User {user} exceeded login attempts"
    
with open("system_logs.txt", "w") as file:
    for _ in range(1000):
        data = generate_input()
        file.write(data+"\n")        
        
input_file = "system_logs.txt"
output_file = "log_summary.json"

email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
ip_pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"

res_dict = {}

with open(input_file, "r") as file1:
    msgs = file1.readlines()
    for line in msgs:
        emails = re.findall(email_pattern, line)
        ips = re.findall(ip_pattern, line)

        for mail in emails:
            if mail not in res_dict:
                res_dict[mail] = {"count": 0, "ips": set()}
            res_dict[mail]["count"] += 1
            res_dict[mail]["ips"].update(ips)

        if "admin" in line:
            if "admin" not in res_dict:
                res_dict["admin"] = {"count": 0, "ips": set()}
            res_dict["admin"]["count"] += 1
            res_dict["admin"]["ips"].update(ips)

for value in res_dict.values():
    value["ips"] = list(value["ips"])

with open(output_file, "w") as file1:
    json.dump(res_dict, file1, indent=4)
