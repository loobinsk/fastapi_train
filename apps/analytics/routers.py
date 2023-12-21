from fastapi import Depends, HTTPException, APIRouter, Security
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from config.database import get_async_session
from . import schemas
from apps.account.schemas import User
from . import models
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import status
from typing import List
from fastapi.security import OAuth2PasswordBearer
# Импортируем функцию для проверки токена
from apps.account.security import verify_token
from typing_extensions import Annotated
from fastapi.responses import JSONResponse

router = APIRouter()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("", tags=["articles"])
async def create_article(article: schemas.ArticleCreate, 
                        token: Annotated[str, Depends(oauth2_scheme)], 
                        db: AsyncSession = Depends(get_async_session)):
    """
    Создать новую статью.
    """
    db_article = models.Article(**article.dict(), author_id=current_user.id)

    db.add(db_article)
    await db.commit()
    db.refresh(db_article)
    
    return JSONResponse(content={"status": "success"}, status_code=status.HTTP_201_CREATED)

@router.get("", response_model=List[schemas.ArticleRead], tags=["articles"])
async def get_all_articles(token: Annotated[str, Depends(oauth2_scheme)], db: AsyncSession = Depends(get_async_session)):
    """
    Получить все статьи.
    """
    query = select(models.Article)
    result = await db.execute(query)
    articles = result.scalars().all()

    # Преобразовать объекты SQLAlchemy в словари
    article_dicts = [dict(article.__dict__) for article in articles]

    # Создать экземпляры схем Pydantic
    articles_response = [schemas.ArticleRead(**article_dict) for article_dict in article_dicts]

    return articles_response

@router.get("/articles/{article_id}", response_model=schemas.ArticleRead, tags=["articles"])
async def read_article(article_id: int, db: AsyncSession = Depends(get_async_session)):
    """
    Получить статью по её идентификатору.
    """
    article = await db.execute(models.Article.__table__.select().where(models.Article.id == article_id))
    article = article.scalars().first()
    if not article:
        raise HTTPException(status_code=404, detail="Статья не найдена")
    return article

@router.put("/articles/{article_id}", response_model=schemas.ArticleRead, tags=["articles"])
async def update_article(
    article_id: int, 
    article: schemas.ArticleUpdate, 
    db: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(verify_token),  # Проверяем токен
):
    """
    Обновить статью по её идентификатору.
    """
    db_article = await db.execute(models.Article.__table__.select().where(models.Article.id == article_id))
    db_article = db_article.scalars().first()
    if not db_article:
        raise HTTPException(status_code=404, detail="Статья не найдена")
    
    if db_article.author_id != current_user.id:
        raise HTTPException(status_code=403, detail="Вы не автор этой статьи")
    
    for key, value in article.dict().items():
        setattr(db_article, key, value)
    
    await db.commit()
    db.refresh(db_article)
    return db_article

@router.delete("/articles/{article_id}", response_model=None, status_code=status.HTTP_204_NO_CONTENT, tags=["articles"])
async def delete_article(
    article_id: int, 
    db: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(verify_token),  # Проверяем токен
):
    """
    Удалить статью по её идентификатору.
    """
    db_article = await db.execute(models.Article.__table__.select().where(models.Article.id == article_id))
    db_article = db_article.scalars().first()
    if not db_article:
        raise HTTPException(status_code=404, detail="Статья не найдена")
    
    if db_article.author_id != current_user.id:
        raise HTTPException(status_code=403, detail="Вы не автор этой статьи")
    
    db.delete(db_article)
    await db.commit()
