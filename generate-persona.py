#!/usr/bin/env python3
import random,string,names

def createPersona():

	# name and email alias generation
	firstName = names.get_first_name()
	lastName = names.get_last_name()
	name = firstName + lastName
	emailName = firstName + '.' + lastName
	emailRandomization = random.randint(1000000,99999999)
	email = emailName + '.' + str(emailRandomization) + '@protonmail.com'

	# password generation
	password = []
	characters = string.ascii_letters + string.digits + string.punctuation
	passwordlength = 24
	for x in range (passwordlength):
		password.append(random.choice(characters))
	password = (''.join(password))

	# prepare to write
	global profile
	profile = name + '\n' + password + '\n' + email + '\n'

def createProfile():

	# write to file
	with open("persona", "x") as file:
		data = file.write(profile)
		print(data)

def main():
	createPersona()
	createProfile()

if __name__ == "__main__":
    main()