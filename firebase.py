import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
# Use a service account
cwd = os.getcwd()
cred = credentials.Certificate(cwd + '\\genshin-companion-deffd-02d741df701f.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

users_ref = db.collection(u'characters')
docs = users_ref.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')