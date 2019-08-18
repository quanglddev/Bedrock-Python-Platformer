# import only system from os 
from os import system, name 

# define our clear function 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

print(firebase_admin.__version__)

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# doc_ref = db.collection(u'users').document(u'alovelace')
# doc_ref.set({
#     u'first': u'Ada',
#     u'last': u'Lovelace',
#     u'born': 1815
# })
  
# users_ref = db.collection(u'users')
# docs = users_ref.stream()

# for doc in docs:
#     print(u'{} => {}'.format(doc.id, doc.to_dict()))

def on_snapshot(doc_snapshot, changes, read_time):
    clear()
    for doc in doc_snapshot:
        # print(u'Received document snapshot: {}'.format(doc.id))
        # print(u'{}'.format(doc.to_dict()['chat']))
        for chat in doc.to_dict()['chat']:
            print(chat)

doc_ref = db.collection(u'chats').document(u'sC0HB4cipYGJcPK4E8N5')

# Watch the document
doc_watch = doc_ref.on_snapshot(on_snapshot)
doc_watch.unsubscribe()