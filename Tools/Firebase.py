import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class Firebase:
    def __init__(self):
        cred = credentials.Certificate("serviceAccountKey.json")
        firebase_admin.initialize_app(cred)

        self.db = firestore.client()

    def getFirebaseDB(self):
        return self.db

    def activateChat(self, chatID):
        # TODO: Create new chat here
        # TODO: Open one listener and writer
        # def on_snapshot(doc_snapshot, changes, read_time):
        #     clear()
        #     for doc in doc_snapshot:
        #         # print(u'Received document snapshot: {}'.format(doc.id))
        #         # print(u'{}'.format(doc.to_dict()['chat']))
        #         for chat in doc.to_dict()['chat']:
        #             print(chat)

        # doc_ref = db.collection(u'chats').document(u'sC0HB4cipYGJcPK4E8N5')

        # # Watch the document
        # doc_watch = doc_ref.on_snapshot(on_snapshot)
        # doc_watch.unsubscribe()
        pass
