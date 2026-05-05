import logging

# Configure logging for debugging
logging.basicConfig(level=logging.DEBUG)

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from connection import send_to_event_hub, generate_uber_ride_confirmation
from jinja2 import Environment, FileSystemLoader

app = FastAPI()
templates = Jinja2Templates(
    env=Environment(loader=FileSystemLoader("templates"), cache_size=0)
)

@app.get("/")
def booking_home():
    return {"message": "Welcome to the Ride Booking API!"}


@app.get("/book")
def book_ride(request: Request):  
    ride = generate_uber_ride_confirmation()
    result = send_to_event_hub(ride)
    return {"message": "Booked!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)