from pydantic import BaseModel, validator
from music import Music
from typing import List
from constants import MUSIC_TYPES

class Store(BaseModel):
    music_type: str
    vinyles: List[Music] = []
    dvds: List[Music] = []
    
    @validator("music_type")
    def music_type_is_valid(cls, m):
        if m not in MUSIC_TYPES:
            raise ValueError("music_type must be a valid music type")
        return m
    
    def add_vinyle(self, m):
        self.vinyles.append(m)
        
    def remove_vinyle(self, title):
        if title in self.vinyles:
            self.vinyles.remove(title)
    
    def get_vinyle(self):
        return self.vinyles
        
    def add_dvds(self, m):
        self.dvds.append(m)
        
    def remove_dvds(self, title):
        if title in self.dvds:
            self.dvds.remove(title)
    
    def get_dvds(self):
        return self.dvds