from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from config.database import get_async_session
from . import schemas
from . import models
from sqlalchemy.future import select


async def verify_token(token: str, db: AsyncSession = Depends(get_async_session)) -> schemas.User:
    async with db.begin():
        # Ищем токен в базе данных
        db_token = await db.execute(select(models.Token).filter(models.Token.access_token == token))
        db_token = db_token.scalar()
        
        if db_token is None:
            raise HTTPException(status_code=401, detail="Неверный токен")
        
        user = await db.execute(select(models.User).filter(models.User.id == db_token.user_id))
        user = user.scalar()
        
        if user is None:
            raise HTTPException(status_code=401, detail="Пользователь не найден")
        
        return user