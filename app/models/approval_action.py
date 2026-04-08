import enum
import uuid
from datetime import datetime

from sqlalchemy import DateTime, Enum, ForeignKey, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, UUIDMixin


class ApprovalActionType(str, enum.Enum):
    APPROVED = "approved"
    REJECTED = "rejected"
    RETURNED = "returned"


class ApprovalAction(Base, UUIDMixin):
    __tablename__ = "approval_actions"

    expense_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("expenses.id", ondelete="CASCADE"), nullable=False, index=True)
    reviewer_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    policy_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("approval_policies.id"))
    action: Mapped[ApprovalActionType] = mapped_column(Enum(ApprovalActionType), nullable=False)
    comment: Mapped[str | None] = mapped_column(Text)
    acted_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    expense = relationship("Expense", back_populates="approval_actions")
    reviewer = relationship("User")
