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

#Frames
left_frame=Frame(window,bg="#086387",relief=RIDGE,bd=10)
left_frame.place(x=10,y=50,width=345,height=250)
right_frame=Frame(window,bg="#086387",relief=RIDGE,bd=10)
right_frame.place(x=365,y=50,width=345,height=250)

#Labels
name = Label(left_frame,text="Your Pet's Name",font=('kacstdigital',15,'bold'), fg='#FCB912',bg="#086387")
name.grid(row=5,column=0,padx=10,pady=20)

animal_type = Label(left_frame,text='Animal Type',font=('kacstdigital',15,'bold'),fg ='#FCB912',bg="#086387")
animal_type.grid(row=6,column=0,padx=10,pady=20)

pet_age = Label(left_frame,text="Your Pet's Age",font=('kacstdigital',15,'bold'),fg ='#FCB912',bg="#086387")
pet_age.grid(row=7,column=0,padx=10,pady=20)


#create the buttons
#create the necessary functions of the buttons

window.mainloop()