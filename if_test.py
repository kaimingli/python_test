# -*- coding: utf-8 -*-

print('1')
s1 = input()
weight = int(s1)
print('2')
s2 = input()
height = int(s2)

bim = weight/(height**2)
if bim<18.5:
	print('3')
else:
	if bim<25:
		print('4')
	else:
		if bim<28:
			print('5')
		else:
			if bim<32:
				print('6')
			else:
				print('7')

input()