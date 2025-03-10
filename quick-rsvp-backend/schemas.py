from pydantic import BaseModel
from typing import List, Optional

class RSVPBase(BaseModel):
    name: str
    email: str

class RSVPCreate(RSVPBase):
    event_id: int

class RSVPOut(RSVPBase):
    id: int
    event_id: int

from pydantic import BaseModel
from datetime import datetime

class EventBase(BaseModel):
    name: str
    description: str
    date: datetime  # Ensure datetime type
    location: str


class EventCreate(EventBase):
    pass

class EventOut(EventBase):
    id: int
    rsvps: List[RSVPOut] = []

    class Config:
        orm_mode = True
