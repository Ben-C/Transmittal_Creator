#from tkinter import *
#from tkinter import messagebox
import datetime
import os
import os.path



def getFiles():
   path = input("Paste in path for outgoing foler: ")
   numTitleRev = os.listdir(path)
   fileData = []
   for item in numTitleRev:
        fileSplit = item.split(',', 2)
        fileData.append(fileSplit)
   print(fileData)

  
    #fileTitle = fileSplit.pop()
    #fileRev = fileSplit.pop()
    #fileNum = fileSplit.pop()
    #issueRec.append(fileNum)
    #issueRec.append(fileRev)
    #issueRec.append(fileTitle)

   

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
