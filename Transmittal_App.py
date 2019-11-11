#from tkinter import *
#from tkinter import messagebox
import datetime
import os
import os.path
import platform
import csv


def createCSV():
    csvHeaders = ["Number", "Revision", "Title"]
    with open('output.csv', 'w+') as newCSV:
        filewriter = csv.writer(newCSV, delimiter=',',
                                quotechar ='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(csvHeaders)
def osChecker():
    platformVer = platform.system() + " " + platform.release()
    print("Your current operating system is: " + platformVer + '\n')

def getFiles():
    
    i = 0
    path = input("Paste in path for outgoing folder: ")
    numTitleRev = os.listdir(path)
    issueRec = []
    fileData = []
    totalList = len(numTitleRev)
    listNumber = str(totalList)
    print('\n' + "The total amount of documents in this folder is: " + listNumber + '\n')

    while i < totalList:
        for item in numTitleRev:
            fileSplit = item.split(',', 2)
            fileTitle = fileSplit.pop(2)
            fileRev = fileSplit.pop(1)
            fileNum = fileSplit.pop(0)

        csvOutput  = [[fileNum,fileRev,fileTitle]]


        with open('output.csv', 'a') as writeCSV:
            writer = csv.writer(writeCSV)
            for row in csvOutput:
                writer.writerow(row)
        
            i += 1
       
    writeCSV.close()
       
    print("Writing complete")


if __name__=="__main__":
    osChecker()
    createCSV()
    getFiles()


  
#def gui
#win = Tk()
#def example():
#    x = 0
#    while x < 1000:
#        x = x+1
#        print (x)
#    messagebox.showinfo("Clicking","Thanks for clicking, good bye")
#    win.destroy()
#    
#    
#button = Button(win, text="Click here", command = example)
#button.pack()
#win.geometry('350x200')
#win.mainloop()
