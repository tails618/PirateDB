from tkinter import *
import firebasemanager

window1=Tk()

#Make the stuff
frame1=Frame(window1)
frame2=Frame(window1)
frame3=Frame(window1)
frame4=Frame(window1)

label1=Label(frame1,text="Pirate Database",font=("Comic Sans MS", 12))
label1.pack()

label2=Label(frame2,text="Search",font=("Comic Sans MS", 12))
label2.grid(row=0,column=0)

def searchUpdate(e):
    doFilter()

entry=Entry(frame2)
entry.bind("<KeyRelease>",searchUpdate)
entry.grid(row=0,column=1)

'''searchButton=Button(frame2,text="Go",font=("Comic Sans MS", 12))
searchButton.grid(row=0,column=2)'''

def doFilter():
    filt=entry.get()
    listbox.delete(0,"end")
    for pirate in d:
        if (filt.lower() in d[pirate]["name"].lower() or filt.lower() in d[pirate]["ship"].lower()):
            listbox.insert(END,d[pirate]["name"])


label3=Label(frame3,text="Frame 3",font=("Comic Sans MS", 12))
label3.grid(row=0,column=0)
leftImg=PhotoImage(file="arrow_left.gif")
rightImg=PhotoImage(file="arrow_right.gif")
leftButton=Button(frame3,image=leftImg)
rightButton=Button(frame3,image=rightImg)
leftButton.grid(row=1,column=0)
rightButton.grid(row=1,column=2)
placeholder=PhotoImage(file="me.gif")
piratePic=Label(frame3,image=placeholder,text="ARRRRRR #teampixel")
piratePic.grid(row=1,column=1)
shipLabel=Label(frame3,text="Ship Name",font=("Comic Sans MS",12))
shipLabel.grid(row=2,column=1)
ficLabel=Label(frame3,text="Fictional?",font=("Comic Sans MS",12))
ficLabel.grid(row=3,column=1)

listbox=Listbox(frame4,font=("Comic Sans MS",12))
listbox.pack()
fm=firebasemanager.FirebaseManager()
d=fm.getAllPirates()
for item in d:
    pirate=d[item]
    listbox.insert(END,pirate["name"])

def listDelete():
    listbox.delete(ANCHOR)
deleteButton=Button(frame4,text="Delete",font=("Comic Sans MS", 12),command=listDelete)
deleteButton.pack()
def quitWindow():
    window1.destroy()
exitButton=Button(frame4,text="Exit",font=("Comic Sans MS",12),command=quitWindow)
exitButton.pack()

#Grid the stuff
frame1.grid(row=0,column=0)
frame2.grid(row=0,column=1)
frame3.grid(row=1,column=0)
frame4.grid(row=1,column=1)

window1.mainloop()
