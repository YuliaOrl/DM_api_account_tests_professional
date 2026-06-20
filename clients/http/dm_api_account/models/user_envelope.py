from datetime import datetime
from enum import Enum
from typing import List, Optional, Union, Dict, Any
from pydantic import BaseModel, Field, ConfigDict


class Rating(BaseModel):
    enabled: bool
    quality: int
    quantity: int


class UserRole(str, Enum):
    GUEST = "Guest"
    PLAYER = "Player"
    ADMINISTRATOR = "Administrator"
    NANNYMODERATOR = "NannyModerator"
    REGULARMODERATOR = "RegularModerator"
    SENIORMODERATOR = "SeniorModerator"


class User(BaseModel):
    login: str = Field(None)
    roles: List[UserRole]
    medium_picture_url: str = Field(None, alias="mediumPictureUrl")
    small_picture_url: str = Field(None, alias="smallPictureUrl")
    status: str = Field(None, alias="status")
    rating: Rating
    online: datetime = Field(None, alias="online")
    name: str = Field(None, alias="name")
    location: str = Field(None, alias="location")
    registration: datetime = Field(None)


class UserEnvelope(BaseModel):
    model_config = ConfigDict(extra="forbid")
    resource: Optional[User] = None
    metadata: Optional[Union[str, Dict[str, Any]]] = None
