from pydantic import BaseModel
from typing import Optional


class CustomModel(BaseModel):
    id: Optional[int] = None

    class Config:
        from_attributes = True


class RoomDTO(CustomModel):
    name: str
    floor_num: int
    building_part_id: int


class BuildingPartDTO(CustomModel):
    name: str
