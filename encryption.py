# Oscar Fernando López Barrios
# Carné 20679
# block-cipher-example

from Crypto.Util.Padding import pad
from Crypto.Cipher import DES3
from Crypto.Cipher import DES, AES

def encrypt_des(key, data):
    cipher = DES.new(key, DES.MODE_ECB)
    result = cipher.encrypt(pad(data.encode(), DES.block_size))
    return result

def encrypt_3des(key, data):
    cipher = DES3.new(key, DES3.MODE_ECB)
    return cipher.encrypt(pad(data.encode(), DES3.block_size))

def encrypt_aes(key, data):
    cipher = AES.new(key, AES.MODE_ECB)
    result = cipher.encrypt(pad(data.encode(), AES.block_size))
    return result

def encrypt_cbc(key, data):
    cipher = AES.new(key, AES.MODE_CBC)
    result = cipher.encrypt(pad(data, AES.block_size))
    return result

def encrypt_ecb(key, data):
    cipher = AES.new(key, AES.MODE_ECB)
    result = cipher.encrypt(pad(data, AES.block_size))
    return result