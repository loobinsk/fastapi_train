from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from config.database import Base
from typing import Union, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update
from sqlalchemy import func


class Crud:
    def __init__(self, model: Base):
        self.model = model

    async def create(self, db: AsyncSession, item: dict) -> Base:
        db_item = self.model(**item.dict())
        db.add(db_item)
        await db.commit()
        await db.refresh(db_item)
        return db_item

    # Добавляем метод для получения общего количества записей
    async def get_total_count(self, db: Session):
        count_query = func.count().select().select_from(self.model)
        result = await db.execute(count_query)
        return result.scalar()

    async def get_all(self, db: AsyncSession, scenario_id: int, page: int = 1, page_size: int = 20) -> List[Base]:
        """
        Получает список всех записей с постраничной пагинацией.

        :param db: Сессия базы данных.
        :param page: Номер страницы (по умолчанию 1).
        :param page_size: Количество элементов на странице (по умолчанию 20).

        :return: Список записей для текущей страницы.
        """
        # Вычисляем индексы начала и конца текущей страницы
        start_idx = (page - 1) * page_size
        end_idx = start_idx + page_size

        items_query = select(self.model).filter_by(scenario_id=scenario_id)
        items = await db.execute(items_query)
        items = items.scalars().all()

        # Получаем список элементов для текущей страницы
        current_page_items = items[start_idx:end_idx]

        return current_page_items

    async def get_by_id(self, db: AsyncSession, item_id: int) -> Union[Base, None]:
        try:
            item = await db.execute(select(self.model).filter(self.model.id == item_id))
            return item.scalar_one()
        except NoResultFound:
            return None

    async def update(self, db: AsyncSession, db_item: Base, updates: dict) -> Base:
        for key, value in updates.items():
            setattr(db_item, key, value)
        await db.commit()
        await db.refresh(db_item)
        return db_item

    async def delete(self, db: AsyncSession, db_item: Base):
        db.delete(db_item)
        await db.commit()

    async def copy(self, db: AsyncSession, db_item: Base) -> Base:
        item_copy = self.model(**db_item.__dict__)
        db.add(item_copy)
        await db.commit()
        await db.refresh(item_copy)
        return item_copy

    async def update_put(self, db: AsyncSession, db_item: Base, updates: dict) -> Base:
        for key, value in updates.items():
            setattr(db_item, key, value)
        await db.commit()
        await db.refresh(db_item)
        return db_item
