from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
from pydantic_extra_types.pendulum_dt import DateTime
from datetime import datetime
from typing import Optional, Self


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
    def check_contact_id(self) -> Self:
        return self
