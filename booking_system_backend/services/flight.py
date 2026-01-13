from sqlalchemy.orm import Session
from models import Flight
from schemas import FlightOut


def list_flights(db: Session) -> list[FlightOut]:
    """List all available flights."""
    flights = db.query(Flight).all()
    return [FlightOut.model_validate(f) for f in flights]
