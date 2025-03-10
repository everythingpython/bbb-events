from fastapi import FastAPI
from db import engine, Base
from routes import events, rsvp

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all domains (change this for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Create database tables
Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(events.router)
app.include_router(rsvp.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Quick RSVP"}
