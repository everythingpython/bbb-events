from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from db import Base

from datetime import datetime
import pytz

IST = pytz.timezone("Asia/Kolkata")

def convert_to_ist(utc_dt):
    """Convert UTC datetime to IST (UTC+05:30)."""
    return utc_dt.astimezone(IST).strftime("%Y-%m-%d %H:%M:%S %Z")  # Example: "2025-03-31 15:30:00 IST"


class Event(Base):
    __tablename__ = "events"


    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    date = Column(DateTime, default=datetime.utcnow)  # Change from String to DateTime
    location = Column(String)

    rsvps = relationship("RSVP", back_populates="event")

class RSVP(Base):
    __tablename__ = "rsvp"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"))

    event = relationship("Event", back_populates="rsvps")
