from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import os

# Definir la clave y el texto a encriptar
secret_key = "FGa62cSP505X6AiQdJI3h2N8LBoXMNyB".encode('utf-8')
password = "nova123".encode('utf-8')

# Generar un IV aleatorio
iv = os.urandom(AES.block_size)

# Crear el objeto de cifrado AES en modo CBC
cipher = AES.new(secret_key, AES.MODE_CBC, iv)

# Encriptar la contraseña
encrypted_password = cipher.encrypt(pad(password, AES.block_size))

# Concatenar IV y contraseña encriptada, luego codificar en base64
encrypted_data = base64.b64encode(iv + encrypted_password).decode('utf-8')
print("Contraseña encriptada para enviar en Postman:", encrypted_data)
