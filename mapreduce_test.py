# -*- coding: utf-8 -*- 
from functools import reduce

def normalize(name):
	return name[0].upper()+name[1:].lower()
	
L1 = ['adam','LISA','barT']
L2 = list(map(normalize,L1))
print(L2)

L3 = [3,5,7,9]
def prod(L):
	def multi(x,y):
		return x*y
	return reduce(multi,L)
print(prod(L3))

def str2float(s):
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9 }[s]
	point_pos = s.find('.')
	power = len(s)-point_pos-1
	map_result = map(char2num,s[:point_pos]+s[point_pos+1:])
	return reduce(lambda x,y:x*10+y,map_result)/(10**power)
print(str2float('123.456'))