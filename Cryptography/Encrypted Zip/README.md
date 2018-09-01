# Cryptography - Encrypted Zip

## 1. Challenge

Only a package with three files inside: `flag.zip`, `weird.zip` and `weird.txt`. 

Please goto [https://ringzer0team.com/challenges/29](https://ringzer0team.com/challenges/29) to download.

## 2. Solution

This is a standard __Zip Known Plaintext Attack__.

The tool I use is `pkcrack`. Please goto [https://www.unix-ag.uni-kl.de/~conrad/krypto/pkcrack.html](https://www.unix-ag.uni-kl.de/~conrad/krypto/pkcrack.html) to download.

Unpack the package and you will get the three files.

Please use __7z__ to zip `weird.txt` without password. Use other zip tools may make attack fail. I waste a lot of time here. :-(

Here is an example:

```bash
$ 7z a wweird_nopass.zip weird.txt
7-Zip [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
p7zip Version 9.20 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,1 CPU)
Scanning

Creating archive weird_nopass.zip

Compressing  weird.txt

Everything is Ok
```

Then use `pkcrack` to find key:

```bash
$ ./pkcrack -c "weird.txt" -p "weird.txt" -C ./weird.zip -P ./weird_nopass.zip -a
Files read. Starting stage 1 on Sat Sep  1 10:43:55 2018
Generating 1st generation of possible key2_96 values...done.
Found 4194304 possible key2-values.
Now we're trying to reduce these...
Done. Left with 109196 possible Values. bestOffset is 24.
Stage 1 completed. Starting stage 2 on Sat Sep  1 10:44:00 2018
Strange... had a false hit.
Strange... had a false hit.
Strange... had a false hit.
Strange... had a false hit.
Ta-daaaaa! key0=3330b3a9, key1=c403beea, key2=a0b3129d
Probabilistic test succeeded for 77 bytes.
```

Use `findkey` to recover user key:

```bash
$ ./findkey 3330b3a9 c403beea a0b3129d
Key: 74 65 73 74 74 65 73 74
Or as a string: 'testtest' (without the enclosing single quotes)
```

Now unzip `flag.zip` to get flag.
