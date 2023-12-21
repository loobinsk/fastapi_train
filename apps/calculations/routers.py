from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from config.database import get_async_session
from . import schemas
from . import models
from passlib.context import CryptContext
import secrets
import string
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def generate_random_token(length=32):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for i in range(length))

@router.post("/register", response_model=schemas.Token)
async def register_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_async_session)):
    """
    Регистрирует нового пользователя и выдает токен доступа.

    :param user: Данные нового пользователя.
    
    :return: Токен доступа.
    """
    # Создаем экземпляр отображаемого класса User
    db_user = models.User(username=user.username, password=pwd_context.hash(user.password))

    existing_user = await db.execute(select(models.User).where(models.User.username == user.username))
    existing_user = existing_user.scalars().first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Пользователь с таким именем уже существует")

    db.add(db_user)
    await db.commit()  # Сначала коммитим, чтобы сгенерировать user.id

    random_token = generate_random_token()
    token = models.Token(access_token=random_token, user_id=db_user.id)
    db.add(token)

    await db.commit()

    return {"access_token": random_token}

@router.post("/login", response_model=schemas.Token)
async def login_for_access_token(user_login: schemas.UserLogin, db: Session = Depends(get_async_session)):
    """
    Авторизует пользователя и выдает токен доступа.

    :param user_login: Учетные данные пользователя.

    :return: Токен доступа.
    """
    user = await db.execute(select(models.User).where(models.User.username == user_login.username))
    user = user.scalars().first()
    if not user or not pwd_context.verify(user_login.password, user.password):
        raise HTTPException(status_code=400, detail="Неверные учетные данные")

    # Ищем существующий токен для пользователя
    existing_token = await db.execute(select(models.Token).where(models.Token.user_id == user.id))
    existing_token = existing_token.scalars().first()

    if existing_token:
        return {"access_token": existing_token.access_token}

    raise HTTPException(status_code=400, detail="Токен не найден")

