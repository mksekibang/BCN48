#! /usr/bin/env python
# -*- coding: utf-8 -*-

import Crypto.Cipher.AES as AES
#import Crypto.Hash.Hmac as Hmac
import datetime,time

#16,24,32byteの文字列が暗号化KEY
CRYPTO_KEY = "16bytes  str1ngs"
crypto_object = AES.new( CRYPTO_KEY, AES.MODE_ECB )

#unixtimeの取得
d = datetime.datetime.today()
utime = int( time.mktime( d.timetuple() ) )

#暗号化できる文字列は16byteの倍数
message = "0000000000000001"
crypto_message = crypto_object.encrypt( message ) 
decrypto_message = crypto_object.decrypt( crypto_message ) 

crypto_message

html  = '''Content-Type: text/html; charset=UTF-8
<html>
<head>
<title>web-pro.appspot.com</title>
</head>
<body>
<table>
<tr><th>message     </th><td>%s </td></tr>
<tr><th>encrypto      </th><td>%s </td></tr>
<tr><th>decrypto  </th><td>%s </td></tr>
</table>
</body>
<html>
'''
#print html % ( message, crypto_message, decrypto_message )
filename = "D:\Data\\beacon\\BCN48\\test.html"
w = open(filename, "w")
w.write(html % ( message, crypto_message, decrypto_message ))
w.flush()
w.close
