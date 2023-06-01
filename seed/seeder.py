from pymongo import MongoClient
from bson import ObjectId

MONGO_HOST = "mongodb"
DB_NAME = "store_music"
MUSIC_COLLECTION_NAME = "music"
STORE_COLLECTION_NAME = "store"

client = MongoClient(MONGO_HOST)
db = client[DB_NAME]

store = {"_id": ObjectId(), "music_type": "POP"}

vinyls = [
    {
        "_id": ObjectId(),
        "title": "Thriller",
        "artist": "Michael Jackson",
        "immat": "MJ281POP0001"
    },
    {
        "_id": ObjectId(),
        "title": "bad",
        "artist": "Michael Jackson",
        "immat": "MJ281POP0002"
    },
]

dvds = [
    {
        "_id": ObjectId(),
        "title": "J'me tire",
        "artist": "Maitre Gims",
        "immat": "MG281POP0003"
    },
    {
        "_id": ObjectId(),
        "title": "fvuk Juv",
        "artist": "Paolo Gybala",
        "immat": "PG281POP0004"
    },
]

musics = vinyls + dvds

#Insérer les données 
db[STORE_COLLECTION_NAME].insert_one(store)

db[MUSIC_COLLECTION_NAME].insert_many(musics)

#Ajouts des vinyls et dvds dans le store crée
db[STORE_COLLECTION_NAME].update_one(
    {"_id": store["_id"]},
    {"$set": {"vinyls": [v["_id"] for v in vinyls], "dvds": [d["_id"] for d in dvds]}},
)