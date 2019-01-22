# Cipher
Encryption and Decryption codes transform plaintext in some way that is dependent on a key, producing ciphertext using by Python3.

## Requirements
```
PyCrypto
```

## How to use
Before you encryption or decrytion something, must know two important values.
1. __Key__: _String_, continous string values like password that will be converted by `UTF-8`
2. __Initial Vector__: _String_, 16 numbers `[0-9]{16}$` and wrap it with type of string

```python
(example)
key = 'password1234~!@#$something'
iv = '1234567890123456'
```

### Encryption
```python
from cipher.crypto import Cipher

data = 'Something you want to encrypt'
enc = Cipher(key, iv)
result = enc.encryption(data)
```

### Decryption
```python
from cipher.crypto import Cipher

data = 'Something you want to decrypt'
dec = Cipher(key, iv)
result = dec.decryption(data)
```
