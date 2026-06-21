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
    login: Optional[str] = Field(None)
    roles: List[UserRole]
    medium_picture_url: Optional[str] = Field(None, alias="mediumPictureUrl")
    small_picture_url: Optional[str] = Field(None, alias="smallPictureUrl")
    status: Optional[str] = Field(None, alias="status")
    rating: Rating
    online: Optional[datetime] = Field(None, alias="online")
    name: Optional[str] = Field(None, alias="name")
    location: Optional[str] = Field(None, alias="location")
    registration: Optional[datetime] = Field(None)


class UserEnvelope(BaseModel):
    model_config = ConfigDict(extra="forbid")
    resource: User
    metadata: Optional[Union[str, Dict[str, Any]]] = None
