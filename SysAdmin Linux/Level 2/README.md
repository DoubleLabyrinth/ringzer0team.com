# ringzer0team.com -- SysAdmin Linux -- Level 2

## 1. Challenge

> Find architect password 
> 
> User: morpheus  
> Password: VNZDDLq2x9qXCzVdABbR1HOtz

Please connect to via SSH:

```bash
$ ssh morpheus@challenges.ringzer0team.com -p 10148
```

## 2. Solution

__Just the same as "Level 1" challenge.__

You should search and read every file you can read. 

But don't look around manually, please use `grep`.

```bash
$ grep "architect" -R /etc/ 2>/dev/null
```

Then you will find something:

```bash
morpheus@lxc-sysadmin:~$ grep "trinity" -R /etc/ 2>/dev/null
/etc/fstab:#//TheMAtrix/phone  /media/Matrix  cifs  username=architect,password=$(base64 -d "RkxBRy14QXFXMnlKZzd4UERCV3VlVGdqd05jMW5WWQo="),iocharset=utf8,sec=ntlm  0  0
/etc/group:challenger:x:1000:morpheus,trinity,architect,oracle,neo,cypher
/etc/group:architect:x:1003:
/etc/passwd:architect:x:1002:1003::/home/architect:/bin/bash
/etc/rcS.d/S07checkroot.sh:             # fail on older kernels on sparc64/alpha architectures due
/etc/subgid:architect:231072:65536
/etc/subuid:architect:231072:65536
/etc/init.d/checkroot.sh:               # fail on older kernels on sparc64/alpha architectures due
```

Please decode the base64 blob and you will see the flag:

```python
import base64
print(base64.b64decode('RkxBRy14QXFXMnlKZzd4UERCV3VlVGdqd05jMW5WWQo=').decode())
```
