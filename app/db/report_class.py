from sqlalchemy import Column, Integer, Float, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class Data(Base):
    __tablename__ = "data"

    id = Column(Integer, primary_key=True, autoincrement=True)
    depth = Column(Float, nullable=False)
    c1 = Column(Float, nullable=False)
    c2 = Column(Float, nullable=False)
    c3 = Column(Float, nullable=False)
    nc4 = Column(Float, nullable=False)
    ic4 = Column(Float, nullable=False)
    nc5 = Column(Float, nullable=False)
    ic5 = Column(Float, nullable=False)
    TotalGas = Column(Float, nullable=False)
    submissionId = Column(Integer, ForeignKey("user.id"), nullable=False)
    createdAt = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), nullable=False)

    submitter = relationship("User", back_populates="recipes")
