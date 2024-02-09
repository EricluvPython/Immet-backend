from DiscoveryComm import DiscoveryComm
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

if __name__ == "__main__":
    # connect to firebase
    cred = credentials.Certificate('lmmet-new-firebase-adminsdk-iwioc-619b101aba.json')
    firebase_admin.initialize_app(cred, {
        'databaseURL': "https://lmmet-new-default-rtdb.firebaseio.com/"
    })
    users = db.reference('/Users')
    print(users.get())

    # generate user id

    

    comm = DiscoveryComm()
    comm.start_network_discovery()
