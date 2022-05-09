from time import sleep
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
import serialRead

cred = credentials.Certificate("./firebase-credential.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client(app)

updating=0

while updating<=10:

    dati = serialRead.read()

    doc_ref = db.collection(u"sensors").document(u"0")

    doc_ref.set({
        u"temp": int(float (dati[0])),
        u"hum": int(float(dati[1])),
        u"light": int(float (dati[2])),
        u"updating": updating
    })

    updating += 1
    if updating==10:
        updating=0

    sleep (2)

    print(doc_ref.get().to_dict())

"""
"sensors"(collection):
    "0"(document):
      temp,
      hum,
      light
"""