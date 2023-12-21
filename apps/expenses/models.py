from sqlalchemy import Column, Text, Integer, String, Float, Boolean, Date
from config.database import Base


class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True, index=True, info={'verbose_name': 'Идентификатор'})
    scenario_id = Column(Integer, nullable=False, index=True, info={'verbose_name': 'Сценарий'})
    
    date = Column(Date, nullable=False, info={'verbose_name': 'Дата'})
    name = Column(String, nullable=False, info={'verbose_name': 'Название'})
    classification = Column(Text, info={'verbose_name': 'Классификация'})
    activity_classification = Column(Text, info={'verbose_name': 'Классификация деятельности'})
    amount = Column(Float, nullable=False, info={'verbose_name': 'Сумма'})
    vat_rate = Column(Float, nullable=False, info={'verbose_name': 'НДС'})
    description = Column(String, nullable=False, info={'verbose_name': 'Описание'})
