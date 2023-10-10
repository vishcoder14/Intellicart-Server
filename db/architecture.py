import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# init. Firebase-Admin-SDK with SA-credentials
cred = credentials.Certificate(r'db\intelli-cart-firebase-adminsdk-cbztz-484657ac4f.json')
firebase_admin.initialize_app(cred)

# init. firestore client
cloudFirestore = firestore.client()

# firebase cloud collection references
ClientStatusData = cloudFirestore.collection('ClientStatusData')
HomeFragmentAssets = cloudFirestore.collection('HomeFragmentAssets')
IntellicartDeliveryApp = cloudFirestore.collection('IntellicartDeliveryApp')
IntellicartOrderApp = cloudFirestore.collection('IntellicartOrderApp')

# firebase cloud document references
serverData = IntellicartOrderApp.document('serverData')
userAppData = IntellicartOrderApp.document('userAppData')
deliveryPartnersOnDuty = ClientStatusData.document('deliveryPartnersOnDuty')


def get_manualCartProductData_ref(client_id: str):
    return userAppData.collection(str.strip(client_id)).document("userCartData").collection("cartItems").document(
        "manualCartProductData")


def get_voiceCartProductData_ref(client_id: str):
    return userAppData.collection(str.strip(client_id)).document("userCartData").collection("cartItems").document(
        "voiceCartProductData")


def get_orderByVoiceData_ref(client_id: str):
    return userAppData.collection(str.strip(client_id)).document("orderByVoiceData")


def get_inactivePartners_ref(ref_date: str):
    return deliveryPartnersOnDuty.collection(ref_date.upper()).document("inactivePartners")
