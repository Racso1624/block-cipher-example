from Crypto.Cipher import DES, AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Cipher import DES3
from PIL import Image

# Función de cifrado DES
def encrypt_des(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(pad(plaintext.encode(), DES.block_size))

# Función de cifrado 3DES
def encrypt_3des(key, plaintext):
    cipher = DES3.new(key, DES3.MODE_ECB)
    return cipher.encrypt(pad(plaintext.encode(), DES3.block_size))

# Función de cifrado AES
def encrypt_aes(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(plaintext.encode(), AES.block_size))

# Función de cifrado de imagen en modo CBC
def encrypt_image_cbc(key, image_path):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    image = Image.open(image_path)
    image_data = image.tobytes()
    encrypted_data = cipher.encrypt(pad(image_data, AES.block_size))
    return encrypted_data, iv

# Función de cifrado de imagen en modo ECB
def encrypt_image_ecb(key, image_path):
    cipher = AES.new(key, AES.MODE_ECB)
    image = Image.open(image_path)
    image_data = image.tobytes()
    encrypted_data = cipher.encrypt(pad(image_data, AES.block_size))
    return encrypted_data

# Clave para cifrado
key_des = b'01234567'  # Clave de 8 bytes para DES
key_3des = b'0123456789012345'  # Clave de 16 bytes para 3DES
key_aes = get_random_bytes(16)  # Clave de 16 bytes para AES

# Texto plano
plaintext = "Hola a todos esto es una prueba para el ejercicio de Block Cipher"

# Cifrado DES
encrypted_des = encrypt_des(key_des, plaintext)
print("Cifrado DES:", encrypted_des)

# Cifrado 3DES
encrypted_3des = encrypt_3des(key_3des, plaintext)
print("Cifrado 3DES:", encrypted_3des)

# Cifrado AES
encrypted_aes = encrypt_aes(key_aes, plaintext)
print("Cifrado AES:", encrypted_aes)

# # Cifrado de imagen en modo CBC
# image_path = "./images/foto1.jpeg"  # Ruta de la imagen
# encrypted_image_cbc, iv = encrypt_image_cbc(key_aes, image_path)
# print("Imagen cifrada en modo CBC:", encrypted_image_cbc)

# # Cifrado de imagen en modo ECB
# encrypted_image_ecb = encrypt_image_ecb(key_aes, image_path)
# print("Imagen cifrada en modo ECB:", encrypted_image_ecb)
