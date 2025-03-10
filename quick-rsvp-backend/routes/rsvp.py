from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from models import RSVP, Event
from schemas import RSVPCreate, RSVPOut

router = APIRouter(prefix="/rsvp", tags=["RSVP"])

@router.post("/", response_model=RSVPOut)
def rsvp_for_event(rsvp: RSVPCreate, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == rsvp.event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    
    new_rsvp = RSVP(**rsvp.dict())
    db.add(new_rsvp)
    db.commit()
    db.refresh(new_rsvp)
    return new_rsvp

@router.get("/{event_id}", response_model=list[RSVPOut])
def get_rsvps_for_event(event_id: int, db: Session = Depends(get_db)):
    return db.query(RSVP).filter(RSVP.event_id == event_id).all()
