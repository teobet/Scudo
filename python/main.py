from time import sleep
import firebase_admin
import time
from firebase_admin import credentials
from firebase_admin import firestore
import serialRead

# Use the application default credentials
#print time.strftime("%a %b %d %H:%M:%S %Y", parsed)


cred = credentials.Certificate("./credentials.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client(app)

updating = 0
nstorico = 0

doc_ref = db.collection(u"sensors").document(u"0")
storico_ref = []

for i in range(10):
    storico_ref.append(db.collection(u"storico").document(u"{}".format(i)))
    #print(storico_ref[i].get().to_dict())

hum=0
temp=0
light=0

while updating<=10:

    dati = serialRead.read()

    temp=int(float (dati[0]))
    hum = int(float(dati[1]))
    light=int(float (dati[2]))

    now = time.ctime()
    parsed = time.strptime(now)
    time1 = time.strftime("Giorno: %d; Ora: %H:%M:%S", parsed)

    doc_ref.set({
        u"temp": temp,
        u"hum": hum,
        u"light": light,
        u"updating": updating
    })

    updating += 1
    nstorico += 1
    if updating==10:
        updating=0

    if nstorico==50: #per 1 ora = 1800
        for i in range(9, 0, -1):
            storico_ref[i].set(storico_ref[i-1].get().to_dict())

        storico_ref[0].set({
            u"temp": temp,
            u"hum": hum,
            u"light": light,
            u"time": time1
        })

        nstorico=0


    sleep (2)

    print(doc_ref.get().to_dict())
    print(time1)

"""
"sensors"(collection):
    "0"(document):
      temp,
      hum,
      light
"""