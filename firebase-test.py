import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('lmmet-new-firebase-adminsdk-iwioc-619b101aba.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://lmmet-new-default-rtdb.firebaseio.com/"
})

ref = db.reference('/Test')
print(ref.get())

