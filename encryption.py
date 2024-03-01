from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Cipher import DES3
from PIL import Image
from Crypto.Cipher import DES, AES

def encrypt_des(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(pad(plaintext.encode(), DES.block_size))

def encrypt_3des(key, plaintext):
    cipher = DES3.new(key, DES3.MODE_ECB)
    return cipher.encrypt(pad(plaintext.encode(), DES3.block_size))

def encrypt_aes(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(plaintext.encode(), AES.block_size))

def encrypt_image_cbc(key, image_path):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    image = Image.open(image_path)
    image_data = image.tobytes()
    encrypted_data = cipher.encrypt(pad(image_data, AES.block_size))
    return encrypted_data, iv

def encrypt_image_ecb(key, image_path):
    cipher = AES.new(key, AES.MODE_ECB)
    image = Image.open(image_path)
    image_data = image.tobytes()
    encrypted_data = cipher.encrypt(pad(image_data, AES.block_size))
    return encrypted_data