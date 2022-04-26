#import firebase admin
from time import sleep
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#use credentials
cred = credentials.Certificate('/Users/teo/Desktop/firebase-credentials.json')
app = firebase_admin.initialize_app(cred)
db=firestore.client(app)
doc_ref = db.collection(u'sensors').document(u'0')


#enter temp hum and light as numeric values
temp=input("Enter temp: ")
hum=input("Enter hum: ")
light=input("Enter light: ")


#convert to int and store in firebase
updating=0
while True:
    
    doc_ref.set({
    u'temp': int(temp),
    u'hum': int(hum),
    u'light': int(light),
    u'updating': updating
    })
    updating=updating+1
    if(updating==10):
        updating=0
    print("updating")
    doc = doc_ref.get()
    print(u'Document data: {}'.format(doc.to_dict()))
    sleep(5)
