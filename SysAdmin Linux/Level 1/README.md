# ringzer0team.com -- SysAdmin Linux -- Level 1

## 1. Challenge

> Find Trinity password 
> 
> User: morpheus  
> Password: VNZDDLq2x9qXCzVdABbR1HOtz

Please connect to via SSH:

```bash
$ ssh morpheus@challenges.ringzer0team.com -p 10089
```

## 2. Solution

You should search and read every file you can read. 

But don't look around manually, please use `grep`.

```bash
$ grep "trinity" -R /etc/ 2>/dev/null
```

Then you will see the flag:

```bash
morpheus@lxc-sysadmin:~$ grep "trinity" -R /etc/ 2>/dev/null
/etc/rc.local:/bin/sh /root/files/backup.sh -u trinity -p Flag-08grILsn3ekqhDK7cKBV6ka8B &
/etc/group:challenger:x:1000:morpheus,trinity,architect,oracle,neo,cypher
/etc/group:trinity:x:1002:neo
/etc/passwd:trinity:x:1001:1002::/home/trinity:/bin/bash
/etc/subgid:trinity:165536:65536
/etc/subuid:trinity:165536:65536
```
