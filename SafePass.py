def keySafe():
    username = input("Input your username here!\n")
    password = input("Your password you wanna save!\n")
    Encryption_Method(password)
    print("Now your password has been encrypted and saved!")



def UserName_Saving(username):
    f = open("Usernames.txt", "a+")
    f.write('[' + str(check("Usernames.txt", "a+"))+ ']' + username + "\n")
    f.close


def pairing(place):
    fU = open("Usernames.txt","r")
    fP = open("Password.txt","r")
    lineU = fU.readlines()
    lineU = lineU[place]
    lineP = fP.readlines()
    lineP = lineP[place]
    lineU.close()
    lineP.close()

    


def Encryption_Method(password):
    answer = ''
    open_file = open('Password.txt','a+')
    aSCII_List = []
    #Konvertera alla till siffror
    for pickup in password:
        aSCII_List.append(to_52_ord(pickup))
    #Kör alla genom xor and 
    encrypted = []
    for binary in aSCII_List:
        binary = binary + 7
        encrypted.append(binary ^ 253)
    for place in range(len(encrypted)):
        answer = answer + str(encrypted[place - 1])
    answer = "["+ str(check(open_file)) +"]"+ answer + "\n"
    open_file.write(answer)
    open_file.close()





def unpack(line):
    x = 0
    chars = []
    for char in line:
        if x > 2 and x < len(line) - 1:
            chars.append(char)
        x = x + 1
    return chars



def New_Encrypting(password):
    crypted = []
    ordered = []
    for char in password:
        ordered.append(to_52_ord(char))
    for spot in range(len(ordered)):
        Temp = rot(ordered[spot], "char")
        crypted.append(Temp * 2)
    return crypted
        

        

    
   







def check(x,y):
    f = open(x,y)
    count = len(f.readlines())
    f.close()
    return count
#Count = Antal rader
#f = Filen öppnad
#lines = Samma sak som count avsedd att anpassa hur många gånger man ska köra loopen
#read = Läser en rad och anpassas vilken rad av 'lines'
#char = En bokstav i varje rad

            

#Ska göra så om att ett nummer högre än 52 tas bort 52 från talet, och lägre än 0 adderas med 52
#Ex: 56 blir till 4, -3 blir 49
def rot(num, direction):
    if num > 104:
        num = num / 52
        num = num - int(num)
        num = num * 52
        num = int(num)
    elif num > 52:
        num = num - 52
    elif num < 0:
        num = num + 52
    if direction == "ord":
        num = to_52_ord(num)
    elif direction == "char":
        num = to_52_char(num)
    return num
    
        
    
        
def to_52_char(num):
    if num < 27:
        answer = num + 96
    else:
        answer = num + 65 - 27
    return answer

def to_52_ord(char):
    num = ord(char)
    if num > 90:
        num = num - 96
    else:
        num = num - 65 + 27
    return num

    
