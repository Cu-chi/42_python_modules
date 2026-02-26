from pydantic import BaseModel, Field, ValidationError
from pydantic_extra_types.pendulum_dt import DateTime
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: DateTime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(max_length=200, default=None)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    try:
        space_station: SpaceStation = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            last_maintenance=datetime(2026, 2, 26),
            oxygen_level=92.3
        )
        print("Valid station created:")
        print(f"ID: {space_station.station_id}")
        print(f"Name: {space_station.name}")
        print(f"Crew: {space_station.crew_size} people")
        print(f"Power: {space_station.power_level}%")
        print(f"Oxygen: {space_station.oxygen_level}%")
        print("Status: " + ("Operational" if space_station.is_operational
              else "Inoperative"))
    except ValidationError as e:
        print(e.errors()[0]["msg"])
    print("\n========================================")
    try:
        print("Expected validation error:")
        space_station: SpaceStation = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=60,
            power_level=85.5,
            last_maintenance=datetime(2026, 2, 26),
            oxygen_level=92.3
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
