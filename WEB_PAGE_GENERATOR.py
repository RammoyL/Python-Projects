

import tkinter as tk
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        #Sets title for the GUI window
        self.master.title("Web Page Generator")
        #Creates button to for default text
        self.btn = Button(self.master, text="Default HTML Page", width=20, height=2, command=self.defaultHTML)
        self.btn.grid(row=1, column=0, padx=(5,5) , pady=(5,5))
        #Creates button to for custom text
        self.custom_btn = Button(self.master, text="Submit Custom Text", width=20, height=2, command=self.customText)
        self.custom_btn.grid(row=1, column=1, padx=(5,5) , pady=(5,5))
        #Positions entry in GUI grid() to ensure they will line up
        self.custom = Entry(width=55)
        self.custom.grid(row=0, column=0, columnspan=2, padx=(5,5) , pady=(5,5))

        
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def customText(self):
        custom = self.custom.get()
        customFile = open("index.html", "w")
        customContent = "<html>\n<body>\n<h1>" + custom + "</h1>\n</body>\n</html>"
        customFile.write(customContent)
        customFile.close()
        webbrowser.open_new_tab("index.html")

    


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
