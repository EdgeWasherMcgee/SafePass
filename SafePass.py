
# -*- coding: iso-8859-15 -*-
class SafePassCode():
    def login():
        while b == False:
            a = input("Here you have to enter the correct masterkey, if you don't already have one you can choose one you want to have as a masterkey.\nIf you want to know more, don't type anything and press enter")
            if a == '':
                print("To make sure your password is safely saved, you have to enter the correct password or else you won't be able to access the right passwords\n When you are typing the password in you have to be carefull so that you don't misspell anything.") 
            elif len(a) < 4:
                print("Your password has to be atleast 4 characters long")
            else:
                b = True
        keysafe(a)
        



    def keySafe(password):
        y = ''
        print("Here you can save your passwords and view those that you already have:")
        a = check("Password.txt")
        for b in range(a):
            print(a,b)
            y += "[%d] Somethin' \n" % (b + 1)
            
        print("Here's your saved passwords:\n%s" % y)
        c = input("Here's a list of things you can do, type the following things to execute the commans:\n1-9 = View one of you passwords\nn = create a new password\nd + [number] = delete a password")
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

        


    def Encryption_Method(password, login_pass):
        answer = ''
        open_file = open('Password.txt','a+')
        aSCII_List = []
        #Konvertera alla till siffror
        #Kör alla genom xor and 
        encrypted = []
        encrypted = New_Encrypting(password, login_pass)
        for place in range(len(encrypted)):
            answer = answer + str(encrypted[place - 1])
        answer = "["+ str(check("Password.txt")) +"]"+ answer + "\n"
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



    def New_Encrypting(password, login_pass):
        crypted = []
        ordered = []
        ordLogin = []
        for char in password:
            ordered.append(to_52_ord(char))
        for char in login_pass:
            ordLogin.append(to_52_ord(char))
        for spot in range(len(ordered)):
            ordered[spot] = ordered[spot] + ordLogin[spot % len(ordLogin)]
            Temp = rot(ordered[spot], "c0har")
            Temp = to_52_char(Temp)
            crypted.append(Temp)
        return crypted
            

        

    







def check(x):
    f = open(x, "r")
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
    num = num / 52
    num = num - int(num)
    num = num * 52
    num = int(num)
    num = abs(num)
    return num
    
        
    
        
def to_52_char(num):
    if num < 27:
        answer = num + 96
        answer = (answer)
    else:
        answer = num + 65 - 27
    return chr(answer)

def to_52_ord(char):
    num = ord(char)
    if num > 90:
        num = num - 96
    else:
        num = num - 65 + 27
    return num

def Decryption_Method(password ,login_password):
    ordered = []
    ordLogin = []
    crypted = []
    for char in password:
        ordered.append(to_52_ord(char))
    for char2 in login_password:
        ordLogin.append(to_52_ord(char2))
    for spot in range(len(ordered)):
        ordered[spot] = ordered[spot] - ordLogin[spot % len(ordLogin)]
        Temp = rot(ordered[spot], "c0har")
        Temp = to_52_char(Temp)
        crypted.append(Temp)
    return crypted
