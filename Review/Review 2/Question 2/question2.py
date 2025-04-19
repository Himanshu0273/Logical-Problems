import re 
import json
from collections import Counter

tag_pattern = "<\s*(\w+)"
with open("page.txt", "r") as file:
    data = file.read()
    tag_list = re.findall(tag_pattern, data)
    tag_freq = Counter(tag_list)
    
with open("tag_count.json", "w") as output:
    json.dump(tag_freq, output, indent=4)