import json
from tkinter import *
class Pirate:
    name=""
    ship=""
    fictional=False
    def getDict(self):
        d={"name": self.name,
           "ship": self.ship,
           "fictional": self.fictional
          }
        return d
    def loadFromDict(self,d):
        self.name=d["name"]
        self.ship=d["ship"]
        self.fictional=d["fictional"]
class FileManager:
    path="pirateDB.json"
    def writeToFile(self,idNum,obj):
        try:
            f=open(self.path,"r")
            d=json.load(f)
            f.close()
        except:
            d={}
        d[idNum]=obj
        f=open(self.path,"w")
        json.dump(d,f)
        f.close()
def addNew():
    x=0
root=Tk()
root.title("Pirate Database")
title=Label(root,text="Pirate Database",font="BlackPearl")
nametext=Label(root,text="Name",font="BlackPearl")
namebox=Entry(root,font="BlackPearl")
shiptext=Label(root,text="Ship",font="BlackPearl")
fictext=Label(root,text="Fictional",font="BlackPearl")
shipbox=Entry(root,font="BlackPearl")
save=Button(root,text="SSSAAAVVVVEEEEE!!!!!!!!",font="BlackPearl",command=addNew)
title.grid(row=0,column=0,columnspan=3)
nametext.grid(row=1,column=0,columnspan=1)
namebox.grid(row=1,column=1,columnspan=2)
shiptext.grid(row=2,column=0,columnspan=1)
shipbox.grid(row=2,column=1,columnspan=2)
fictext.grid(row=3,column=0,columnspan=1)
save.grid(row=4,column=0,columnspan=3)
optionString=StringVar(root)
optionString.set("True")
dropdown=OptionMenu(root,optionString,"True","False")
dropdown.config(font="BlackPearl",width="10")
dropdown.nametowidget(dropdown.menuname).config(font="BlackPearl")
dropdown.grid(row=3,column=1,columnspan=2)
root.mainloop()
