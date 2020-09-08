from cryptography.fernet import Fernet, InvalidToken
import os
key = b''
input_file = input("File You going to decrypt(Without File extension): ")+'.encrypted'
output_file = input("Out Put file name(With File extension): ")

with open("key.key",'rb') as f:
    key = f.read()

with open(input_file, 'rb') as f:
    data = f.read() 

fernet = Fernet(key)
try:
    decrypted = fernet.decrypt(data)

    with open(output_file, 'wb') as f:
        f.write(decrypted)
        os.remove('key.key')
        os.remove(input_file)
except InvalidToken as e:
    print("Invalid Key - Unsuccessfully decrypted")
