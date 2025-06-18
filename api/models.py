from datetime import datetime, timezone
from enum import Enum
from sqlalchemy import MetaData
from sqlmodel import Relationship, SQLModel, Field

from api.core.timezone_handler import UTCDateTime


# Create common Base to be used by all models
class BaseDbModel(SQLModel):
    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_`%(constraint_name)s`",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )

    __abstract__ = True


class BaseIndexedDbModel(BaseDbModel):
    __abstract__ = True
    id: int | None = Field(default=None, index=True, primary_key=True)


class SubscriptionLevel(Enum):
    FREE = None
    PRO = 10
    ENTERPRISE = 20


class ProjectStatus(Enum):
    CREATED = None
    IDEA = 10
    PLAN = 20
    ACTIVE = 30
    COMPLETE = 40
    ARCHIVED = 50
    CANCELLED = 60


class TaskStatus(Enum):
    CREATED = None
    IN_PROGRESS = 10
    COMPLETED = 20
    CANCELLED = 30


class TaskTier(Enum):
    TIER_1 = 10
    TIER_2 = 20
    TIER_3 = 30


class User_Permission(BaseDbModel, table=True):
    user_id: int = Field(default=None, foreign_key="user.id", primary_key=True)
    permission_id: int = Field(
        default=None, foreign_key="permission.id", primary_key=True
    )


class User(BaseIndexedDbModel, table=True):
    avatar_url: str | None = None
    username: str
    email: str
    display_name: str
    admin: bool = False
    disabled: bool = False
    google_user_id: str | None = None
    last_login: datetime | None = Field(
        default_factory=lambda: datetime.now(tz=timezone.utc), sa_type=UTCDateTime
    )
    sub_level: SubscriptionLevel = SubscriptionLevel.FREE

    tokens: list["Token"] = Relationship(back_populates="user")
    permissions: list["Permission"] = Relationship(link_model=User_Permission)


class TokenType(Enum):
    Access = 10


class Token(BaseIndexedDbModel, table=True):
    user_id: int = Field(foreign_key="user.id")
    access_token: str
    token_type: TokenType

    user: "User" = Relationship(back_populates="tokens")


class Permission(BaseIndexedDbModel, table=True):
    name: str


class Upload(BaseIndexedDbModel, table=True):
    created_by_id: int = Field(foreign_key="user.id")
    created_on: datetime = Field(sa_type=UTCDateTime)
    file_path: str
    name: str

    created_by: "User" = Relationship()


class Project(BaseIndexedDbModel, table=True):
    created_by_id: int = Field(foreign_key="user.id")
    created_on: datetime = Field(sa_type=UTCDateTime)
    name: str
    description: str
    status: ProjectStatus
    budget: float
    public: bool = False
    published_on: datetime | None = Field(sa_type=UTCDateTime)
    showcase: bool = False
    duration: float = 0
    start_date: datetime | None = Field(sa_type=UTCDateTime)

    created_by: "User" = Relationship()
    expenses: list["Expense"] = Relationship(back_populates="project")


class Expense(BaseIndexedDbModel, table=True):
    project_id: int = Field(foreign_key="project.id")
    name: str
    description: str
    amount: float
    date: datetime = Field(sa_type=UTCDateTime)

    project: "Project" = Relationship()


class ProjectImage(BaseIndexedDbModel, table=True):
    project_id: int = Field(foreign_key="project.id")
    upload_id: int = Field(foreign_key="upload.id")

    project: "Project" = Relationship()
    upload: "Upload" = Relationship()


class Tag(BaseIndexedDbModel, table=True):
    name: str


class ProjectTag(BaseIndexedDbModel, table=True):
    project_id: int = Field(foreign_key="project.id")
    tag_id: int = Field(foreign_key="tag.id")

    project: "Project" = Relationship()
    tag: "Tag" = Relationship()


class Like(BaseIndexedDbModel, table=True):
    user_id: int = Field(foreign_key="user.id")
    project_id: int = Field(foreign_key="project.id")

    user: "User" = Relationship()
    project: "Project" = Relationship()


class TimeLog(BaseIndexedDbModel, table=True):
    project_id: int = Field(foreign_key="project.id")
    user_id: int = Field(foreign_key="user.id")
    date: datetime = Field(sa_type=UTCDateTime)
    hours: float = 0

    project: "Project" = Relationship()
    user: "User" = Relationship()


class Collaborator(BaseIndexedDbModel, table=True):
    project_id: int = Field(foreign_key="project.id")
    user_id: int = Field(foreign_key="user.id")

    project: "Project" = Relationship()
    user: "User" = Relationship()


class Task(BaseIndexedDbModel, table=True):
    project_id: int = Field(foreign_key="project.id")
    name: str
    description: str
    status: TaskStatus
    tier: TaskTier
    due_date: datetime | None = Field(sa_type=UTCDateTime)

    project: "Project" = Relationship()
