# Cryptography - File recovery

## 1. Challenge

Only two files: `flag.enc` and `private.pem`. Please goto [https://ringzer0team.com/challenges/49](https://ringzer0team.com/challenges/49) to download.

## 2. Solution

Open `private.pem` and you will see an RSA private key with PEM format.

So, just use `openssl` and this RSA private key to decrypt `flag.enc` and you will see the flag.

```bash
$ openssl rsautl -decrypt -inkey private.pem -in flag.enc
```
