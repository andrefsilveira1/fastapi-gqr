from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Submission(Base):
    __tablename__ = "submission"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    createdAt = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), nullable=False)

    data = relationship("Data", back_populates="submission", uselist=False)
