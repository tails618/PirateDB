from firebase import firebase as fb
class FirebaseManager:
    app=fb.FirebaseApplication("https://piratedb-f3ec8.firebaseio.com/")
    def writeToFile(self,idNum,obj):
        result=self.app.put("",idNum,obj)
    def getAllPirates(self):
        d=self.app.get("",None)
        return d

    def DeletePirate(self,id):
        self.app.delete(id,None)
