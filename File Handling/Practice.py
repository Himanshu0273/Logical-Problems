# start = input("Enter the start cup: ")
# n = int(input("Number of moves: "))
# lst = [input("Enter the 2 letter strings: ").upper() for _ in range(n)]

# for i in lst:
#     if start in i:
#         start = i[0] if start==i[1] else i[1]
        
# print(start)


#Number to words:

# def number_to_word(n):

#     numbers= {
#         1: "One",
#         2: "Two",
#         3: "Three",
#         4: "Four",
#         5: "Five",
#         6: "Six",
#         7: "Seven",
#         8: "Eight",
#         9: "Nine",
#         10: "Ten",
#         11: "Eleven",
#         12: "Twelve",
#         13: "Thirteen",
#         14: "Fourteen",
#         15: "Fifteen",
#         16: "Sixteen",
#         17: "Seventeen",
#         18: "Eighteen",
#         19: "Nineteen",
#     }

#     tens = {
#         2: "Twenty",
#         3: "Thirty",
#         4: "Forty",
#         5: "Fifty",
#         6: "Sixty",
#         7: "Seventy",
#         8: "Eighty",
#         9: "Ninety"        
#     }


#     res=""
    
#     if n>=1000:
#         res+=(numbers[n//1000]) + " Thousand "
#         n%=1000

#     if n>=100 and n<=999:
#         res+=(numbers[n//100]) + " Hundred "
#         n%=100

#     if n>=20 and n<=99:
#         res+=(tens[n//10])+" "
#         n%=10
#     if n>0:
#         res+=numbers[n]+" "
    
#     return res
    
# n = int(input("Enter number: "))
# print (number_to_word(n))


#Word to number:

# dic={
#     "one": 1,
#     "two": 2,
#     "three": 3,
#     "four": 4,
#     "five": 5,
#     "six": 6,
#     "seven": 7,
#     "eight": 8,
#     "nine": 9,
#     "ten": 10,
#     "eleven": 11,
#     "twelve": 12,
#     "thirteen": 13,
#     "fourteen": 14,
#     "fifteen": 15,
#     "sixteen": 16,
#     "seventeen": 17,
#     "eighteen": 18,
#     "nineteen": 19,
#     "twenty": 20,
#     "thirty": 30,
#     "forty": 40,
#     "fifty": 50,
#     "sixty": 60,
#     "seventy": 70,
#     "eighty": 80,
#     "ninety": 90
# }



def words_to_number(s):
    dic = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11, 
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
        "hundred": 100,
        "thousand": 1000,
        "lakh": 100000,
        "crore": 10000000
    }

    words = s.lower().replace("-", " ").split()  
    num, current = 0, 0  

    for word in words:
        if word in dic:
            value = dic[word]

            if value == 100:  
                current *= value
            elif value >= 1000: 
                num += current * value
                current = 0 
            else:
                current += value 
        else:
            return "Invalid Input"

    return num + current

while True:
    s = input("Enter a number in words: ")
    print("In numbers:", words_to_number(s))
