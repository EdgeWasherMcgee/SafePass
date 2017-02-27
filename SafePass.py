
# -*- coding: iso-8859-15 -*-
class SafePassCode():
	def login(self):
		b = False
		while b == False:
		    a = str(input("Here you have to enter the correct masterkey, if you don't already have one you can choose one you want to have as a masterkey.\nIf you want to know more, don't type anything and press enter\n"))
		    if a == '':
			print("To make sure your password is safely saved, you have to enter the correct password or else you won't be able to access the right passwords.\nWhen you are typing the password in you have to be carefull so that you don't misspell anything.") 
		    elif len(a) < 4:
			print("Your password has to be atleast 4 characters long")
		    else:
			b = True
		self.keysafe(a)


	def load(self):
		a = 0


	def keySafe(self, login_pass):
		y = ''
		print("Here you can save your passwords and view those that you already have:")
		a = self.check("Password.txt")
		for b in range(a):
		    print(a,b)
		y = self.unpack_U()
		print("Here's your saved passwords:\n%s" % y)
		c = str(input("Here's a list of things you can do, type the following things to execute the commands:\n\n0-9 = View one of you passwords\n\nn = create a new password\n\nd + [number] = delete a password\n\n"))
		if c == in (0,1,2,3,4,5,6,7,8,9):
			decrypted = self.Decryption_Method(self.unpack(c), login_pass)
			print(decrypted)
		elif c == 'n':
			new_name = str(input('Type the name you want your password to have:\n'))
			new_pass = str(input('Type the password you want to save:\n'))
			self.Encryption_Method(new_pass, login_pass)
			print("Now your password has been encrypted and saved!\n\n\n\n")
			self.UserName_Saving(new_name)
			self.keySafe(login_pass)
	#	elif c[0] == d:



	def delete(self,line):
		fP = open('Password.txt','w+')
		fU = open ('Usernames.txt','w+')
		aP = fP.readlines()
		aU = fU.readlines()
		print(aU,aP)
		aP.remove(aP[line])	
		aU.remove(aU[line])
		fP.write(aP)
		fU.write(aU)	
		aU.close()
		aP.close()
		

	
	def UserName_Saving(self,username):
		f = open("Usernames.txt", "a+")
		f.write('[' + str(self.check("Usernames.txt"))+ ']' + username + "\n")
		f.close


	def Encryption_Method(self,password, login_pass):
		answer = ''
		open_file = open('Password.txt','a+')
		aSCII_List = []
		#Konvertera alla till siffror
		#Kör alla genom xor and 
		encrypted = []
		encrypted = self.new_Encrypting(password, login_pass)
		for place in range(len(encrypted)):
		    answer = answer + (encrypted[place])
		answer = "["+ str(self.check("Password.txt")) +"]"+ answer + "\n"
		open_file.write(answer)
		open_file.close()





	def unpack(self,line):
		x = 0
		chars = []
                f = open('Password.txt','r')
                temp = f.readlines()
                line = temp[line]
		for char in line:
		    if x > 2 and x < len(line) - 1:
			chars.append(char)
		    x = x + 1
		f.close()
		return chars



	def unpack_U(self):
		f = open("Usernames.txt",'r')
		a = f.readlines()
		d = ''
		for y in range(len(a)):
			d = d + a[y] + '\n'
		d.strip('[],')
		f.close()	
		return(d)	


	def new_Encrypting(self,password, login_pass):
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
	#f = Filen öppnad
	#lines = Samma sak som count avsedd att anpassa hur många gånger man ska köra loopen
	#read = Läser en rad och anpassas vilken rad av 'lines'
	#char = En bokstav i varje rad


		    
		    
		    
		    

	#Ska göra så om att ett nummer högre än 52 tas bort 52 från talet, och lägre än 0 adderas med 52
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






