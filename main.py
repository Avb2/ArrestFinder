import webbrowser
import requests
from src import myFunctions
from tkinter import *

# initialize tkinter root
root = Tk()

# Information input
fnameEntry = Entry()
fnameEntry.grid(row=0, column=1)
Label(text='First Name').grid(row=0, column=0)

lnameEntry = Entry()
lnameEntry.grid(row=1, column=1)
Label(text='Last Name').grid(row=1, column=0)

countyEntry = Entry()
countyEntry.grid(row=2, column=1)
Label(text='County').grid(row=2, column=0)

# Search Button
search = Button(text='Search', command=lambda: myFunctions.runSearch(countyEntry,fnameEntry,lnameEntry))
search.grid(row=4, column=0, columnspan=2)

# Run script
root.mainloop()
