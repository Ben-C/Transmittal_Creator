#from tkinter import *
#from tkinter import messagebox
import datetime
import os
import os.path
import csv



def getFiles():
    path = input("Paste in path for outgoing foler: ")
    numTitleRev = os.listdir(path)
    issueRec = []
    fileData = []
    for item in numTitleRev:
        fileSplit = item.split(',', 2)
        fileTitle = fileSplit.pop(2)
        fileRev = fileSplit.pop(1)
        fileNum = fileSplit.pop(0)
              
    
    print(fileTitle)
    print(fileRev)
    print(fileNum)
    
    csvHeaders = [["Number", "Revision", "Title"]]
    csvOutput  = [[fileNum,fileRev,fileTitle]]

    with open('output.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        lines = list(reader)
    
    with open('output.csv', 'w') as csvHeader:
        writer = csv.writer(csvHeader)
        writer.writerows(csvHeaders)

    with open('output.csv', 'a') as writeCSV:
        writer = csv.writer(writeCSV)
        writer.writerows(csvOutput)
             
    writeCSV.close()
    csvFile.close()
   
    print("Writing complete")



  
    

   

if __name__=="__main__":
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
