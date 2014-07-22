import Tkinter
import tkFileDialog

class CSVGenerator(Tkinter.Tk):
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()

	def initialize(self):
		self.grid()
		var = StringVar()
		self.label = Tkinter.Label(self, anchor="w", textvariable=var)
		self.label.grid(column=0, row=0, stick='EW')
		var.set("Source folder: ")

		self.entry = Tkinter.Entry(self)
		self.entry.grid(column = 1, row=0, sticky='EW')

		button = Tkinter.Button(self, text=u"Browse", command=self.browseFolder)
		button.grid(column=2, row=0)

		self.grid_columnconfigure(0, weight = 1)

	def browseFolder(self):
		directory = tkFileDialog.askdirectory()
		self.entry.insert(0, directory) 

if __name__=="__main__":
	app = CSVGenerator(None)
	app.title('DICOM to CSV Convertor')
	app.mainloop()
