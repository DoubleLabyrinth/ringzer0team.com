# Cryptography - Martian message part 2

## 1. Challenge

```
I think that's the key "fselkladfklklakl" 

KDERE2UNX1W1H96GYQNUSQT1KPGB
```

## 2. Solution

This is a standard Vigenere cipher. So just decrypt message by the key given.

```python
#!/usr/bin/env python3

Alphabet = 'abcdefghijklmnopqrstuvwxyz'
AlphabetTrans = { Alphabet[i] : i for i in range(len(Alphabet)) }
AlphabetTrans.update({ Alphabet[i].upper() : i for i in range(len(Alphabet)) })

'''
def Encrypt(msg : str, key : str):
    enc = []
    key_len = len(key)
    i = 0
    for c in msg:
        if c.isupper():
            enc.append(Alphabet[(AlphabetTrans[c] + AlphabetTrans[key[i % key_len]]) % 26].upper())
            i += 1
        elif c.islower():
            enc.append(Alphabet[(AlphabetTrans[c] + AlphabetTrans[key[i % key_len]]) % 26])
            i += 1
        else:
            enc.append(c)
    return ''.join(enc)
'''

def Decrypt(enc : str, key : str):
    msg = []
    key_len = len(key)
    i = 0
    for c in enc:
        if c.isupper():
            msg.append(Alphabet[(AlphabetTrans[c] - AlphabetTrans[key[i % key_len]]) % 26].upper())
            i += 1
        elif c.islower():
            msg.append(Alphabet[(AlphabetTrans[c] - AlphabetTrans[key[i % key_len]]) % 26])
            i += 1
        else:
            msg.append(c)
    return ''.join(msg)

print(Decrypt('KDERE2UNX1W1H96GYQNUSQT1KPGB', 'fselkladfklklakl'))
```

