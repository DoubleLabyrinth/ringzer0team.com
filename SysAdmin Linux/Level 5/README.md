# ringzer0team.com -- SysAdmin Linux -- Level 5

## 1. Challenge

> Decrypt the oracle encrypted file   
>   
> User: oracle  

Please connect to via SSH:

```bash
$ ssh oracle@challenges.ringzer0team.com -p 10149
```

## 2. Solution

I just looked around the `~` folder and I see

```bash
oracle@lxc-sysadmin:~$ cat .bashrc
...
...
alias reveal="openssl enc -aes-256-cbc -a -d -in encflag.txt.enc -k 'lp6PWgOwDctq5Yx7ntTmBpOISc'"
...
...
```

So you should how to do. 

