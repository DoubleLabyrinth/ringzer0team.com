#!/usr/bin/env python3
import base64, randcrack

rc = randcrack.RandCrack()
with open('message.txt') as f:
    c = f.read()

c = c.replace('---Total Secure Message Encrypter V1.0 ---', '')
c = c.replace('++ Format: ringzer0team ++', '')
c = c.replace('---End Total Secure Message Encrypter Message---', '')
c = c.replace(' ', '')
c = c.replace('\n', '')
c = base64.b64decode(c).decode()

cb = bytes.fromhex(c + '0' if len(c) % 2 != 0 else '')
i = cb.find(b'[')
j = cb.find(b']')
assert(i != -1 and j != -1)
pseudo_random_known = cb[i:j + 1].decode()
pseudo_random_known = pseudo_random_known.replace('L', '')
pseudo_random_known = eval(pseudo_random_known)
for i in range(624):
    rc.submit(pseudo_random_known[i])
for i in range(624, len(pseudo_random_known)):
    assert(rc.predict_getrandbits(32) == pseudo_random_known[i])
c = c[2 * (j + 1):]

key = ''
for i in range(10):
    key += str(rc.predict_getrandbits(32))
m = int(key) ^ int(c)
print(m.to_bytes((m.bit_length() + 7) // 8, 'big'))
