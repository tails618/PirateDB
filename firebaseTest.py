from firebase import firebase as fb
app=fb.FirebaseApplication("https://piratedb-f3ec8.firebaseio.com/",None)
d=app.get("14504","name")
print(d)
newPirate={"name":"Davy Jones","ship":"Flying Dutchman","fictional":"True"}
result=app.put("","3.141592",newPirate)
print(result)
