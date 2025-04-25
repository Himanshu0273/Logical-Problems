#Check if the words can be made from the given string:

def anagram(main_str, lst):
    for i in lst:
        print("Word RN: ", i)
        for j in range(len(i)):
            if i[j] not in main_str:
                return False
            ind = main_str.find(i[j])
            main_str = main_str[:ind]+main_str[ind+1:]
            print(main_str)
            
    return True

main_str = "Justin Bieber"
lst = ["injures", "ebb", "it"]
print(anagram(main_str.lower(), lst))