import enum
import uuid
from datetime import datetime

from sqlalchemy import DateTime, Enum, ForeignKey, Integer, JSON, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, UUIDMixin


class OCRStatus(str, enum.Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class Receipt(Base, UUIDMixin):
    __tablename__ = "receipts"

    expense_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("expenses.id", ondelete="CASCADE"), nullable=False)
    storage_path: Mapped[str] = mapped_column(String(500), nullable=False)
    file_name: Mapped[str] = mapped_column(String(255), nullable=False)
    file_type: Mapped[str] = mapped_column(String(50), nullable=False)
    file_size: Mapped[int | None] = mapped_column(Integer)
    ocr_data: Mapped[dict] = mapped_column(JSON, default=dict)
    ocr_status: Mapped[OCRStatus] = mapped_column(Enum(OCRStatus), default=OCRStatus.PENDING)
    uploaded_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    expense = relationship("Expense", back_populates="receipts")
