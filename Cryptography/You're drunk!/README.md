# Cryptography - You're drunk!

## 1. Challenge

```
Ayowe awxewr nwaalfw die tiy rgw fklf ua xgixiklrw! Tiy lew qwkxinw.
```

## 2. Solution

Well, this challenge really gets me stuck for a long time. 

I searched for somebody's write-up and here's the solution.

I'd like call this keyboard-shifting cipher, which means there is a mapping like the following

```
A --> L
B --> V
C --> X
...
...
Z --> M
```

in encryption. You can get `"L"` by shifting one key left from `"A"` key, of course, rotating. And so do `"B"`, `"C"`...

So the plaintext shoud be:

```
Ayowe awxewr nwaalfw die tiy rgw fklf ua xgixiklrw! Tiy lew qwkxinw.
Super secret message for you the glag is chocolate! You are welcome.
```

Of course, `"glag"` should be `"flag"`. It's just an exception.

