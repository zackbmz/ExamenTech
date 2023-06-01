def extract_initials_artist(artist):
    if len(artist.split()) == 2:
        return "".join([x[0].upper() for x in artist.split(" ")])
    
def extract_initials_artist_from_immat(immat: str):
    return immat[:2]

def extract_music_length_from_immat(immat: str):
    return immat [2:5]

def extract_type_music_from_immat(immat: str):
    return immat [5:8]

def extract_id_from_immat(immat: str):
    return immat [8:]