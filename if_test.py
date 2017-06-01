# -*- coding: utf-8 -*-

print('输入体重')
s1 = input()
weight = int(s1)
print('输入身高')
s2 = input()
height = int(s2)

bim = weight/(height**2)
if bim<18.5:
	print('过轻')
else:
	if bim<25:
		print('正常')
	else:
		if bim<28:
			print('过重')
		else:
			if bim<32:
				print('肥胖')
			else:
				print('严重肥胖')

input()