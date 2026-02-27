from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
from pydantic_extra_types.pendulum_dt import DateTime
from datetime import datetime
from typing_extensions import Self


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: DateTime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def check_data(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError("'mission_id' must start with 'M'")
        crew_valid: bool = False
        for crew_member in self.crew:
            if crew_member.rank.value == Rank.COMMANDER.value\
               or crew_member.rank.value == Rank.CAPTAIN.value:
                crew_valid = True
        if not crew_valid:
            raise ValueError("Mission must have at least"
                             " one Commander or Captain")
        if self.duration_days > 365:
            crew_len: int = len(self.crew)
            total_experienced: int = sum([
                1 for member in self.crew
                if member.years_experience >= 5
            ])
            if total_experienced / crew_len < 0.5:
                raise ValueError("crew is not experienced")
        for member in self.crew:
            if not member.is_active:
                raise ValueError("all crew members must be active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("========================================")
    try:
        mission: SpaceMission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2026, 2, 27),
            duration_days=900,
            mission_status="planned",
            crew=[
                CrewMember(
                        member_id="CM001",
                        name="Sarah Williams",
                        rank=Rank.CAPTAIN,
                        age=43,
                        specialization="Mission Command",
                        years_experience=19,
                        is_active=True
                ),
                CrewMember(
                        member_id="CM002",
                        name="James Hernandez",
                        rank=Rank.CAPTAIN,
                        age=43,
                        specialization="Pilot",
                        years_experience=30,
                        is_active=True
                ),
                CrewMember(
                        member_id="CM003",
                        name="Anna Jones",
                        rank=Rank.CADET,
                        age=35,
                        specialization="Communications",
                        years_experience=15,
                        is_active=True
                ),
            ],
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} "
              + ("day" if mission.duration_days == 1
                 else "days"))
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for member in mission.crew:
            print(f"- {member.name} ({member.rank.value})"
                  f"- {member.specialization}")
    except ValidationError as e:
        print(e.errors()[0]["msg"])
    print("\n========================================")
    try:
        print("Expected validation error:")
        mission: SpaceMission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2026, 2, 27),
            duration_days=900,
            mission_status="planned",
            crew=[
                CrewMember(
                        member_id="CM001",
                        name="Sarah Williams",
                        rank=Rank.CADET,
                        age=43,
                        specialization="Mission Command",
                        years_experience=19,
                        is_active=True
                ),
                CrewMember(
                        member_id="CM002",
                        name="James Hernandez",
                        rank=Rank.CADET,
                        age=43,
                        specialization="Pilot",
                        years_experience=30,
                        is_active=True
                ),
                CrewMember(
                        member_id="CM003",
                        name="Anna Jones",
                        rank=Rank.CADET,
                        age=35,
                        specialization="Communications",
                        years_experience=15,
                        is_active=True
                ),
            ],
            budget_millions=2500.0
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"].split(",")[1].strip())


if __name__ == "__main__":
    main()
