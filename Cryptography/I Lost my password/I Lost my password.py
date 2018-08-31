#!/usr/bin/env python3
from Crypto.Cipher import AES
import base64

def decrypt_cpassword(s : str):
    padding = '=' * (4 - len(s) % 4)
    padding = padding if len(padding) != 4 else ''
    cpassword_base64 = s + padding
    cpassword_blob = base64.b64decode(cpassword_base64)

    key = b'\x4e\x99\x06\xe8\xfc\xb6\x6c\xc9' \
          b'\xfa\xf4\x93\x10\x62\x0f\xfe\xe8' \
          b'\xf4\x96\xe8\x06\xcc\x05\x79\x90' \
          b'\x20\x9b\x09\xa4\x33\xb6\x6c\x1b'
    cipher = AES.new(key, AES.MODE_CBC, iv = b'\x00' * 16)

    plaintext_blob = cipher.decrypt(cpassword_blob)
    plaintext = plaintext_blob[0:-plaintext_blob[-1]]
    return plaintext.decode('utf-16le')


print(decrypt_cpassword('PCXrmCkYWyRRx3bf+zqEydW9/trbFToMDx6fAvmeCDw'))
