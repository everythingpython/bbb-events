from datetime import datetime
import pytz

IST = pytz.timezone("Asia/Kolkata")

def convert_to_ist(utc_dt: datetime) -> str:
    """Convert UTC datetime to IST (UTC+05:30) and return as a string."""
    if isinstance(utc_dt, str):
        utc_dt = datetime.fromisoformat(utc_dt)  # Convert string to datetime
    
    if utc_dt.tzinfo is None:  # If naive, assume UTC
        utc_dt = utc_dt.replace(tzinfo=pytz.utc)
    
    ist_dt = utc_dt.astimezone(IST)
    return ist_dt.strftime("%Y-%m-%d %H:%M:%S %Z")  # Example: "2025-02-23 15:30:00 IST"
