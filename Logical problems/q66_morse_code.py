#Translate to and from morse code

def to_morse(str):
    d = {
            "A":".-","B":"-...","C":"-.-.","D":"-..","E":".",
            "F":"..-.","G":"--.","H":"....","I":"..","J":".---",
            "K":"-.-","L":".-..","M":"--","N":"-.","O":"---",
            "P":".--.","Q":"--.-","R":".-.","S":"...","T":"-",
            "U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..",
            " ":"....."
        }
    res = ""  
    morse = ""
    word=""
    for i in range(len(str)):
        if morse == ".....":
            res+=word
            word=""
            morse=""
            continue
        
        if i == ' ':
            char = d[morse]
            word+=char
            morse=""
            continue
        print(str[i])
        morse+=str[i]
    print(res)

def from_morse(str):
    d = {
            "A":".-","B":"-...","C":"-.-.","D":"-..","E":".",
            "F":"..-.","G":"--.","H":"....","I":"..","J":".---",
            "K":"-.-","L":".-..","M":"--","N":"-.","O":"---",
            "P":".--.","Q":"--.-","R":".-.","S":"...","T":"-",
            "U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..",
            " ":"....."
        }
    res = ""  
    morse = ""
    word=""
    
    
s1 = ".--- --- .... -. ..... ..-. ..... -.- . -. -. . -.. -.--"
# s1 = "Barack Obama"
if s1[0].isalpha():
    print("Given Alphabets to Morse Code is: ")
    to_morse(s1)
else:
    print("Given Morse Code to alphabets is: ")
    from_morse(s1)