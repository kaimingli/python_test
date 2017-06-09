# -*- coding: utf-8 -*- 

from tkinter import *

class Application(Frame):
	def _init_(self,master=None):
		Frame._init_(self,master)
		self.pack()
		self.createWidgets()
	def createWidgets(self):
		self.helloLable = Lable(self,text='Hello,world!')
		self.helloLable.pack()
		self.quitButton = Button(self,text='Quit',command=self.quit)
		self.quitButton.pack()
		
app = Application()
app.master.title('Hello World')
app.mainloop()