from datetime import datetime
from enum import Enum
from typing import List, Optional, Union
from pydantic import BaseModel, Field, ConfigDict


class Rating(BaseModel):
    enabled: bool
    quality: int
    quantity: int


class BbParseMode(str, Enum):
    COMMON = "Common"
    INFO = "Info"
    POST = "Post"
    CHAT = "Chat "


class InfoBbText(BaseModel):
    value: str = Field(None)
    parse_mod: BbParseMode = Field(None, alias="parseMode")


class ColorSchema(str, Enum):
    MODERN = "Modern"
    PALE = "Pale"
    CLASSIC = "Classic"
    CLASSIC_PALE = "ClassicPale "
    NIGHT = "Night"


class PagingSettings(BaseModel):
    posts_per_page: int = Field(alias="postsPerPage")
    comments_per_page: int = Field(alias="commentsPerPage")
    topics_per_page: int = Field(alias="topicsPerPage")
    messages_per_page: int = Field(alias="messagesPerPage")
    entities_per_page: int = Field(alias="entitiesPerPage")


class UserSettings(BaseModel):
    color_schema: ColorSchema = Field(alias="colorSchema")
    nanny_greetings_message: str = Field(None, alias="nannyGreetingsMessage")
    paging: PagingSettings


class UserRole(str, Enum):
    GUEST = "Guest"
    PLAYER = "Player"
    ADMINISTRATOR = "Administrator"
    NANNYMODERATOR = "NannyModerator"
    REGULARMODERATOR = "RegularModerator"
    SENIORMODERATOR = "SeniorModerator"


class UserDetails(BaseModel):
    login: str = Field(None)
    roles: List[UserRole]
    medium_picture_url: str = Field(None, alias="mediumPictureUrl")
    small_picture_url: str = Field(None, alias="smallPictureUrl")
    status: str = Field(None)
    rating: Rating
    online: datetime = Field(None)
    name: str = Field(None)
    location: str = Field(None)
    registration: datetime = Field(None)
    icq: str = Field(None)
    skype: str = Field(None)
    original_picture_url: str = Field(None, alias="originalPictureUrl")
    info: Optional[Union[InfoBbText, str]] = Field(None)
    settings: UserSettings


class UserDetailsEnvelope(BaseModel):
    model_config = ConfigDict(extra="forbid")
    resource: Optional[UserDetails] = None
    metadata: Optional[str] = None
