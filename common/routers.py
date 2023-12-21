from fastapi import APIRouter, Depends, HTTPException, Query, responses
from sqlalchemy.orm import Session
from typing import List
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
from .crud import Crud
from config.database import get_async_session
from .api import check_author

class NotIsAuthor(BaseModel):
    message: str = "Вы не являетесь автором сценария"

class NotIsAuth(BaseModel):
    message: str = "Неверный токен авторизации"

# Объявляем экземпляр APIKeyHeader
token_header = APIKeyHeader(name="Token")

# Объявляем функцию для создания маршрутов
def create_crud_routes(
    router: APIRouter,
    db_model: BaseModel,  # Модель базы данных SQLAlchemy
    paginated_schema: BaseModel, # Схема получения с постраничной пагинацией
    create_schema: BaseModel,  # Схема создания
    update_schema: BaseModel,  # Схема обновления
    get_schema: BaseModel,  # Схема получения
):
    get_schema = get_schema
    # Получаем verbose_name и verbose_name_plural из модели, если они заданы
    verbose_name = getattr(db_model, "verbose_name", db_model.__name__)
    verbose_name_plural = getattr(db_model, "verbose_name_plural", f"{db_model.__name__}s")

    # Создаем экземпляр CRUD для работы с данными
    crud = Crud(db_model)
    # Создание записи
    @router.post("/", response_model=get_schema, summary=f"Создать {verbose_name}", 
        responses={403: {"model": NotIsAuthor},401: {"model": NotIsAuth}})
    async def create_item(item: create_schema, db: Session = Depends(get_async_session), token: str = Depends(token_header)):
        """
        Создает новую запись.

        :param item: Данные для создания записи.

        :param token: Токен авторизации.

        :return: Созданная запись.
        """
        is_author = await check_author(item.scenario_id, token)

        if is_author == False:
            raise HTTPException(status_code=403, detail="Вы не являетесь автором сценария")
        elif is_author == "Неверный токен авторизации":
            raise HTTPException(status_code=401, detail="Неверный токен авторизации")

        db_item = await crud.create(db, item)
        return get_schema(**db_item.__dict__)

    @router.get("/", response_model=paginated_schema, summary=f"Получить список {verbose_name_plural}",
        responses={401: {"model": NotIsAuth}})
    async def read_items(
        scenario_id: int = Query(description="id Сценария"),
        db: Session = Depends(get_async_session),
        token: str = Depends(token_header),
        page: int = Query(1, description="Номер страницы (по умолчанию 1)"),
        page_size: int = Query(20, description="Количество элементов на странице (по умолчанию 20)"),
    ):
        """
        Получает список записей с постраничной пагинацией.

        :param token: Токен авторизации.

        :param page: Номер страницы.

        :param page_size: Количество элементов на странице.

        :return: Список записей.
        """
        items = await crud.get_all(db, scenario_id=scenario_id, page=page, page_size=page_size)

        # Вычисляем общее количество страниц
        total_pages = (await crud.get_total_count(db)) // page_size + 1

        # Преобразуем текущую страницу в response_model
        response_items = [get_schema(**item.__dict__) for item in items]

        return {
            "items": response_items,
            "total_pages": total_pages,
            "page": page,
            "page_size": page_size,
        }

    # Получение записи по ID
    @router.get("/{item_id}", response_model=get_schema, summary=f"Получить {verbose_name} по ID")
    async def read_item(item_id: int, db: Session = Depends(get_async_session), token: str = Depends(token_header)):
        """
        Получает запись по ее ID.

        :param item_id: ID записи.

        :param token: Токен авторизации.

        :return: Запись с указанным ID.
        """
        db_item = await crud.get_by_id(db, item_id)
        if db_item is None:
            raise HTTPException(status_code=404, detail=f"{verbose_name} не найден")
        return get_schema(**db_item.__dict__)

    # Обновление записи через PATCH
    @router.patch("/{item_id}", response_model=get_schema, summary=f"Обновить {verbose_name} через PATCH")
    async def update_item(item_id: int, item_update: update_schema, db: Session = Depends(get_async_session), token: str = Depends(token_header)):
        """
        Обновляет запись через метод PATCH.

        :param item_id: ID записи для обновления.

        :param item_update: Данные для обновления записи.

        :param token: Токен авторизации.

        :return: Обновленная запись.
        """
        db_item = await crud.get_by_id(db, item_id)
        if db_item is None:
            raise HTTPException(status_code=404, detail=f"{verbose_name} не найден")
        updated_item = await crud.update(db, db_item, item_update)
        return get_schema(**updated_item.__dict__)

    # Обновление записи через PUT
    @router.put("/{item_id}", response_model=get_schema, summary=f"Обновить {verbose_name} через PUT")
    async def put_item(item_id: int, item_update: create_schema, db: Session = Depends(get_async_session), token: str = Depends(token_header)):
        """
        Обновляет запись через метод PUT.

        :param item_id: ID записи для обновления.

        :param item_update: Данные для обновления записи.

        :param token: Токен авторизации.

        :return: Обновленная запись.
        """
        db_item = await crud.get_by_id(db, item_id)
        if db_item is None:
            raise HTTPException(status_code=404, detail=f"{verbose_name} не найден")
        updated_item = await crud.put(db, db_item, item_update)
        return get_schema(**updated_item.__dict__)

    # Удаление записи
    @router.delete("/{item_id}", response_model=get_schema, summary=f"Удалить {verbose_name}")
    async def delete_item(item_id: int, db: Session = Depends(get_async_session), token: str = Depends(token_header)):
        """
        Удаляет запись.

        :param item_id: ID записи для удаления.

        :param token: Токен авторизации.

        :return: Удаленная запись.
        """
        db_item = await crud.get_by_id(db, item_id)
        if db_item is None:
            raise HTTPException(status_code=404, detail=f"{verbose_name} не найден")
        await crud.delete(db, db_item)
        return get_schema(**db_item.__dict__)

    # Копирование записи
    @router.post("/copy/{item_id}", response_model=get_schema, summary=f"Копировать {verbose_name}")
    async def copy_item(item_id: int, db: Session = Depends(get_async_session), token: str = Depends(token_header)):
        """
        Копирует запись с указанным ID.

        :param item_id: ID записи для копирования.

        :param token: Токен авторизации.

        :return: Созданная копия записи.
        """
        db_item = await crud.get_by_id(db, item_id)
        if db_item is None:
            raise HTTPException(status_code=404, detail=f"{verbose_name} не найден")

        copied_item = await crud.copy(db, db_item)
        return get_schema(**copied_item.__dict__)

    return router
