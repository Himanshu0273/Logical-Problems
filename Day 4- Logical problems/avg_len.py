#Average length of the words in a sentence

import string

def avg_len(s):
    s=s.translate(str.maketrans('','',string.punctuation))
    words = s.split()
    tot = sum(len(x) for x in words)
    avg = tot / len(words) if words else 0
    print(words)
    return avg

s = input("Enter the sentence: ")
print("Average length of words: ", avg_len(s))
