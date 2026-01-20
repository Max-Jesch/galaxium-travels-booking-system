from pydantic import BaseModel, EmailStr
from typing import Optional, Literal

# Seat class type definition
SeatClass = Literal['economy', 'business', 'galaxium']


class FlightOut(BaseModel):
    flight_id: int
    origin: str
    destination: str
    departure_time: str
    arrival_time: str
    base_price: int  # Economy price (1x)
    economy_seats_available: int
    business_seats_available: int
    galaxium_seats_available: int
    # Computed prices for all classes
    economy_price: int
    business_price: int
    galaxium_price: int

    class Config:
        from_attributes = True


class BookingRequest(BaseModel):
    user_id: int
    name: str
    flight_id: int
    seat_class: SeatClass = 'economy'  # Default to economy


class BookingOut(BaseModel):
    booking_id: int
    user_id: int
    flight_id: int
    status: str
    booking_time: str
    seat_class: str
    price_paid: int

    class Config:
        from_attributes = True


class UserRegistration(BaseModel):
    name: str
    email: EmailStr


class UserOut(BaseModel):
    user_id: int
    name: str
    email: str

    class Config:
        from_attributes = True


class ErrorResponse(BaseModel):
    success: bool = False
    error: str
    error_code: str
    details: Optional[str] = None
