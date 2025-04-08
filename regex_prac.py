import re

text = "My email is himanshu@example.com and yours is test123@test.com"

# Match
# m = re.match(r"My email", text)
# print(m)  # Only checks the start

# Search
s = re.search(r"\w+@\w+\.\w+", text)
print(s.group())  # Finds first email

# # Findall
# emails = re.findall(r"\w+@\w+\.\w+", text)
# print(emails)  # List of all emails

# # Substitution
# new_text = re.sub(r"\w+@\w+\.\w+", "hidden_email", text)
# print(new_text)

# # Split
# parts = re.split(r"\s", text)
# print(parts)
