from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from models import Event
from schemas import EventCreate, EventOut

from sqlalchemy.orm import Session
from datetime import datetime
from fastapi import APIRouter, Depends
from db import get_db
from models import Event
from schemas import EventOut
router = APIRouter(prefix="/events", tags=["Events"])

@router.post("/", response_model=EventOut)
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    new_event = Event(**event.dict())
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event

# @router.get("/", response_model=list[EventOut])
# def get_events(db: Session = Depends(get_db)):
#     print(db)
#     print(dir(db)) 
#     return db.query(Event).all()

@router.get("/upcoming", response_model=list[EventOut])
def get_upcoming_events(db: Session = Depends(get_db)):
    today = datetime.utcnow()
    upcoming_events = db.query(Event).filter(Event.date >= today).all()
    return [EventOut.from_orm(event).dict() for event in upcoming_events]

@router.get("/past", response_model=list[EventOut])
def get_past_events(db: Session = Depends(get_db)):
    today = datetime.utcnow()
    past_events = db.query(Event).filter(Event.date < today).all()
    return [EventOut.from_orm(event).dict() for event in past_events]

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import Event
from schemas import EventOut, convert_to_ist


@router.get("/", response_model=list[EventOut])
def get_events(db: Session = Depends(get_db)):
    events = db.query(Event).all()

    # Convert each event into a dictionary with the correctly formatted date
    return [EventOut.from_orm(event).dict() for event in events]


