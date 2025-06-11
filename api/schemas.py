from datetime import datetime
from pydantic import BaseModel, computed_field


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    display_name: str
    admin: bool
    disabled: bool
    avatar_url: str | None = None
    last_login: datetime | None = None


class UserPublic(BaseModel):
    id: int
    display_name: str
    avatar_url: str | None = None


class UserUpdate(BaseModel):
    display_name: str | None = None


class GoogleLoginPayload(BaseModel):
    credential: str


class TokenResponse(BaseModel):
    access_token: str
    user: UserResponse


class UploadFileResponse(BaseModel):
    id: int
    name: str
    file_path: str
    created_on: datetime
    created_by_id: int

    @computed_field
    @property
    def url(self) -> str:
        return f"/uploads/{self.file_path}"
