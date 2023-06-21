from cryptography.fernet import Fernet
import os.path

class DarkCrypt:
	def __init__(self, file, dec_key=None) -> None:
		self.file = file
		self.key = dec_key
		self.message = ''

	def isVerified(self) -> bool:
		conditions = [len(self.file) >= 4, self.file.endswith('.py'), os.path.isfile(self.file)]
		if all(conditions):
			return True
		print("[-] File Error, The file must end with '.py' and have a minimum of 3 letters, and it must exist.")
		exit()

	def gen_key(self):
		key = Fernet.generate_key()
		with open('key4decoding.key', 'wb') as f:
			f.write(key)
			f.close()
			self.message += "[+] Saved key file as 'key4decoding.key'\n"
		return key

	def encrypt_it(self) -> bool:
		key = self.gen_key()
		with open(self.file, 'rb') as encryptingFile:
			data = encryptingFile.read()
			encrypted_data = Fernet(key).encrypt(data)
			encryptingFile.close()
			self.message += "[+] Encrypted File Content Successfully!\n"

		new_file_name = self.file.replace('.py', '_ENC.py')
		with open(new_file_name, 'wb') as savingEnc:
			savingEnc.write(encrypted_data)
			savingEnc.close()
			self.message += "[+] Saved Encrypted File Successfully!\n"

		return True

	def decrypt_it(self) -> bool:
		with open(self.file, 'rb') as target_dec_file:
			data = target_dec_file.read()
			decrypted_data = Fernet(self.key).decrypt(data)
			target_dec_file.close()
			self.message += '[+] Decrypted File Content Successfully!\n'

		new_file_name = self.file.replace('.py', '_DEC.py')
		with open(new_file_name, 'wb') as decrypted_file:
			decrypted_file.write(decrypted_data)
			decrypted_file.close()
			self.message += '[+] Saved Decrypted File Successfully!\n'

		return True

	def enc(self) -> None:
		if self.isVerified():
			if self.encrypt_it():
				print(self.message)

	def dec(self) -> None:
		if self.isVerified():
			if self.decrypt_it():
				print(self.message)


########################################################
##                 User Interactions                  ##
########################################################

filename = str(input("Enter Filename: "))

tool = DarkCrypt(filename)

options: str = '''
DarkCrypt

[1] Encrypt
[2] Decrypt
'''

print(options)

user_option = int(input("\nSelect an Option: "))

if user_option == 1:
	tool.enc()
elif user_option == 2:
	dec_key = str(input("\nEnter Your Decrypt Key: "))
	tool = DarkCrypt(filename, dec_key)
	try:
		tool.dec()
	except ValueError:
		print("[-] Malformed Key!")
else:
	print("[-] Option does not exist!")