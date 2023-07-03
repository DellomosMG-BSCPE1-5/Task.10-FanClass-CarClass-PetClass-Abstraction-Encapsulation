#import necessary modules
from tkinter import *
from tkinter import ttk,messagebox
import os

#create the window
window=Tk()
window.title('Your Pet')
window.geometry('720x360')
window.configure(bg="#0F1524")

#design/create the frames
#headers
heading = Label(text="Your Pet", fg="#8FBB3F", bg="#0F1524", width="450",height="1", font=("Helvetica", 20, "bold"))
heading.pack(fill=X)
#create the buttons
#create the necessary functions of the buttons

window.mainloop()