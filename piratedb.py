import json
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
