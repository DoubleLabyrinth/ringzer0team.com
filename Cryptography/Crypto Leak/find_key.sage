#!/usr/bin/env sage
file_size = '\x30\x50\x05\x00'
plaintext = bytearray('RIFF' + file_size)
ciphertext = bytearray('\x81\xa3\x7b\x2c\xcd\x36\xeb\x30')
stage = bytearray([plaintext[i] ^^ ciphertext[i] for i in range(8)])
stage = int(str(stage)[::-1].encode('hex'), 16)
print('seed = %d' % stage)

plaintext = bytearray('WAVEfmt ')
ciphertext = bytearray('\x08\xb5\x74\xdb\xaf\xb4\x74\xe6')
next_stage = bytearray([plaintext[i] ^^ ciphertext[i] for i in range(8)])
next_stage = int(str(next_stage)[::-1].encode('hex'), 16)
# print('next_stage = %d' % next_stage)

A = MatrixSpace(GF(2), 64, 64)()
B = MatrixSpace(GF(2), 64, 1)()
for i in range(64):
    tmp_stage = ((next_stage << (64 - i)) | (stage >> i)) & (2 ^ 64 - 1)
    for j in range(64):
        if tmp_stage & 2 ^ j:
            A[i, j] = 1
        else:
            A[i, j] = 0
    if (next_stage << (64 - i)) & 2 ^ 64:
        B[i, 0] = 1
    else:
        B[i, 0] = 0
X = A.inverse() * B

key = 0
for i in range(64):
    key += int(X[i, 0]) * 2 ^ i
print('key = %d' % key)

