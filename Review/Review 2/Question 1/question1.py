import re
import json
from faker import Faker

faker=Faker()
def generate_input():
    input_lst = []
    for i in range(1000):
        gen_name = faker.first_name()
        gen_email = faker.email()

        if i % 10 == 0:
            gen_content = f"{faker.text()} python {faker.text()} docker {faker.text()}".lower()
        else:
            gen_content = faker.text().lower()

        my_dict = {
            "name": gen_name,
            "email": gen_email,
            "content": gen_content
        }

        input_lst.append(my_dict)

    return input_lst

with open("resumes.json", "w") as file:
    json.dump(generate_input(), file, indent=4)

json_file="resumes.json"
keywords = ["python", "docker"]
shortlisted=[]
with open(json_file, "r") as file1:
    data1 = json.load(file1)
    c=0
    for data in data1:
        c+=1
        value = data["email"]
        pattern = r"^[a-zA-Z0-9.-]+@[a-z.]+\.[a-z]{2,}$" #Email Pattern
        if re.match(pattern, value):
            print("Valid Email")
        else:
            pass
        content=data.get("content")
        matched=[]
        for i in keywords:
            if i not in content:
                print(f"'{i}' Keyword missing!!")
                continue
            matched.append(i)  
            
        
        else:
            print("All keywords present")
            final_dict=dict()
            final_dict["id"] = c
            final_dict["name"] = data["name"]
            final_dict["email"] = data["email"]
            final_dict["matched_keywords"] = matched
            if len(matched)>0:
                shortlisted.append(final_dict)
        print()
            
            
with open("shortlisted.json", "w") as output:
    json.dump(shortlisted, output, indent=4)
        