import datetime
import random
import uuid
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials


cred = credentials.Certificate("safeets.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


dateNow = datetime.datetime.now()
# print(dateNow.strftime("%d/%m/%Y %H:%M:%S"))


UID = str(uuid.uuid4())

worker = random.choice(['Lucas', 'Tayssa', 'Leonardo', 'Raissa', 'Gustavo', 'Nicolas', 'Tiago'])
tag = 1231412

doc_ref = db.collection(u'registros').document(UID)
varpraver = doc_ref.set({
    'Colaborador': worker,
    'Tag': tag,
    'Horario': dateNow.strftime("%d/%m/%Y %H:%M:%S")
})

print(varpraver)