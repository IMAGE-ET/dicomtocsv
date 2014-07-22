from Tkinter import *
import tkFileDialog
from os import listdir
import dicom
import csv

class DicomToCSV:

    def __init__(self, parent):
    	self.parent = parent
    	
    	self.file_opt = options = {}
        options['filetypes'] = [('CSV Files', '.csv'), ('CSV File', '.csv')]
        options['initialfile'] = 'dicom.csv'
        options['parent'] = root
    	
    	self.initialize()

    def initialize(self):
    	self.frame = Frame(self.parent, padx=20, pady=20)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.parent.grid_rowconfigure(0, weight=1)
    	self.parent.grid_columnconfigure(0, weight=1)

        self.source_label = Label(self.frame, pady=10, text="Source folder  ")
        self.source_label.grid(sticky=E)

        self.source_entry = Entry(self.frame)
        self.source_entry.grid(row=0, column=1)

        self.source_browse = Button(self.frame, text="Browse", command=self.browseSourceFolder)
        self.source_browse.grid(row=0, column = 2)

        self.dest_label = Label(self.frame, text="Save to file  ")
        self.dest_label.grid(sticky=E)

        self.dest_entry = Entry(self.frame)
        self.dest_entry.grid(row=1, column=1)

        self.dest_browse = Button(self.frame, text="Browse", command=self.browseDestFolder)
        self.dest_browse.grid(row=1, column = 2)

        self.save_button = Button(self.frame, text="Save", command=self.saveCSV)
        self.save_button.grid(row=2,column=0, columnspan=2, sticky=E)

        self.cancel_button = Button(self.frame, text="Cancel", command=self.frame.quit)
        self.cancel_button.grid(row=2,column=2)

    def browseSourceFolder(self):
    	directory = tkFileDialog.askdirectory()
    	self.source_entry.delete(0, END)
    	self.source_entry.insert(0, directory)

    def browseDestFolder(self):
    	FILEOPTIONS = dict(defaultextension='.csv',filetypes=[('CSV file','*.csv')])
    	csv_file = tkFileDialog.asksaveasfilename(**self.file_opt)
    	self.dest_entry.insert(0, csv_file)

    def saveCSV(self):
    	files = listdir(self.source_entry.get())
    	csvfile = open(self.dest_entry.get(), 'a')
    	wr = csv.writer(csvfile, delimiter=',', quotechar='\'', quoting=csv.QUOTE_ALL)

    	for fil in files:
    		dicom_file = self.source_entry.get()+'/'+fil
    		plan = dicom.read_file(dicom_file)
    		print plan.PatientName
    		wr.writerow([plan.PatientID] + [plan.PatientName] +[plan.BodyPartExamined]+[plan.StationName])
    		
if __name__=="__main__":
	root = Tk()
	app = DicomToCSV(root)
	root.title('DICOM to CSV Converter')
	root.resizable(0,0)
	root.mainloop()
