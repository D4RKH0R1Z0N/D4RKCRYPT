from sys import exit
from cryptography.fernet import Fernet
import pyfiglet as figlet

banner = figlet.figlet_format('D4RKCRYPT', font = 'small')
print(banner, "Made by D4RKH0R1Z0N (https://github.com/D4RKH0R1Z0N)")

def verify_file(file):
	filetype = ".py"
	if len(file) < 4:
		print("Invalid File! Please Enter a File with more than 3 letters")
		program()
	elif filetype in file:
		print("Valid File!")
	else:
		print("Invalid File! Please use a file with '.py' extension")
		program()

file = input("Enter The File Name You Want To Encrypt : ")
verify_file(file)
key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
	thekey.write(key)
	thekey.close()

print("Key saved to file as 'thekey.key'")

with open(file, "rb") as filetoencrypt:
	file_data = filetoencrypt.read()
	file_data_enc = Fernet(key).encrypt(file_data)
	filetoencrypt.close()

file_ = file.replace(".py", "_ENCRYPTED.py")
with open(file_, "wb") as encryptedfile:
	encryptedfile.write(file_data_enc)
	encryptedfile.close()

print("File Saved As", file_, "!")
with open(file, "r") as key_file:
	key_ = key_file.read()
	key_file.close()
print("Important! Remeber the Key or else you won't be able to use this file! its almost Impossible to Decrypt!")
print("""
Here's the Key Again : """, key_, """ Make Sure to Remeber!""")
print("If you forgot to Copy the Key! Its save as thekey.key you can Copy it from There!")