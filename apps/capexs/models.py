from sqlalchemy import Column, Integer, String, Float, Boolean, Date
from sqlalchemy.orm import validates
from config.database import Base

class Capex(Base):
    __tablename__ = 'capex'

    id = Column(Integer, primary_key=True, index=True, info={'verbose_name': 'Идентификатор'})
    scenario_id = Column(Integer, nullable=False, index=True, info={'verbose_name': 'Сценарий'})
    
    date = Column(Date, nullable=False, info={'verbose_name': 'Дата'})
    name = Column(String, nullable=False, info={'verbose_name': 'Название'})
    amount = Column(Float, nullable=False, info={'verbose_name': 'Сумма'})
    vat_rate = Column(Float, nullable=False, info={'verbose_name': 'НДС'})
    depreciation_period = Column(Integer, nullable=False, info={'verbose_name': 'Период амортизации'})
    is_leasing = Column(Boolean, nullable=False, info={'verbose_name': 'Лизинг'})
    description = Column(String, nullable=False, info={'verbose_name': 'Описание'})

    @validates('amount')
    def validate_amount(self, key, value):
        if value < 0:
            raise ValueError("Сумма не может быть отрицательной.")
        return value

    @validates('vat_rate')
    def validate_vat_rate(self, key, value):
        if value < 0 or value > 100:
            raise ValueError("НДС должен быть в пределах от 0 до 1.")
        return value