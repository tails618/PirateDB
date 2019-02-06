import json
from tkinter import *
from random import randint
from tkinter import filedialog
from firebase import firebase as fb
import os
class Pirate:
    name=""
    ship=""
    fictional=False
    image=""
    def getDict(self):
        d={"name": self.name,
           "ship": self.ship,
           "fictional": self.fictional,
           "image": self.image
          }
        return d
    def loadFromDict(self,d):
        self.name=d["name"]
        self.ship=d["ship"]
        self.fictional=d["fictional"]
        self.image=f["image"]
class FirebaseManager:
    app=fb.FirebaseApplication("https://piratedb-f3ec8.firebaseio.com/",None)
    def writeToFile(self,idNum,obj):
        result=self.app.put("",idNum,obj)
def addNew():
    global win, namebox, shipbox, optionString, lbImage
    p=Pirate()
    p.name=namebox.get()
    p.ship=shipbox.get()
    p.fictional=optionString.get()
    #p.image=lbImage.cget("text")
    imgr.im.ImageManager()
    imgr.imagepath=win.filename
    imgr.uploadImage
    p.image=imgr.url
    print(imgr.url)
    namebox.delete(0,"end")
    shipbox.delete(0,"end")
    optionString.set("")
    lbImage.config(text="")
    d=p.getDict()
    fm=FirebaseManager()
    idNum=randint(11111,99999)
    fm.writeToFile(idNum,d)
    win.destroy()

def Canc():
    global win
    win.destroy()

def browseImage():
    global win,lbImage
    win.filename=filedialog.askopenfilename()
    justfile=os.path.basename(win.filename)
    lbImage.config(text=justfile)

def loadwindow(root):
    global win, namebox, shipbox, optionString, lbImage
    win=root
    root.title("Pirate Database")
    root.title("Pirate Database")
    title=Label(root,text="Pirate Database",font="BlackPearl")
    nametext=Label(root,text="Name",font="BlackPearl")
    namebox=Entry(root,font="BlackPearl")
    shiptext=Label(root,text="Ship",font="BlackPearl")
    fictext=Label(root,text="Fictional",font="BlackPearl")
    shipbox=Entry(root,font="BlackPearl")
    save=Button(root,text="SSSAAAVVVVEEEEE!!!!!!!!",font="BlackPearl",command=addNew)
    cancel=Button(root,text="Cancel...?",font="BlackPearl",command=Canc)
    cancel.grid(row=5,column=0)
    imgSelect=Button(root,font="BlackPearl", text="Select an Image", bg="lightGreen",command=browseImage)
    lbImage=Label(root,text="",font="BlackPearl")
    imgSelect.grid(row=4,column=0)
    lbImage.grid(row=4,column=1)
    title.grid(row=0,column=0,columnspan=3)
    nametext.grid(row=1,column=0,columnspan=1)
    namebox.grid(row=1,column=1,columnspan=2)
    shiptext.grid(row=2,column=0,columnspan=1)
    shipbox.grid(row=2,column=1,columnspan=2)
    fictext.grid(row=3,column=0,columnspan=1)
    save.grid(row=5,column=1,columnspan=2)
    optionString=StringVar(root)
    optionString.set("True")
    dropdown=OptionMenu(root,optionString,"True","False")
    dropdown.config(font="BlackPearl",width="10")
    dropdown.nametowidget(dropdown.menuname).config(font="BlackPearl")
    dropdown.grid(row=3,column=1,columnspan=2)
    root.mainloop()
