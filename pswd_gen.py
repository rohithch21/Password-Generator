import random
import hashlib



def password_generator2():
	
	password_list = []
	no_of_char = int(input("Enter no. of characters for the password: "))
	psswd = ['None'] * no_of_char
	count = 0
	while count < no_of_char:
		random_number = random.randint(1,7)
		corresponding_set = {1 : Dictionary(33,47), 2:Dictionary(48,57), 3:Dictionary(58,64), 4:Dictionary(65,90), 5:Dictionary(91,96), 6:Dictionary(97,122), 7:Dictionary(123,126)} 
		psswd[count] = corresponding_set[random_number]
		count += 1
	

	password = "".join(psswd)
	password = hash_pswd(password)
	if password in password_list:
		print("Password exists! Try again")
		password_generator2()
	else:
		password_list.append(password)
	print("Password is: ",password)
	
		
def Dictionary(range1,range2):
		another_random = random.randint(range1,range2)
		for i in range(range1,another_random+1):
			ch = chr(i)
		return ch
def hash_pswd(password):
	hash_obj = hashlib.sha512(password.encode())
	hash_digest = hash_obj.hexdigest()
	return hash_digest

password_generator2()
