# -*- coding: utf-8 -*- 

import base64

def safe_base64_decode(s):
	equalnum =4 - len(s)%4
	s = s + b'='*equalnum
	return base64.b64decode(s)
	
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')