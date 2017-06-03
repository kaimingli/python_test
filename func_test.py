# -*- coding: utf-8 -*-

import math

n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))

def quadratic(a,b,c):
	temp = math.sqrt(b**2-4*a*c)
	return (-b+temp)/(2*a),(-b-temp)/(2*a)

print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))


def move(n,a,b,c):
	if n==1:
		print('move',a,'-->',c)
	else:
		move(n-1,a,c,b)
		move(1,a,b,c)
		move(n-1,b,a,c)
	
move(3,'A','B','C')