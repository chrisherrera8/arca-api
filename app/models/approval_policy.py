import uuid
from decimal import Decimal

from sqlalchemy import Boolean, Enum, ForeignKey, Numeric, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin, UUIDMixin
from app.models.user import UserRole


class ApprovalPolicy(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "approval_policies"

    org_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    threshold_amount: Mapped[Decimal | None] = mapped_column(Numeric(12, 2))
    approver_role: Mapped[UserRole] = mapped_column(Enum(UserRole), default=UserRole.MANAGER)
    auto_approve_below: Mapped[Decimal | None] = mapped_column(Numeric(12, 2))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    organization = relationship("Organization", back_populates="approval_policies")
