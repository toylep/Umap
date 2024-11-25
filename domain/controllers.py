from domain.models import Room
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from config.db import AsyncSessionLocal
from domain.dto import RoomDTO
from sqlalchemy.future import select
router = APIRouter()

@router.get("/rooms")
async def get_rooms():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Room))
        rooms = [RoomDTO.from_orm(room).dict() for room in result.scalars().all()]
        
    return JSONResponse(content=rooms)

@router.post("/rooms")
async def add_room(room: RoomDTO):
    async with AsyncSessionLocal() as session:
        new_room = Room(**room.dict())
        session.add(new_room)
        await session.commit()
    return JSONResponse(content={"success": "ok"})

