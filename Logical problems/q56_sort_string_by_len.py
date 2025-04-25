#Order string by the length of each word


def sort_by_length(s):
    words = s.split()
    words.sort(key=lambda word: len(word))
    print(words)

s = "Have a wonderful day"
sort_by_length(s)