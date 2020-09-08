from cryptography.fernet import Fernet
import os
key = Fernet.generate_key() 
with open("key.key",'wb') as f:
    f.write(key)
input_file = input("암호화 할 파일명(확장자 포함): ")
output_file = input("암호화파일명(확장자 제외): ")+'.encrypted'

with open(input_file, 'rb') as f:
    data = f.read()  

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted) 
    os.remove(input_file)
