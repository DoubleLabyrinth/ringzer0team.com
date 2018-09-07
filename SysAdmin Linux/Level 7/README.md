# ringzer0team.com -- SysAdmin Linux -- Level 7

## 1. Challenge

> Neo is not alone!   
>   
> User: neo  
> Password: FLAG for the Level 2  

Please connect to via SSH:

```bash
$ ssh neo@challenges.ringzer0team.com -p 10091
```

## 2. Solution

I don't know how to solve this challenge at the beginning. I searched for other's write-ups and found a solution.

```bash
neo@lxc-sysadmin:~$ ps fl -u neo
F   UID   PID  PPID PRI  NI    VSZ   RSS WCHAN  STAT TTY        TIME COMMAND
4  1004 31916 31913  35  15   4216   612 hrtime SNs  ?          0:01 /bin/monitor
4  1004 31448 31446  35  15   4216   612 hrtime SNs  ?          0:06 /bin/monitor
4  1004 30748 30746  35  15   4216   612 hrtime SNs  ?          0:06 /bin/monitor
4  1004 30120 30117  35  15   4216   612 hrtime SNs  ?          0:06 /bin/monitor
4  1004 29225 29222  35  15   4216   612 hrtime SNs  ?          0:06 /bin/monitor
4  1004 28630 28627  35  15   4216   612 hrtime SNs  ?          0:06 /bin/monitor
4  1004 27890 27886  35  15   4216   612 hrtime SNs  ?          0:05 /bin/monitor
4  1004 27531 27528  35  15   4216   612 hrtime SNs  ?          0:04 /bin/monitor
4  1004 27273 27271  35  15   4216   612 hrtime SNs  ?          0:05 /bin/monitor
4  1004 27239 27236  35  15   4216   612 hrtime SNs  ?          0:04 /bin/monitor
4  1004 27133 27130  35  15   4216   612 hrtime SNs  ?          0:02 /bin/monitor
4  1004 26646 26643  35  15   4216   612 hrtime SNs  ?          0:01 /bin/monitor
4  1004 26549 26544  35  15   4216   612 hrtime SNs  ?          0:05 /bin/monitor
4  1004 26241 26237  35  15   4216   612 hrtime SNs  ?          0:00 /bin/monitor
4  1004 26131 26128  35  15   4216   612 hrtime SNs  ?          0:03 /bin/monitor
4  1004 26056 26054  35  15   4216   612 hrtime SNs  ?          0:00 /bin/monitor
4  1004 25948 25945  35  15   4216   612 hrtime SNs  ?          0:04 /bin/monitor
4  1004 25798 25792  35  15   4216   612 hrtime SNs  ?          0:00 /bin/monitor
4  1004 25474 25471  35  15   4216   612 hrtime SNs  ?          0:04 /bin/monitor
4  1004 25189 25186  35  15   4216   612 hrtime SNs  ?          0:03 /bin/monitor
4  1004 24796 24793  35  15   4216   612 hrtime SNs  ?          0:02 /bin/monitor
4  1004 24788 24785  35  15   4216   612 hrtime SNs  ?          0:02 /bin/monitor
4  1004 23517 23514  35  15   4216   612 hrtime SNs  ?          0:01 /bin/monitor
4  1004 21686 21683  35  15   4216   612 hrtime SNs  ?          0:03 /bin/monitor
4  1004 21281 21278  35  15   4216   612 hrtime SNs  ?          0:02 /bin/monitor
4  1004 18489 18486  35  15   4216   612 hrtime SNs  ?          0:01 /bin/monitor
4  1004 16210 16207  35  15   4216   612 hrtime SNs  ?          0:01 /bin/monitor
4  1004 15659 15656  35  15   4216   612 hrtime SNs  ?          0:07 /bin/monitor
4  1004 15057 15054  35  15   4216   612 hrtime SNs  ?          0:00 /bin/monitor
4  1004 14943 14940  35  15   4216   612 hrtime SNs  ?          0:06 /bin/monitor
4  1004 14163 14160  35  15   4216   612 hrtime SNs  ?          0:06 /bin/monitor
4  1004 13857 13854  35  15   4216   612 hrtime SNs  ?          0:00 /bin/monitor
5  1004 13850 13843  35  15  90488  3380 -      SN   ?          0:00 sshd: neo@pts/5
0  1004 13851 13850  35  15  21176  3732 wait   SNs  pts/5      0:00  \_ -bash
0  1004 13867 13851  35  15  37512  3192 -      RN+  pts/5      0:00      \_ ps fl -u neo
4  1004 13458 13455  35  15   4216   612 hrtime SNs  ?          0:06 /bin/monitor
4  1004 12717 12714  35  15   4216   612 hrtime SNs  ?          0:03 /bin/monitor
4  1004 12589 12586  35  15   4216   612 hrtime SNs  ?          0:06 /bin/monitor
4  1004 12063 12060  35  15   4216   612 hrtime SNs  ?          0:05 /bin/monitor
4  1004 11971 11968  35  15   4216   612 hrtime SNs  ?          0:01 /bin/monitor
4  1004 11325 11321  35  15   4216   612 hrtime SNs  ?          0:05 /bin/monitor
4  1004 11256 11253  35  15   4216   612 hrtime SNs  ?          0:02 /bin/monitor
4  1004 10781 10778  35  15   4216   612 hrtime SNs  ?          0:02 /bin/monitor
4  1004 10771 10767  35  15   4216   612 hrtime SNs  ?          0:01 /bin/monitor
4  1004 10754 10752  35  15   4216   612 hrtime SNs  ?          0:05 /bin/monitor
4  1004 10371 10369  35  15   4216   612 hrtime SNs  ?          0:00 /bin/monitor
4  1004  9983  9980  35  15   4216   612 hrtime SNs  ?          0:05 /bin/monitor
4  1004  9697  9694  35  15   4216   612 hrtime SNs  ?          0:03 /bin/monitor
4  1004  9688  9684  35  15   4216   612 hrtime SNs  ?          0:00 /bin/monitor
4  1004  9587  9584  35  15   4216   612 hrtime SNs  ?          0:04 /bin/monitor
4  1004  9509  9503  35  15   4216   612 hrtime SNs  ?          0:00 /bin/monitor
4  1004  9455  9452  35  15   4216   612 hrtime SNs  ?          0:04 /bin/monitor
4  1004  8860  8857  35  15   4216   612 hrtime SNs  ?          0:02 /bin/monitor
4  1004  8514  8511  35  15   4216   612 hrtime SNs  ?          0:02 /bin/monitor
4  1004  6092  6089  35  15   4216   612 hrtime SNs  ?          0:00 /bin/monitor
4  1004  5830  5827  35  15   4216   612 hrtime SNs  ?          0:03 /bin/monitor
4  1004  5256  5253  35  15   4216   612 hrtime SNs  ?          0:03 /bin/monitor
4  1004  2735  2732  35  15   4216   612 hrtime SNs  ?          0:03 /bin/monitor
4  1004  2602  2599  35  15   4216   612 hrtime SNs  ?          0:01 /bin/monitor
4  1004  2099  2096  35  15   4216   612 hrtime SNs  ?          0:04 /bin/monitor
4  1004   247   244  35  15   4216   612 hrtime SNs  ?          0:07 /bin/monitor
4  1004   185   179  35  15   4216   612 hrtime SNs  ?          0:07 /bin/monitor
```

You can see there a lot of processes which are run as neo.

So we can get all of syscalls generated by those processes.

```bash
neo@lxc-sysadmin:~$ strace -p 185
strace: Process 185 attached
restart_syscall(<... resuming interrupted nanosleep ...>) = 0
write(-1, "telnet 127.0.0.1 23\n", 20)  = -1 EBADF (Bad file descriptor)
write(-1, "user\n", 5)                  = -1 EBADF (Bad file descriptor)
write(-1, "FLAG-a4UVY5HJQO5ddLc5wtBps48A3\n", 31) = -1 EBADF (Bad file descriptor)
write(-1, "get-cpuinfo\n", 12)          = -1 EBADF (Bad file descriptor)
nanosleep({10, 0}, 0x7fffffffec10)      = 0
write(-1, "telnet 127.0.0.1 23\n", 20)  = -1 EBADF (Bad file descriptor)
write(-1, "user\n", 5)                  = -1 EBADF (Bad file descriptor)
write(-1, "FLAG-a4UVY5HJQO5ddLc5wtBps48A3\n", 31) = -1 EBADF (Bad file descriptor)
write(-1, "get-cpuinfo\n", 12)          = -1 EBADF (Bad file descriptor)
nanosleep({10, 0}, 0x7fffffffec10)      = 0
write(-1, "telnet 127.0.0.1 23\n", 20)  = -1 EBADF (Bad file descriptor)
write(-1, "user\n", 5)                  = -1 EBADF (Bad file descriptor)
write(-1, "FLAG-a4UVY5HJQO5ddLc5wtBps48A3\n", 31) = -1 EBADF (Bad file descriptor)
write(-1, "get-cpuinfo\n", 12)          = -1 EBADF (Bad file descriptor)
nanosleep({10, 0}, 0x7fffffffec10)      = 0
write(-1, "telnet 127.0.0.1 23\n", 20)  = -1 EBADF (Bad file descriptor)
write(-1, "user\n", 5)                  = -1 EBADF (Bad file descriptor)
write(-1, "FLAG-a4UVY5HJQO5ddLc5wtBps48A3\n", 31) = -1 EBADF (Bad file descriptor)
write(-1, "get-cpuinfo\n", 12)          = -1 EBADF (Bad file descriptor)
nanosleep({10, 0}, ^Cstrace: Process 185 detached
 <detached ...>
```

Here's the flag.

