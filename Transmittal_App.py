#from tkinter import *
#from tkinter import messagebox
import datetime
import os
import os.path
import platform
import csv


def create_CSV():
    
    """Creates CSV file for saving outgoing file names."""

    csvHeaders = ["Number", "Revision", "Title"]
    with open('output.csv', 'w+') as newCSV:
        filewriter = csv.writer(newCSV, delimiter=',',
                                quotechar ='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(csvHeaders)

def os_Checker():
    """As the output.csv writes differently depending on OS (Windows or Linux) an OS checker has been included to keep trackof this."""
    platformVer = platform.system() + " " + platform.release()
    print("Your current operating system is: " + platformVer + '\n')

def get_Files():
    """User to copy and past in file path of documents being issued. The total number of documents in folder will be displayed."""
    path = input("Paste in path for outgoing folder: ")
    numTitleRev = os.listdir(path)
    print('\n' + "The total amount of documents in this folder is: %s\n" % len(numTitleRev))
    return numTitleRev

def process_files(filenames):
    """This process splits the list created from get_Files() into Number, Revision & Title. This is then created into a new list."""
    parsed = []
    for item in filenames:
        fileNum, fileRev, fileTitle = item.split(',',2)
        parsed.append([fileNum,fileRev,fileTitle])
    return parsed

def write_output(parsed_data):
    """This new list is written to the CSV file."""
    with open('output.csv', 'a') as writeCSV:
        writer = csv.writer(writeCSV)
        for row in parsed_data:
            writer.writerow(row)
    print("Writing complete")

def main():
    """Where the magic happens."""
    filenames = get_Files()
    converted = process_files(filenames)
    write_output(converted)


if __name__=="__main__":
    print(get_Files.__doc__)
    os_Checker()
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
