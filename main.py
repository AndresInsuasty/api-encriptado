from fastapi import FastAPI
import hashlib
from fastapi import HTTPException

app = FastAPI()

#################################### Cifrado César ####################################
def cesar_cipher(text: str, shift: int = 5) -> str:
    """
    Aplica el cifrado César a un texto con un desplazamiento dado.
    Por defecto, el desplazamiento es 5.
    """
    result = []
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
        else:
            result.append(char)
    return ''.join(result)

@app.post("/codificar/",tags=["Cifrado"])
async def encrypt_word(palabra: str,clave: int = 5):
    """
    Endpoint que recibe una palabra y la devuelve cifrada con el cifrado César.
    """
    encrypted_word = cesar_cipher(palabra, clave)
    return {"original": palabra, "encrypted": encrypted_word}

def cesar_decipher(text: str, shift: int = 5) -> str:
    """
    Aplica el descifrado César a un texto con un desplazamiento dado.
    Por defecto, el desplazamiento es 5.
    """
    return cesar_cipher(text, -shift)

@app.post("/decodificar/",tags=["Cifrado"])
async def decrypt_word(palabra: str, clave: int = 5):
    """
    Endpoint que recibe una palabra cifrada y la devuelve descifrada con el cifrado César.
    """
    decrypted_word = cesar_decipher(palabra, clave)
    return {"original": palabra, "decrypted": decrypted_word}

@app.post("/encriptar/",tags=["Encriptado"])
async def sha256_encrypt(palabra: str):
    """
    Endpoint que recibe una palabra y devuelve su hash SHA-256.
    """
    sha256_hash = hashlib.sha256(palabra.encode()).hexdigest()
    return {"original": palabra, "sha256_hash": sha256_hash}

@app.post("/encriptar/verify/",tags=["Encriptado"])
async def sha256_verify(palabra: str, hash: str):
    """
    Endpoint que verifica si una palabra coincide con un hash SHA-256 dado.
    """
    sha256_hash = hashlib.sha256(palabra.encode()).hexdigest()
    if sha256_hash == hash:
        return {"match": True, "message": "La palabra coincide con el hash proporcionado."}
    else:
        raise HTTPException(status_code=400, detail="La palabra no coincide con el hash proporcionado.")


import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)