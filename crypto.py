import os
import re

from Crypto.Cipher import AES
from Crypto.Hash import SHA256


class Cipher:
    """
    Encryption and Decryption codes transform plaintext in some way that is
    dependent on a key, producing ciphertext.

    """

    def __init__(self, pw, iv):
        assert bool(re.match(r'[0-9]{16}$', iv)), "The initial vector must be 16 length."

        key = SHA256.new(pw.encode('utf-8')).digest()
        self.cfb = AES.new(key, AES.MODE_CFB, iv)

    def encryption(self, data):
        return self.cfb.encrypt(data)

    def decryption(self, data):
        return self.cfb.decrypt(data)
