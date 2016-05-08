from Tkinter import *

def my_calc(create, side):
	storeIt = Frame( create, borderwidth = 4, bd = 4 , bg = "powder blue")
	storeIt.pack(side = side, expand = YES , fill = BOTH)
	return storeIt

def button(create, side, text , command = None):
    storeIt = Button(create, text = text, command = command)
    storeIt.pack(side = side, expand = YES , fill = BOTH)
    return storeIt

class Capp(Frame):
	def __init__(self):
		Frame.__init__(self)
		self.option_add('*Font', 'arial 16')
		self.pack(expand = YES, fill = BOTH)
		self.master.title('My Calculator')

		display = StringVar()
		Entry(self, relief = RIDGE, textvariable = display, justify = 'right', bd = 15, bg = "powder blue").pack(side = TOP, expand = YES, fill = BOTH)


		for Cbutton in ( ["C"]):
			remove =  my_calc(self, TOP)
			for my_char in Cbutton:
				button(remove, LEFT , my_char, lambda storeIt = display, q = my_char: storeIt.set(''))

		

		for Numbutton in ("789/", "456*", "123-", "0.+"):
			number =  my_calc(self, TOP)
			for char in Numbutton:
				button(number, LEFT , char, lambda storeIt = display, q = char: storeIt.set(storeIt.get() + q))


		EqButton = my_calc(self, TOP)
		for iEq in "=":
			if iEq == '=':
				btniEq = button(EqButton, LEFT, iEq)
				btniEq.bind('<ButtonRelease-1>', lambda e, s = self, storeIt = display: s.calc(storeIt), '+')

			else:
				btniEq = button(EqButton, LEFT, iEq, lambda storeIt = display, s=' %s '%iEq: storeIt.set(storeIt.get() + s))


	def calc(self, display):
		try:
			display.set(eval(display.get()))
		except:
			display.set("ERROR")
	
    	
if __name__ == '__main__':
	Capp() .mainloop()
