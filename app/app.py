from fastapi import FastAPI
from pymongo import MongoClient
from bson import ObjectId

from music import Music
from store import Store

from constants import MUSIC_COLLECTION_NAME, STORE_COLLECTION_NAME, MONGO_HOST, DB_NAME
from parsers import parse_music_from_db, parse_store_from_db
from utils import (
    extract_initials_artist,
    extract_initials_artist_from_immat,
    extract_music_length_from_immat,
    extract_type_music_from_immat,
    extract_id_from_immat,
)

client = MongoClient(MONGO_HOST)
db = client[DB_NAME]
app = FastAPI()

#Music endpoints
@app.get("/musics")
def get_musics():
    musics = db[MUSIC_COLLECTION_NAME].find()
    
    return [parse_music_from_db(music) for music in musics]
    
@app.post("/musics")
def create_musics(music: Music):
    inserted_music = db[MUSIC_COLLECTION_NAME].insert_one(dict(music))
    
    #le signe | signifie la fusion entre 2 dictionnaire
    return {"_id": str(inserted_music.inserted_id)} | dict(music)

@app.get("/musics/{id}")
def get_music(id:str):
    music = db[MUSIC_COLLECTION_NAME].find_one({"_id": ObjectId(id)})
    
    if music is None:
        return {"message" "Music not found"}
    return parse_music_from_db(music) | {
        "music_initials": extract_initials_artist_from_immat(music["immat"]
        ),
        "music_length": extract_music_length_from_immat(music["immat"]
        ),
        "music_type": extract_type_music_from_immat(music["immat"]
        ),
        "music_id": extract_id_from_immat(music["immat"]),
    }