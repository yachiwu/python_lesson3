# 平方計算器label
import tkinter as tk
import tkinter.font as tkFont
import math
from PIL import ImageTk
class Calculator(tk.Frame):
	shouldReset = True
	def __init__(self):
		tk.Frame.__init__(self)
		self.grid()
		self.createWidgets()
	def createWidgets(self):
		f1 = tkFont.Font(size = 48,family = 'Courier New')
		f2 = tkFont.Font(size = 32,family = 'Courier New')
		self.imageSqrt = ImageTk.PhotoImage(file="square-02.png")
		self.lb1Num = tk.Label(self,text="0",height = 1,width = 7,font = f1)
		self.btnNum0 = tk.Button(self,text="0",command = self.clickBtnNum0,height = 1,width = 2,font = f2)
		self.btnSqrt = tk.Button(self,image = self.imageSqrt,command = self.clickBtnSqrt,height = 1,width = 2,font = f2)
		self.btnNum1 = tk.Button(self,text="1",command = self.clickBtnNum1,height = 1,width = 2,font = f2)
		self.btnNum2 = tk.Button(self,text="2",command = self.clickBtnNum2,height = 1,width = 2,font = f2)
		self.btnNum3 = tk.Button(self,text="3",command = self.clickBtnNum3,height = 1,width = 2,font = f2)
		self.btnNum4 = tk.Button(self,text="4",command = self.clickBtnNum4,height = 1,width = 2,font = f2) 
		self.btnNum5 = tk.Button(self,text="5",command = self.clickBtnNum5,height = 1,width = 2,font = f2)
		self.btnNum6 = tk.Button(self,text="6",command = self.clickBtnNum6,height = 1,width = 2,font = f2)
		self.btnNum7 = tk.Button(self,text="7",command = self.clickBtnNum7,height = 1,width = 2,font = f2)
		self.btnNum8 = tk.Button(self,text="8",command = self.clickBtnNum8,height = 1,width = 2,font = f2)
		self.btnNum9 = tk.Button(self,text="9",command = self.clickBtnNum9,height = 1,width = 2,font = f2)	
		self.lb1Num.grid(row = 0,column = 0,columnspan = 3,sticky = tk.NE+tk.SW)
		self.btnNum1.grid(row = 1,column = 0,sticky = tk.NE+tk.SW)
		self.btnNum2.grid(row = 1,column = 1,sticky = tk.NE+tk.SW)
		self.btnNum3.grid(row = 1,column = 2,sticky = tk.NE+tk.SW)
		self.btnNum4.grid(row = 2,column = 0,sticky = tk.NE+tk.SW)
		self.btnNum5.grid(row = 2,column = 1,sticky = tk.NE+tk.SW)
		self.btnNum6.grid(row = 2,column = 2,sticky = tk.NE+tk.SW)
		self.btnNum7.grid(row = 3,column = 0,sticky = tk.NE+tk.SW)
		self.btnNum8.grid(row = 3,column = 1,sticky = tk.NE+tk.SW)
		self.btnNum9.grid(row = 3,column = 2,sticky = tk.NE+tk.SW)
		self.btnNum0.grid(row = 4,column = 0,columnspan =2,sticky = tk.NE+tk.SW)
		self.btnSqrt.grid(row = 4,column = 2,sticky = tk.NE+tk.SW)
	def setNumStr(self,content):	
		if self.shouldReset == True:
			self.lb1Num.configure(text = content)
			self.shouldReset = False
		else :
			self.lb1Num.configure(text = self.lb1Num.cget('text')+content)	
	def clickBtnNum1(self):
		self.setNumStr("1")
	def clickBtnNum2(self):
		self.setNumStr("2")
	def clickBtnNum3(self):
		self.setNumStr("3")
	def clickBtnNum4(self):
		self.setNumStr("4")
	def clickBtnNum5(self):
		self.setNumStr("5")
	def clickBtnNum6(self):
		self.setNumStr("6")	
	def clickBtnNum7(self):
		self.setNumStr("7")
	def clickBtnNum8(self):
		self.setNumStr("8")
	def clickBtnNum9(self):
		self.setNumStr("9")
	def clickBtnNum0(self):
		self.setNumStr("0")							
	def clickBtnSqrt(self):
		curNum = float(self.lb1Num.cget('text'))	
		self.lb1Num.configure(text = str(pow(curNum, 2)))	
		self.shouldReset = True
cal = Calculator()
cal.master.title("My Calculator")
cal.mainloop()
