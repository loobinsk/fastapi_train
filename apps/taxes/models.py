from sqlalchemy import Column, Integer, String, Float, Date
from config.database import Base

class Tax(Base):
    __tablename__ = 'taxes'

    TAX_CHOICES = [
        ("profit_tax", "Налог на прибыль"),
        ("vat", "НДС"),
        ("refundable_vat", "НДС возмещенный"),
        ("usn", "УСН"),
        ("eshn", "ЕСХН"),
        ("patent", "Патент"),
    ]
    
    id = Column(Integer, primary_key=True, index=True, info={'verbose_name': 'Идентификатор'})
    scenario_id = Column(Integer, nullable=False, index=True, info={'verbose_name': 'Сценарий'})
    
    date = Column(Date, nullable=False, info={'verbose_name': 'Дата'})
    type = Column(String(100), nullable=False, info={'verbose_name': 'Тип налога'})  # Изменено на String(100)
    name = Column(String, nullable=False, info={'verbose_name': 'Название'})
    amount = Column(Float, nullable=False, info={'verbose_name': 'Сумма'})
    description = Column(String, nullable=False, info={'verbose_name': 'Описание'})
