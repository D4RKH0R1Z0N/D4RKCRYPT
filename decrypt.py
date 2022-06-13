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

file = input("Enter The File Name You Want To Decrypt : ")
verify_file(file)
key = input("Enter The Decyption Key : ")

with open(file, "rb") as filetodecrypt:
	file_data = filetodecrypt.read()
	file_data_dec = Fernet(key).decrypt(file_data)
	filetodecrypt.close()

file_ = file.replace(".py", "_DECRYPTED.py")
with open(file_, "wb") as decryptedfile:
	decryptedfile.write(file_data_dec)
	decryptedfile.close()

print("File Saved As", file_, "!")