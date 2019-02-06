from tkinter import *
import firebasemanager
import Pirate
import imageManager

window1=Tk()

frame1=Frame(window1)
frame2=Frame(window1)
frame3=Frame(window1)
frame4=Frame(window1)

def doFilter():
    filt=entry.get()
    listbox.delete(0,"end")
    for pirate in d:
        if (filt.lower() in d[pirate]["name"].lower() or filt.lower() in d[pirate]["ship"].lower()):
            listbox.insert(END,d[pirate]["name"])

def display(pirateId):
    label3.config(text=d[pirateId]["name"])
    shipLabel.config(text=d[pirateId]["ship"])
    if d[pirateId]["fictional"]=="True":
        ficLabel.config(text="Fictional")
    else:
        ficLabel.config(text="Real")
    #show the image
    im=imageManager.ImageManager()
    #handle pirates with no images
    try:
        im.url=d[pirateId]["image"]
    except:
        pass
    if im.url !="":
        img=im.downloadUrl()
        piratePic.config(image=img)
        piratePic.image=img #TKinterJustNeedsThis #LOL
    else:
        piratePic.config(image=placeholder)
def scrollRight():
    index=int(listbox.curselection()[0])
    listbox.selection_clear(index)
    if index==len(d)-1:
        index=0
    else:
        index+=1

    updateListbox(index)
def scrollLeft():
    index=int(listbox.curselection()[0])
    listbox.selection_clear(index)
    if index==0:
        index=len(d)-1
    else:
        index-=1
    updateListbox(index)
def updateListbox(index):
    listbox.selection_set(index)
    piratename=listbox.get(index)
    for pirate in d:
        if piratename.lower()==d[pirate]["name"].lower():
            display(pirate)
def searchUpdate(e):
    doFilter()
def listDelete():
    #deletekey=""
    index=int(listbox.curselection()[0])
    listbox.selection_set(index)
    piratename=listbox.get(index)
    for pirate in d:
        if piratename.lower()==d[pirate]["name"].lower():
            #save the id because you can't delete while looping through a dictionary
            deletekey=pirate
    #use firebasemanager to delete from the db
    fm.DeletePirate(deletekey)
    #delete from dictionary
    d.pop(deletekey)
    listbox.delete(ANCHOR)


def onselect(e):
    w=e.widget
    try:
        index=int(w.curselection()[0])
        piratename=w.get(index)
        for pirate in d:
            if piratename.lower() == d[pirate]["name"].lower():
                display(pirate)
    except:
        pass

def new_pirate():
    global window2
    window2=Toplevel()
    Pirate.loadwindow(window2)
def fillListBox():
    global d
    print(d)
    for item in d:
        pirate=d[item]
        listbox.insert(END, pirate["name"])
    updateListbox(0)
def refresh_list():
    print("Bla bla bla")
    global d
    #refresh the dictionary from Firebase
    d=fm.getAll()
    #clear out the listbox
    listbox.delete(0,END)
    #refill the list box
    fillListBox()

def ext():
    window1.destroy()


def quitWindow():
    window1.destroy()
exitButton=Button(frame4,text="Exit",font=("Comic Sans MS",12),command=quitWindow)
exitButton.pack()


#Make the stuff


label1=Label(frame1,text="Pirate Database",font=("Comic Sans MS", 12))
label1.pack()

label2=Label(frame2,text="Search",font=("Comic Sans MS", 12))
label2.grid(row=0,column=0)



entry=Entry(frame2)
entry.bind("<KeyRelease>",searchUpdate)
entry.grid(row=0,column=1)

'''searchButton=Button(frame2,text="Go",font=("Comic Sans MS", 12))
searchButton.grid(row=0,column=2)'''



label3=Label(frame3,text="Frame 3",font=("Comic Sans MS", 12))
label3.grid(row=0,column=0)
leftImg=PhotoImage(file="arrow_left.gif")
rightImg=PhotoImage(file="arrow_right.gif")
leftButton=Button(frame3,image=leftImg,command=scrollLeft)
rightButton=Button(frame3,image=rightImg,command=scrollRight)
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
listbox.bind("<<ListboxSelect>>",onselect)
listbox.pack()
fm=firebasemanager.FirebaseManager()
d=fm.getAll()

fillListBox()
deleteButton=Button(frame4,text="Delete",font=("Comic Sans MS",12),command=listDelete)
deleteButton.pack()
newButton=Button(frame4,text="New Pirate",font=("Comic Sans MS",12),command=new_pirate)
newButton.pack()
refreshButton=Button(frame4,text="Refresh",font=("Comic Sans MS",12),command=refresh_list)
refreshButton.pack()



#Grid the stuff
frame1.grid(row=0,column=0)
frame2.grid(row=0,column=1)
frame3.grid(row=1,column=0)
frame4.grid(row=1,column=1)

window1.mainloop()
