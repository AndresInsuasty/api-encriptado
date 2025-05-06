from fastapi import FastAPI

app = FastAPI()

def cesar_cipher(text: str, shift: int = 5) -> str:
    """
    Aplica el cifrado César a un texto con un desplazamiento dado.
    Por defecto, el desplazamiento es 3.
    """
    result = []
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
        else:
            result.append(char)
    return ''.join(result)

@app.post("/encrypt/")
async def encrypt_word(palabra: str,clave: int = 5):
    """
    Endpoint que recibe una palabra y la devuelve cifrada con el cifrado César.
    """
    encrypted_word = cesar_cipher(palabra, clave)
    return {"original": palabra, "encrypted": encrypted_word}

def cesar_decipher(text: str, shift: int = 5) -> str:
    """
    Aplica el descifrado César a un texto con un desplazamiento dado.
    Por defecto, el desplazamiento es 3.
    """
    return cesar_cipher(text, -shift)

@app.post("/decrypt/")
async def decrypt_word(palabra: str, clave: int = 5):
    """
    Endpoint que recibe una palabra cifrada y la devuelve descifrada con el cifrado César.
    """
    decrypted_word = cesar_decipher(palabra, clave)
    return {"original": palabra, "decrypted": decrypted_word}

import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)