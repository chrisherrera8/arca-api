from sqlalchemy import JSON, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin, UUIDMixin


class Organization(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "organizations"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    plan: Mapped[str] = mapped_column(String(20), default="free")
    default_currency: Mapped[str] = mapped_column(String(3), default="USD")
    settings: Mapped[dict] = mapped_column(JSON, default=dict)

    users = relationship("User", back_populates="organization", cascade="all, delete-orphan")
    categories = relationship("Category", back_populates="organization", cascade="all, delete-orphan")
    approval_policies = relationship("ApprovalPolicy", back_populates="organization", cascade="all, delete-orphan")
