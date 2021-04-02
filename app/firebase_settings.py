import pyrebase

config = {
    "apiKey": "AIzaSyCoqxBFjtSrr5F51sqVwkU-VWpftl_R6FU",
    "authDomain": "e-commerce-19b59.firebaseapp.com",
    "projectId": "e-commerce-19b59",
    "storageBucket": "e-commerce-19b59.appspot.com",
    "messagingSenderId": "550026983047",
    "databaseURL" :"gs://e-commerce-19b59.appspot.com",
    "appId": "1:550026983047:web:baa439f7cd478d819faa22",
    "measurementId": "G-7KYFDE0TLZ"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()