from sqlalchemy.orm import Session
from models import Flight
from schemas import FlightOut


def list_flights(db: Session) -> list[FlightOut]:
    """List all available flights with computed prices for all seat classes."""
    flights = db.query(Flight).all()
    result = []
    for f in flights:
        # Compute prices for all seat classes
        flight_dict = {
            'flight_id': f.flight_id,
            'origin': f.origin,
            'destination': f.destination,
            'departure_time': f.departure_time,
            'arrival_time': f.arrival_time,
            'base_price': f.base_price,
            'economy_seats_available': f.economy_seats_available,
            'business_seats_available': f.business_seats_available,
            'galaxium_seats_available': f.galaxium_seats_available,
            'economy_price': f.base_price,  # 1x
            'business_price': int(f.base_price * 2.5),  # 2.5x
            'galaxium_price': f.base_price * 5  # 5x
        }
        result.append(FlightOut(**flight_dict))
    return result
