
# -*- coding: iso-8859-15 -*-
import getpass
class SafePassCode():
        def login(self):
                b = True
                while b:
                    print("\n\n\nHere you have to enter your masterkey\n\nIf you don't already have one you can choose the one you want to have")
                    print("Type your masterkey and press enter, if you want to know more, leave the feild open and press enter")
                    a = getpass.getpass()
                    print("\n\n\n")
                    if a == '':
                        print("To make sure your password is safely saved, you have to enter the correct password or else you won't be able to access the right passwords.\nWhen you are typing the password in you have to be carefull so that you don't misspell anything.") 
                    elif len(a) < 4:
                        print("Your password has to be atleast 4 characters long")
                    else:
                        b = False
                self.keySafe(a)

        def keySafe(self, login_pass):
                y = ''
                a = self.check("Password.txt")
                y = self.unpack_U()
                print("Here's your saved passwords:\n%s" % y)
                c = input("Here's a list of things you can do, type the following things to execute the commands:\n\n0-9 = View one of you passwords\n\nn = create a new password\n\nd + [number] = delete a password\n\n")
                elif c in ('0','1','2','3','4','5','6','7','8','9'):
                        decrypted = self.Decryption_Method(self.unpack(int(c)), login_pass)
                        d = ''
                        for x in decrypted:
                                d = d + x
                        print('Decrypted password:\n%s \n\n\n' % d)
                        self.keySafe(login_pass)
                elif c == 'n':
                        new_name = input('Type the name you want your password to have:\n')
                        new_pass = getpass.getpass('Type the password you want to save:\n')
                        self.Encryption_Method(new_pass, login_pass)
                        print("Now your password has been encrypted and saved!\n\n\n\n")
                        self.UserName_Saving(new_name)
                        self.keySafe(login_pass)
                elif c[0] == 'd':
                        self.delete(c[1])
                        self.keySafe(login_pass)
                elif c == '':
                        print('End')
        #       elif c[0] == d:



        def delete(self,line):
                fPr = open('Password.txt','r')     
                fUr = open('Usernames.txt','r')
                aP = fPr.readlines()
                aU = fUr.readlines()
                aP.pop(int(line))
                aU.pop(int(line))
                y = ''
                for x in range(len(aU)):
                      y = y + aU[x]
                d = ''
                for x in range(len(aP)):
                      d = d + aP[x]
                fP = open('Password.txt','w+')
                fU = open ('Usernames.txt','w+') 
                fP.write(d)
                fU.write(y)    
                fUr.close()
                fPr.close()
                fP.close()
                fU.close()

        
        def UserName_Saving(self,username):
                f = open("Usernames.txt", "a+")
                f.write(username +  "\n")
                f.close


        def Encryption_Method(self,password, login_pass):
                answer = ''
                open_file = open('Password.txt','a+')
                aSCII_List = []
                #Konvertera alla till siffror
                #Kor alla genom xor and 
                encrypted = []
                encrypted = self.new_Encrypting(password, login_pass)
                for place in range(len(encrypted)):
                    answer = answer + (encrypted[place])
                answer = answer + '\n'
                open_file.write(answer)
                open_file.close()





        def unpack(self,line):
                x = 0
                chars = []
                f = open('Password.txt','r')
                temp = f.readlines()
                line = temp[line]
                for char in line:
                        chars.append(char)
                f.close()
                chars = chars[0:(len(chars)-1)]
                return chars



        def unpack_U(self):
                f = open("Usernames.txt",'r')
                a = f.readlines()
                d = ''
                for y in range(len(a)):
                        d = d +'[' + str(y) + ']' +  a[y]+ '\n'
                f.close()       
                return(d)       


        def new_Encrypting(self, password, login_pass):
                crypted = []
                ordered = []
                ordLogin = []
                for char in password:
                    ordered.append(self.to_52_ord(char))
                for char in login_pass:
                    ordLogin.append(self.to_52_ord(char))
                for spot in range(len(ordered)):
                    ordered[spot] = ordered[spot] + ordLogin[spot % len(ordLogin)]
                    Temp = self.rot(ordered[spot])
                    Temp = self.to_52_char(Temp)
                    crypted.append(Temp)
                return crypted
                    



        def check(self,x):
                f = open(x, "r")
                count = len(f.readlines())
                f.close()
                return count
        #Count = Antal rader
        #f = Filen oppnad
        #lines = Samma sak som count avsedd att anpassa hur manga ganger man ska kora loopen
        #read = Laser en rad och anpassas vilken rad av 'lines'
        #char = En bokstav i varje rad


                    
                    
                    
                    

        #Ska gora sa om att ett nummer hogre an 52 tas bort 52 fran talet, och lagre an 0 adderas med 52
        #Ex: 56 blir till 4, -3 blir 49
        def rotnotworking(self,num, direction):
                num = num / 52.
                num = num - int(num)
                num = num * 52.
                num = abs(num)
            

        def rot(self, num):
                return ((num - 1) % 52) + 1
            
                
        def to_52_char(self,num):
            if num < 27:
                answer = num + 96
                answer = (answer)
            else:
                answer = num + 65 - 27
            return chr(answer)

        def to_52_ord(self,char):
            num = ord(char)
            if num > 90:
                num = num - 96
            else:
                num = num - 65 + 27
            return num

        def Decryption_Method(self, password,  login_password):
            ordered = []
            ordLogin = []
            crypted = []
            for char in password:
                ordered.append(self.to_52_ord(char))
            for char2 in login_password:
                ordLogin.append( self.to_52_ord( char2 )  )
            for spot in range(len(ordered)):
                ordered[spot] = ordered[spot] - ordLogin[spot % len(ordLogin)]
                Temp = self.rot(ordered[spot])
                Temp = self.to_52_char(Temp)
                crypted.append(Temp)
            return crypted

o = SafePassCode()

# vím: tabexpand
