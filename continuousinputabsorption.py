import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

newLines = db.collection(u'chats').document(u'sC0HB4cipYGJcPK4E8N5')

while True:
    userInput = input()
    newLines.update({u'chats': firestore.ArrayUnion([u'userInput'])})
