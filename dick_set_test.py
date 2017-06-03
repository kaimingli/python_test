# -*- coding: utf-8 -*-

d = {
	'zhao':90,
	'qian':80,
	'sun':70,
	'li':60
}
print(d['zhao'])
print(d['qian'])
print(d['sun'])
print(d['li'])

s1 = set([1,2,3,3,4,4,5])
print(s1)
s2 = set([1,4,6,6,8,9])
print(s2)
print(s1&s2)
print(s1|s2)

#可以实现
d_test1 = {
	(1,2,3):'test1'
}
print(d_test1[(1,2,3)])

#list可变，不能作为hash索引
#d_test2 = {
#	(1,[2,3]):'test2'
#}
#print(d_test2[(1,[2,3])])