import logging
from sqlmodel import Session, select

from api.core.config import settings
from api.models import User

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init_users(session: Session):
    if not settings.SUPERUSER_GID:
        raise ValueError("Missing SUPERUSER_GID env variable.")

    existing = session.exec(
        select(User).where(User.google_user_id == settings.SUPERUSER_GID)
    ).first()

    if existing is not None:
        logger.warn("Superuser already exsits, skipping add.")
        return

    first_user = User.model_validate(
        {
            "username": "admin",
            "email": "admin@joelyoung.dev",
            "display_name": "admin",
            "admin": True,
            "google_user_id": settings.SUPERUSER_GID,
        }
    )
    session.add(first_user)
    session.commit()
    session.refresh(first_user)
    logger.info("Successfully created users")


def seed_database(session: Session):
    init_users(session)
