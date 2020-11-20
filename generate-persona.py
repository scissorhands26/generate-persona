#!/usr/bin/env python3
import random,string,names

class alias:

	def __init__(self, fname, lname):
		self.fname = fname
		self.lname = lname
		self.name = fname + ' ' + lname
		self.email = fname + '.' + lname + '@protonmail.com'
		self.password = createPassword()

def createPassword():
	password = []
	characters = string.ascii_letters + string.digits + string.punctuation
	passwordlength = 24
	for x in range (passwordlength):
		password.append(random.choice(characters))
	password = (''.join(password))
	return password

def createProfile():
	
	fname = names.get_first_name()
	lname = names.get_last_name()
	
	profile = alias(fname, lname)

	person = profile.name + '\n' + profile.email + '\n' + profile.password + '\n'
	return person

def createPersona(person):

	with open("persona", "w") as file:
		data = file.write(createProfile())
		print(data)

def main():
	createPersona(createProfile())

if __name__ == "__main__":
	main()
