from google.cloud import storage
import os
import datetime

class ImageManager:
#this tells the project where to find the credentials we downloaded
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="pirateDB-a1c1dd245fa5.json"
    client=storage.Client()
    bucket=client.get_bucket('piratedb-f3ec8.appspot.com')
    url=''
    imagepath="me.gif"
    def uploadImage(self):
        imageBlob=self.bucket.blob("images/"+os.path.basename(self.imagepath))
        imageBlob.upload_from_filename(self.imagepath)
        d=datetime.datetime(2006,12,18)
        self.url=imageBlob.generate_signed_url(d)
    def downloadUrl(self):
