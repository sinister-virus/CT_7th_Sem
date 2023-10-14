from des import DES


#Main Program DES
number = int(input("Enter Number to Encrypt: ")) #123456
key = int(input("Enter Key for Encryption: ")) #167
des = DES(key)
ciphertext = des.encrypt_number(number)
decrypted = des.decrypt_number(ciphertext)
print('Number:', number)
print('Encrypted:', ciphertext)
print('Decrypyed: ', decrypted)