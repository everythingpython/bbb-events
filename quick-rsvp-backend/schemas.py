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

from pydantic import BaseModel
from datetime import datetime
import pytz


from pydantic import BaseModel
from datetime import datetime
from utils import convert_to_ist

class EventOut(BaseModel):
    id: int
    name: str
    description: str
    date: str  # Ensure date is a string
    location: str

    @classmethod
    def from_orm(cls, event):
        return cls(
            id=event.id,
            name=event.name,
            description=event.description,
            date=convert_to_ist(str(event.date)),  # Ensure IST conversion!
            location=event.location
        )
