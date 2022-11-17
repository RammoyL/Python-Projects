

import datetime as dt
from datetime import timedelta
import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #Sets title for the GUI window
        self.master.title("File Transfer")
        #Creates button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=15, command=self.sourceDir)
        #Positions source buttton in GUI using grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(15, 10), pady=(20, 0))
        #Creates entry for source directory selection
        self.source_dir = Entry(width=30)
        #Positions entry in GUI grid() to ensure they will line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        #Creates button to select destination of files from the destination directory
        self.destDir_btn = Button(text="Select Destination", width=15, command=self.destDir)
        #Positions destination button in GUI on the next row under the source button
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))
        #Creates entry for destination directory selection
        self.destination_dir = Entry(width=30)
        #Positions entry in GUI to line up with select soruce button
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))
        #Creates button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=12, command=self.transferFiles)
        #Positions transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))
        #Creates an Exit button
        self.exit_btn = Button(text="Exit", width=12, command=self.exit_program)
        #Positions exit button
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))
        
        
    #Creates function to select source directory.
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #The .delete(0, END) will clear the content that is inserted in the Entry widget
        #now allows the path to be inserted into the widget properly.
        self.source_dir.delete(0, END)
        #The .insert method will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)
        
    #Creates function to select destination directory.
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        #The .delete(0, END) will clear content that is inserted in the Entry widget,
        #this allows the path to be inserted into the Entry widget properly.
        self.destination_dir.delete(0, END)
        #The .insert method will insert the user selection to th destination_dir Entry
        self.destination_dir.insert(0, selectDestDir)
        
    #Creates function to transfer files from one directory to another.
    def transferFiles(self):
        #Gets source directory
        source = self.source_dir.get()
        #Gets destination directory
        destination = self.destination_dir.get()
        #Gets list of files in source directory
        source_files = os.listdir(source)
        #Gets file times within 24hrs
        Yesterday = dt.datetime.now() + timedelta(days=-1)
        print(Yesterday)
        #Runs through each file in the source directory
        for i in source_files:
            path = source + '/' + i
            #get mod times for files
            modTime_epoch = os.path.getmtime(path)
            #changes epoch time to readable format
            mod_time = dt.datetime.fromtimestamp(modTime_epoch)
            #if mod time is greater than Yesterday then move the file
            if mod_time > Yesterday:
                shutil.move(source + '/' + i, destination)
            print(path)
            print(mod_time)
            

    #Creates function to exit program
    def exit_program(self):
        #root is the main GUI window, the Tkinter destroy method tells python to terminate root.mainloop
        #and all widgets inside the GUI window
        root.destroy()
       
##date_time = dt.timedelta(hours, minutes, seconds)
##path = source + '/' + i
##modification_time = os.path.getmtime(path)
##print("Last mod time:", )

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
