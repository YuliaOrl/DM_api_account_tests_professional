from pydantic import BaseModel, ConfigDict, Field


class ChangeEmail(BaseModel):
    model_config = ConfigDict(extra="forbid")
    login: str = Field(..., description="Логин")
    password: str = Field(..., description="Пароль")
    email: str = Field(..., description="Новый email")
