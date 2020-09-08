from cryptography.fernet import Fernet
import os
key = Fernet.generate_key() 
with open("key.key",'wb') as f:
    f.write(key)
input_file = input("File You going to encrypt(With File extension): ")
output_file = input("OutPut file name(Without File extension): ")+'.encrypted'

with open(input_file, 'rb') as f:
    data = f.read()  

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted) 
    os.remove(input_file)
