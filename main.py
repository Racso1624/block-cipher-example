# Oscar Fernando López Barrios
# Carné 20679
# block-cipher-example

from encryption import *
from Crypto.Random import get_random_bytes

key_des = b'LlaveDES'
key_3des = b'LlaveTripleDES12'
key_aes = get_random_bytes(16)

text = "Hola a todos esto es una prueba para el ejercicio de Block Cipher"

encrypted_des = encrypt_des(key_des, text)
print("Resultado de Cifrado DES:", encrypted_des)

encrypted_3des = encrypt_3des(key_3des, text)
print("Resultado de Cifrado 3DES:", encrypted_3des)

encrypted_aes = encrypt_aes(key_aes, text)
print("Resultado de Cifrado AES:", encrypted_aes)

image_path_1 = "./images/foto1.jpeg"
image_path_2 = "./images/Logo-UVG.webp"

image_1 = Image.open(image_path_1)
image_data_1 = image_1.tobytes()

image_2 = Image.open(image_path_2)
image_data_2 = image_2.tobytes()

image_result_cbc_1 = encrypt_cbc(key_aes, image_data_1)
image_result_ecb_1 = encrypt_ecb(key_aes, image_data_1)

image_result_cbc_2 = encrypt_cbc(key_aes, image_data_2)
image_result_ecb_2 = encrypt_ecb(key_aes, image_data_2)

with open("resultado_cbc_1.jpg", "wb") as f:
    f.write(image_result_cbc_1)
with open("resultado_ecb_1.jpg", "wb") as f:
    f.write(image_result_ecb_1)

with open("resultado_cbc_2.jpg", "wb") as f:
    f.write(image_result_cbc_2)
with open("resultado_ecb_2.jpg", "wb") as f:
    f.write(image_result_ecb_2)
