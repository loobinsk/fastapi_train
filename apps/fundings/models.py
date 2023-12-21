from sqlalchemy import Column, Integer, String, Float, Boolean, Date, Numeric, Text
from config.database import Base

class OwnFund(Base):
    __tablename__ = 'own_funds'

    id = Column(Integer, primary_key=True, info={'verbose_name': 'Идентификатор'})
    scenario_id = Column(Integer, nullable=False, index=True, info={'verbose_name': 'Сценарий'})

    date = Column(Date, info={'verbose_name': 'Дата'})
    name = Column(String(255), info={'verbose_name': 'Название'})
    amount = Column(Numeric(10, 2), info={'verbose_name': 'Сумма'})
    investor = Column(String(255), info={'verbose_name': 'Инвестор'})
    description = Column(Text, info={'verbose_name': 'Описание'})

class Credit(Base):
    __tablename__ = 'credits'

    id = Column(Integer, primary_key=True, info={'verbose_name': 'Идентификатор'})
    scenario_id = Column(Integer, nullable=False, index=True, info={'verbose_name': 'Сценарий'})

    date = Column(Date, info={'verbose_name': 'Дата'})
    name = Column(String(255), info={'verbose_name': 'Название'})
    bank = Column(String(255), info={'verbose_name': 'Банк'})
    amount = Column(Numeric(10, 2), info={'verbose_name': 'Сумма'})
    payment_type = Column(String(100), info={'verbose_name': 'Тип платежа'})  # Изменено на String(100)
    description = Column(Text, info={'verbose_name': 'Описание'})

class Leasing(Base):
    __tablename__ = 'leasings'

    id = Column(Integer, primary_key=True, info={'verbose_name': 'Идентификатор'})
    scenario_id = Column(Integer, nullable=False, index=True, info={'verbose_name': 'Сценарий'})
    
    date = Column(Date, info={'verbose_name': 'Дата'})
    name = Column(String(255), info={'verbose_name': 'Название'})
    leasing_id = Column(String(100), info={'verbose_name': 'Идентификатор лизинга'})  # Изменено на String(100)
    lessor = Column(String(255), info={'verbose_name': 'Лизингодатель'})
    amount = Column(Numeric(10, 2), info={'verbose_name': 'Сумма'})
    vat_rate = Column(Float, info={'verbose_name': 'НДС'})
    payment_type = Column(String(100), info={'verbose_name': 'Тип платежа'})  # Изменено на String(100)
    description = Column(Text, info={'verbose_name': 'Описание'})
