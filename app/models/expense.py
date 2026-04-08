import enum
import uuid
from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import Date, DateTime, Enum, ForeignKey, Index, JSON, Numeric, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin, UUIDMixin


class ExpenseStatus(str, enum.Enum):
    DRAFT = "draft"
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    RETURNED = "returned"


class Expense(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "expenses"
    __table_args__ = (
        Index("idx_expenses_org_status", "org_id", "status"),
        Index("idx_expenses_date", "expense_date"),
    )

    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    org_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=False)
    category_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("categories.id", ondelete="SET NULL"))
    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    currency: Mapped[str] = mapped_column(String(3), default="USD")
    expense_date: Mapped[date] = mapped_column(Date, nullable=False)
    merchant: Mapped[str | None] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(String(1000))
    status: Mapped[ExpenseStatus] = mapped_column(Enum(ExpenseStatus), default=ExpenseStatus.DRAFT)
    metadata_: Mapped[dict] = mapped_column("metadata", JSON, default=dict)
    submitted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

    user = relationship("User", back_populates="expenses")
    organization = relationship("Organization")
    category = relationship("Category", back_populates="expenses")
    receipts = relationship("Receipt", back_populates="expense", cascade="all, delete-orphan")
    approval_actions = relationship("ApprovalAction", back_populates="expense", cascade="all, delete-orphan")
