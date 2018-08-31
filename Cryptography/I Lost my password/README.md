# Cryptography - I Lost my password

## 1. Challenge

Just a package. Please goto [https://ringzer0team.com/challenges/51](https://ringzer0team.com/challenges/51) to download.

## 2. Solution

This package seems to be an export of Windows Policy. 

Explore these files and you will see an interesting file: `Policies\{75DE8F0A-DEC0-441F-AE29-90DFAFCF632B}\User\Preferences\Groups\Groups.xml`

The content of this file is:

```xml
<?xml version="1.0" encoding="utf-8"?>
<Groups clsid="{3125E937-EB16-4b4c-9934-544FC6D24D26}">
  <User clsid="{DF5F1855-51E5-4d24-8B1A-D9BDE98BA1D1}" 
        name="Administrator (built-in)" 
        image="1" 
        changed="2014-02-06 19:33:28" 
        uid="{C73C0939-38FB-4287-AC48-478F614F5EF7}" 
        userContext="0" 
        removePolicy="0">
   
    <Properties action="R" 
                fullName="Administrator" 
                description="Administrator" 
                cpassword="PCXrmCkYWyRRx3bf+zqEydW9/trbFToMDx6fAvmeCDw" 
                changeLogon="0" 
                noChange="0" 
                neverExpires="1" 
                acctDisabled="0" 
                subAuthority="" 
                userName="Administrator (built-in)"/>
  </User>
</Groups>
```

where `cpassword` leaks Administrator's password.

`cpassword` is Base64 encoded while `"="` padding is removed. You should filling it with `"="` until the length is a multiple of 4. 

After decode, `cpassword` is the ciphertext of Administrator's password. The encryption algorithm is `AES-256/CBC/PKCS5Padding` where the key is documented in [MSDN](https://msdn.microsoft.com/en-us/library/2c15cbf0-f086-4c74-8b70-1f2fa45dd4be.aspx#endNote2).

I've written a python script to decrypt it. Just run it to get password. 
