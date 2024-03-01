from encryption import *
from Crypto.Random import get_random_bytes

key_des = b'01234567'
key_3des = b'0123456789012345'
key_aes = get_random_bytes(16)

plaintext = "Hola a todos esto es una prueba para el ejercicio de Block Cipher"

encrypted_des = encrypt_des(key_des, plaintext)
print("Cifrado DES:", encrypted_des)

encrypted_3des = encrypt_3des(key_3des, plaintext)
print("Cifrado 3DES:", encrypted_3des)

encrypted_aes = encrypt_aes(key_aes, plaintext)
print("Cifrado AES:", encrypted_aes)

# # Cifrado de imagen en modo CBC
# image_path = "./images/foto1.jpeg"  # Ruta de la imagen
# encrypted_image_cbc, iv = encrypt_image_cbc(key_aes, image_path)
# print("Imagen cifrada en modo CBC:", encrypted_image_cbc)

# # Cifrado de imagen en modo ECB
# encrypted_image_ecb = encrypt_image_ecb(key_aes, image_path)
# print("Imagen cifrada en modo ECB:", encrypted_image_ecb)
