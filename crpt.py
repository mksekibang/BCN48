#! /usr/bin/env python
# -*- coding: utf-8 -*-
# シリアルコード暗号化モジュール

# CryptoはPythonの標準モジュールじゃないので別途インストールが必要
# この辺からもってきてください（GAEでは使えるらしいです）
# http://www.voidspace.org.uk/python/modules.shtml#pycrypto
from Crypto.Cipher import CAST
import base64

# 暗号化用のキーを持つ変数（16バイトの倍数。たぶん）
CRYPTO_KEY = "16bytes  str1ngs"

# 暗号化
def CryptionMessage(message):
    """
        暗号化できる文字数は8の倍数です
    """
    crypto_object = CAST.new(CRYPTO_KEY)
    crypto_message = crypto_object.encrypt(message)
    en_cr_message = base64.b16encode(crypto_message)

    return en_cr_message

# 復号化
def DecryptionMessage(message):
    crypto_object = CAST.new(CRYPTO_KEY)
    de_message = base64.b16decode(message)
    decrypto_message = crypto_object.decrypt(de_message) 

    return decrypto_message


if __name__ == "__main__":
    a = CryptionMessage("00000003")
    print a
    print DecryptionMessage(a)
