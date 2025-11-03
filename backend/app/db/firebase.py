import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("firebase-credentials.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://liulaoshistock-default-rtdb.asia-southeast1.firebasedatabase.app'
})

def get_db():
    return db
