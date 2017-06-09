# -*- coding: utf-8 -*- 
import os

print(os.path.split(os.path.abspath('.'))[0])

#打印出path以及子目录中包含keyword的文件
def searchdir(path,keyword):
	if os.path.isfile(path):
		if keyword in path:
			print(os.path.split(path)[1],os.path.split(path)[0])
			pass
	else:
		for x in os.listdir(path):
			if os.path.isfile(x):
				if keyword in x:
					print(x,path)
			else:
				searchdir(os.path.join(path,x),keyword)
searchdir('.','py')