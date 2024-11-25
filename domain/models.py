from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, declarative_base

# from config.db import Base

Base = declarative_base()


class BuildingPart(Base):

    __tablename__ = "building_part"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)

    rooms = relationship("Room", back_populates="building_part")


class Room(Base):

    __tablename__ = "room"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    building_part_id: Mapped[int] = mapped_column(ForeignKey("building_part.id"))
    floor_num: Mapped[int] = mapped_column(Integer)

    building_part = relationship("BuildingPart", back_populates="rooms")
