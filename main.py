import datetime
import random
import uuid
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials


cred = credentials.Certificate("safeets.json")
firebase_admin.initialize_app(cred)
db = firestore.client()





worker = random.choice(['Lucas', 'Tayssa', 'Leonardo', 'Raissa', 'Gustavo', 'Nicolas', 'Tiago'])
tag = 1231412


document = ({
    'Colaborador': worker,
    'Tag': tag,
    'Horario': firestore.SERVER_TIMESTAMP
})
response = db.collection(u'registros').add(document)

print(response)