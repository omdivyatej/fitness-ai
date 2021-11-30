import pyrebase

config={
  "apiKey": "AIzaSyAbCkkO6PyRjmM-DhXHKFr6mmMOmMyZr7A",
  "authDomain": "ketorunner-e76ad.firebaseapp.com",
  "databaseURL": "https://ketorunner-e76ad-default-rtdb.firebaseio.com",
  "projectId": "ketorunner-e76ad",
  "storageBucket": "ketorunner-e76ad.appspot.com",
  "messagingSenderId": "454061422073",
  "appId": "1:454061422073:web:fec156a132774ae0aa3928"
}

firebase = pyrebase.initialize_app(config)
db=firebase.database()
