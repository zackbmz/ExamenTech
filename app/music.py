from pydantic import BaseModel, validator
from utils import extract_initials_artist
from constants import MUSIC_TYPES

class Music(BaseModel):
    titre: str
    artist: str
    immat: str
    
    @validator('immat')
    def immat_is_valid(cls, v, values):
        if len(v) !=12:
            raise ValueError("L'immatriculation doit contenir 12 caractères")
        
        artist_field = values["artist"] 
        artist_initial = extract_initials_artist(artist_field)
        artist_initial_from_immat = v[:2]
        
        if artist_initial != artist_initial_from_immat:
            raise ValueError("l'immat dois commencer par les initial de l'artist")
        
        music_length = v[2:5]
        if not 60 <= int(music_length) <= 300:
            raise ValueError("La durée de la musique dois etre compris entre 60 et 300")
        
        
        music_types = v[5:8]
        if music_types not in MUSIC_TYPES:
            raise ValueError("l'immat doit contenir un type de musique valide")
        
        id_immat = v[8:]
        if (not id_immat.isdigit()) or "6" in id_immat:
            raise ValueError("l'immat dois etre un id et ne pas contenir de 6")
        
        
        return v