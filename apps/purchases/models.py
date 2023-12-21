from sqlalchemy import Column, Integer, String, Float, Boolean, Date, CheckConstraint
from config.database import Base

class Purchase(Base):
    __tablename__ = 'purchases'

    id = Column(Integer, primary_key=True, info={'verbose_name': 'Идентификатор'})
    scenario_id = Column(Integer, nullable=False, index=True, info={'verbose_name': 'Сценарий'})
    
    month = Column(Integer, CheckConstraint('month >= 1 AND month <= 12'), info={'verbose_name': 'Месяц'})
    year = Column(Integer, CheckConstraint('year >= 1900 AND year <= 3000'), info={'verbose_name': 'Год'})
    tmc = Column(Float, CheckConstraint('tmc >= 0'), info={'verbose_name': 'ТМЦ'})
    customer_advances = Column(Float, CheckConstraint('customer_advances >= 0'), info={'verbose_name': 'Авансы от клиентов'})
    customer_accounts_receivable = Column(Float, CheckConstraint('customer_accounts_receivable >= 0'), info={'verbose_name': 'Дебиторская задолженность клиентов'})
    supplier_advances = Column(Float, CheckConstraint('supplier_advances >= 0'), info={'verbose_name': 'Авансы поставщикам'})
    supplier_accounts_payable = Column(Float, CheckConstraint('supplier_accounts_payable >= 0'), info={'verbose_name': 'Кредиторская задолженность поставщикам'})
    vat_balance_on_purchased_assets = Column(Float, CheckConstraint('vat_balance_on_purchased_assets >= 0'), info={'verbose_name': 'НДС по приобретенным активам'})
