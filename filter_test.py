# -*- coding: utf-8 -*- 

def is_palindrome(n):
	n_str = str(n)
	length = len(n_str)
	a = 0
	b = length-1
	while a<b:
		if n_str[a] != n_str[b]:
			return False
		a = a+1
		b = b-1
	return True

output = filter(is_palindrome,range(1,1000))
print(list(output))		