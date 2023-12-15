import json
from fastapi import FastAPI
from pyrebase import pyrebase
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

fireBaseConfig = {

    'apiKey': "AIzaSyBRe8bCQ1MigB4PI9hAgFnBLNt5vR2O288",
    'authDomain': "sublime-mission-404920.firebaseapp.com",
    'databaseURL': "https://sublime-mission-404920-default-rtdb.firebaseio.com",
    'projectId': "sublime-mission-404920",
    'storageBucket': "sublime-mission-404920.appspot.com",
    'messagingSenderId': "589546934427",
    'appId': "1:589546934427:web:4a5efa72d7d9d3c048f63e",
    'measurementId': "G-ZM0PM6RH2G"
}

class ResponseOK(BaseModel):
    ok: bool = True
    result: dict


class ResponseError(BaseModel):
    ok: bool = False
    error_code: int
    description: str

firebase = pyrebase.initialize_app(fireBaseConfig)
auth = firebase.auth()
db = firebase.database()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_model=ResponseOK | ResponseError)
async def get_data():
    some_data = db.reference(f'/users').get()
    for data in some_data.each():



    #ec = some_data[0]
    #tds = some_data[1]
    #ec = ec.json()

    return {"ok": True, "result": some_data}
