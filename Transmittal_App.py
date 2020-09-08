from datetime import date
import os
import os.path
import platform
import csv
import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = tk.Tk()

class Application(tk.Frame):
    def __init__ (self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry('250x75')
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.submit = tk.Button(self)
        self.submit ["text"] = "Submit"
        self.submit ["command"] = self.onClick
        self.submit.grid(column=0,row=2)

        self.cancel = tk.Button(self)
        self.cancel ["text"] = "Cancel"
        self.cancel ["command"] = self.cancelApp
        self.cancel.grid(column=2, row=2)

        self.uL1 = tk.Label(self)
        self.uL1 ["text"] = "Path to documents"
        self.uL1.grid(column=0, row=1)
        self.userInput = tk.Entry(self) 
        self.userInput.grid(column=2,row=1)

    def get_Files(self):
        """User to copy and past in file path of documents being issued. The total number of documents in folder will be displayed."""
    #    path = input("Paste in path for outgoing folder: ")
        numTitleRev = os.listdir(self.userInput.get())
        print('\n' + "The total amount of documents in this folder is: %s\n" % len(numTitleRev))
        return numTitleRev 

    def process_files(self, filenames):
        """This process splits the list created from get_Files() into Number, Revision & Title. This is then created into a new list."""
        today = date.today()
        parsed = []
        for item in filenames:
            fileNum, fileRev, fileTitle = item.split(',',2)
            parsed.append([fileNum,fileRev,fileTitle, today])
        return parsed

    def write_output(self, parsed_data):
        """This new list is written to the CSV file."""   
        with open('output.csv', 'a') as writeCSV:
            writer = csv.writer(writeCSV)
            for row in parsed_data:
                writer.writerow(row)
        print("Writing complete")

    def cancelApp(self):
        cancelMsg = tk.messagebox.askquestion('Please choose an option','Are you sure you want to close application?')
        if cancelMsg == 'yes':
            self.master.destroy()
        else:
            tk.messagebox.showinfo('Return', 'You will be returned to the application.')

    def exitApp(self):
        exitMsg = tk.messagebox.askquestion('Please choose an option','Are you sure you want to close application?')
        if exitMsg == 'yes':
            tk.messagebox.showinfo('Return', 'You will be returned to the application.')
        else:
            self.master.destroy()
  
    def onClick(self):
        """When user clicks submit."""
        filenames = self.get_Files()
        converted = self.process_files(filenames)
        self.write_output(converted)
        self.exitApp()

def create_CSV():
    """Creates CSV file for saving outgoing file names."""
    csvExists = os.path.isfile('ENTER IN FILE PATH') 
    if csvExists:
        main()
    else:
        csvHeaders = ["Number", "Revision", "Title", "Date"]
        with open('output.csv', 'w+') as newCSV:
            filewriter = csv.writer(newCSV, delimiter=',',
                                    quotechar ='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(csvHeaders)

def os_Checker():
    """As the output.csv writes differently depending on OS (Windows or Linux) an OS checker has been included to keep trackof this."""
    platformVer = platform.system() + " " + platform.release()
    print("Your current operating system is: " + platformVer + '\n')

def main():
    """Calls tkinter gui. Sets master as root"""
    app = Application(master = root)
    app.mainloop()


if __name__=="__main__":
    create_CSV()
    os_Checker()
    main()

