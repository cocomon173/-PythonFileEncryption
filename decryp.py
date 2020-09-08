from cryptography.fernet import Fernet, InvalidToken
import os
key = b''
input_file = input("암호화 풀을 파일명(확장자 제외): ")+'.encrypted'
output_file = input("암호화 푼 파일명(확장자 포함): ")

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

