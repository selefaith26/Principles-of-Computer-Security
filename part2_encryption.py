def encrypt(text):
    return text[::-1]

def decrypt(text):
    return text[::-1]

def apply_encryption(username, text):
    if len(username) % 2 == 0:
        return encrypt(text)
    else:
        return encrypt(encrypt(text))

def apply_decryption(username, text):
    if len(username) % 2 == 0:
        return decrypt(text)
    else:
        return decrypt(decrypt(text))