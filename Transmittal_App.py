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
    path = input("Paste in path for outgoing folder: ")
    numTitleRev = os.listdir(path)
    print('\n' + "The total amount of documents in this folder is: %s\n" % len(numTitleRev))
    return numTitleRev

def process_files(filenames):
    parsed = []
    for item in filenames:
        fileNum, fileRev, fileTitle = item.split(',',2)
        parsed.append([fileNum,fileRev,fileTitle])
    return parsed

def write_output(parsed_data):
    with open('output.csv', 'a') as writeCSV:
        writer = csv.writer(writeCSV)
        for row in parsed_data:
            writer.writerow(row)
    print("Writing complete")

def main():
    filenames = getFiles()
    converted = process_files(filenames)
    write_output(converted)


if __name__=="__main__":
    osChecker()
    main()

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
