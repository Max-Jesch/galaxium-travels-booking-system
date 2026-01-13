from pydantic import BaseModel, EmailStr
from typing import Optional


class FlightOut(BaseModel):
    flight_id: int
    origin: str
    destination: str
    departure_time: str
    arrival_time: str
    price: int
    seats_available: int

    class Config:
        from_attributes = True


class BookingRequest(BaseModel):
    user_id: int
    name: str
    flight_id: int


class BookingOut(BaseModel):
    booking_id: int
    user_id: int
    flight_id: int
    status: str
    booking_time: str

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
