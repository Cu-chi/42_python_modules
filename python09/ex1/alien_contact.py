from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
from pydantic_extra_types.pendulum_dt import DateTime
from datetime import datetime
from typing import Optional
from typing_extensions import Self


class ContactType(Enum):
    RADIO = "radio",
    VISUAL = "visual",
    PHYSICAL = "physical",
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: DateTime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500, default=None)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def check_data(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError("'contact_id' must start with 'AC'")
        contact_type_valid: bool = False
        for contact_type in ContactType:
            if self.contact_type.value == contact_type.value:
                contact_type_valid = True
                break
        if not contact_type_valid:
            raise ValueError(f"'{self.contact_type}' is not"
                             " a valid contact_type")
        if self.contact_type.value == ContactType.TELEPATHIC.value\
           and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at"
                             "least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("signal_strength >7.0 should"
                             " include message_received")
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("========================================")
    try:
        alien_contact: AlienContact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2026, 2, 27),
            contact_type=ContactType.RADIO,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )
        print("Valid contact report:")
        print(f"ID: {alien_contact.contact_id}")
        print(f"Type: {alien_contact.contact_type}")
        print(f"Location: {alien_contact.location}")
        print(f"Signal: {alien_contact.signal_strength}/10")
        print(f"Duration: {alien_contact.duration_minutes} "
              + ("minute" if alien_contact.duration_minutes == 1
                 else "minutes"))
        print(f"Witnesses: {alien_contact.witness_count}")
        print(f"Message: '{alien_contact.message_received}'")
    except ValidationError as e:
        print(e.errors()[0]["msg"])
    print("\n========================================")
    try:
        print("Expected validation error:")
        alien_contact: AlienContact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2026, 2, 27),
            contact_type=ContactType.TELEPATHIC,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli"
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"].split(",")[1].strip())


if __name__ == "__main__":
    main()
