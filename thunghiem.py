import binascii
import os
table = open("code.txt","r")
table = table.read()
again = 'yes'
while again == 'yes':
	print("Table:\n",table)
	system = int(input("1.Bina\n2.Decimal\n3.Hexa\nYour choice: "))
	if system == 1:
		bit = int(input("Code: "))
		while len(bit) % 8 != 0:
			print("Your binary code is must be divisible by 8.!!!")
			bit = input("Code: ")
		n = int(bit,2)
		code = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
		print("Translate: ",code)
	elif system == 2:
		bit = input("Code: ")
		code = chr(int(bit))
		print("Translate: ",code)
	else:
		bit = input("Code: ")
		bit = bit.lower()
		code = bytearray.fromhex(bit).decode() 
		print("Translate: ",code)
	again = input("Again? (yes ): ")
table.close()
