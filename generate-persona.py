#!/usr/bin/env python3
import random,string,names

class alias:

	def __init__(self, fname, lname):
		self.fname = fname
		self.lname = lname
		self.name = fname + ' ' + lname + '\n'
		self.email = fname + '.' + lname + '@protonmail.com\n'
		self.password = createPassword()

def createPassword():
	password = []
	characters = string.ascii_letters + string.digits + string.punctuation
	passwordlength = 24
	for x in range (passwordlength):
		password.append(random.choice(characters))
	password = (''.join(password)) + '\n'
	return password

def createProfile():

	profile = alias(names.get_first_name(), names.get_last_name())
	return profile

def createPersona(profile):

	with open("persona", "w") as file:
		file.write(profile.name)
		file.write(profile.email)
		file.write(profile.password)

def main():
	createPersona(createProfile())

if __name__ == "__main__":
	main()
