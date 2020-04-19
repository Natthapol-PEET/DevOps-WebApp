import pyrebase

# config = {
#   "apiKey": "AIzaSyDKqw81UDwGDiJJSjHF7uQI-AECzbz9S9w",
#   "authDomain": "g0lineapi-opxykx.firebaseapp.com",
#   "databaseURL": "https://g0lineapi-opxykx.firebaseio.com",
#   "storageBucket": "g0lineapi-opxykx.appspot.com",
#   "serviceAccount": "serviceAccountCredentials.json"
# }

config = {
  "apiKey": "09f74a83d364da911cafe68fca995b42a70d1d9d",
  "authDomain": "g0lineapi-opxykx.firebaseapp.com",
  "databaseURL": "https://g0lineapi-opxykx.firebaseio.com",
  "storageBucket": "g0lineapi-opxykx.appspot.com",
  "serviceAccount": "serviceAccountCredentials.json"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

# storage.child("image/new.jpg").put("image.jpg")

img_name = 'coff.PNG'
storage.child(img_name).download(img_name)

# url = storage.child("login.png").get_url(None)
# print(url)
