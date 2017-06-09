# -*- coding: utf-8 -*- 

import hashlib

db = {}
def register(username,password):
	db[username] = get_md5(password+username+'the-Salt')
	
def get_md5(s):
	md5 = hashlib.md5()
	md5.update(s.encode('utf-8'))
	return md5.hexdigest()
	
def login(username,password):
	if username in db:
		if db[username] == get_md5(password+username+'the-Salt'):
			return True
	return False

register('likaiming','123455')
print(login('likaiming','123455'))