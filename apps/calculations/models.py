from sqlalchemy import create_engine, Column, Integer, String, Numeric, Float, Date
from sqlalchemy.orm import validates
from config.database import Base


class SalesPlan(Base):
    __tablename__ = 'sales_plan'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False, info={'verbose_name': 'Дата'})
    scenario_id = Column(Integer, nullable=False, index=True, info={'verbose_name': 'Сценарий'})

    product_name = Column(String, nullable=False, info={'verbose_name': 'Название продукта'})
    price = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Цена'})
    volume = Column(Integer, nullable=False, info={'verbose_name': 'Объем'})
    revenue_with_vat = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Выручка с НДС'})
    vat = Column(Numeric(precision=5, scale=2), nullable=False, info={'verbose_name': 'НДС'})

    @property
    def revenue_without_vat(self):
        return self.revenue_with_vat / (1 + self.vat)

class ProfitLossPlan(Base):
    __tablename__ = 'profit_loss_plan'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False, info={'verbose_name': 'Дата'})
    scenario_id = Column(Integer, nullable=False, index=True, info={'verbose_name': 'Сценарий'})

    revenue = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Выручка'})
    cost_of_goods_sold = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Себестоимость'})
    gross_profit = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Валовая прибыль'})
    operating_expenses = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Коммерческие расходы'})
    management_expenses = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Управленческие расходы'})
    ebit = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Операционная прибыль EBIT'})
    interest_expenses = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Процентные расходы'})
    profit_before_tax = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Прибыль до налогообложения'})
    income_tax = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Налог на прибыль'})
    net_profit = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Чистая прибыль'})
    ebitda = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'EBITDA'})

class CashFlowPlan(Base):
    __tablename__ = 'cash_flow_plan'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False, info={'verbose_name': 'Дата'})
    scenario_id = Column(Integer, nullable=False, index=True, info={'verbose_name': 'Сценарий'})

    working_capital_change = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Изменение рабочего капитала'})
    income_tax = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Налог на прибыль'})
    operating_cash_flow = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Чистый денежный поток от операционной деятельности'})
    vat_refund = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Возмещение НДС'})
    capital_expense_payment = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Оплата капитальных расходов'})
    liquidation_expense_payment = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Оплата ликвидационных расходов'})
    liquidation_income_payment = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Оплата ликвидационных доходов'})
    investment_cash_flow = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Чистый денежный поток от инвестиционной деятельности'})
    owner_contribution = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Поступление от собственников'})
    loan_receipt = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Поступление кредита'})
    loan_repayment = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Возврат кредитов'})
    interest_payment = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Оплата процентов'})
    financing_cash_flow = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Чистый денежный поток от финансовой деятельности'})
    net_cash_flow = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Чистый денежный поток'})
    beginning_cash_balance = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Остаток денежных средств на начало периода'})
    ending_cash_balance = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Остаток денежных средств на конец периода'})

class BalanceSheet(Base):
    __tablename__ = 'balance_sheet'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False, info={'verbose_name': 'Дата'})
    scenario_id = Column(Integer, nullable=False, index=True, info={'verbose_name': 'Сценарий'})
    
    # Активы
    fixed_assets = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Основные средства'})
    total_non_current_assets = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Итого внеоборотные активы'})
    inventories = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Запасы'})
    vat_on_purchases = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'НДС по приобретенным ценностям'})
    accounts_receivable = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Дебиторская задолженность'})
    cash = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Денежные средства'})
    total_current_assets = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Итого оборотные активы'})
    total_assets = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Итого баланс (активы)'})
    
    # Капитал и обязательства
    share_capital = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Уставный капитал'})
    retained_earnings = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Нераспределенная прибыль'})
    total_equity = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Итого собственный капитал'})
    borrowed_funds = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Заемные средства'})
    accounts_payable = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Кредиторская задолженность'})
    total_liabilities = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Итого обязательства'})
    total_liabilities_and_equity = Column(Numeric(precision=10, scale=2), nullable=False, info={'verbose_name': 'Итого баланс (обязательства и собственный капитал)'})

class FinancialRatios(Base):
    __tablename__ = 'financial_ratios'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False, info={'verbose_name': 'Дата'})
    scenario_id = Column(Integer, nullable=False, index=True, info={'verbose_name': 'Сценарий'})

    ros = Column(Float, nullable=True, info={'verbose_name': 'Рентабельность продаж (ROS)'})
    roe = Column(Float, nullable=True, info={'verbose_name': 'Рентабельность собственного капитала (ROE)'})
    roa = Column(Float, nullable=True, info={'verbose_name': 'Рентабельность активов (ROA)'})
    asset_turnover = Column(Float, nullable=True, info={'verbose_name': 'Коэффициент оборачиваемости активов'})
    current_assets_turnover = Column(Float, nullable=True, info={'verbose_name': 'Коэффициент оборачиваемости оборотных активов'})
    inventory_turnover = Column(Float, nullable=True, info={'verbose_name': 'Коэффициент оборачиваемости запасов'})
    accounts_receivable_turnover = Column(Float, nullable=True, info={'verbose_name': 'Коэффициент оборачиваемости дебиторской задолженности'})
    accounts_payable_turnover = Column(Float, nullable=True, info={'verbose_name': 'Коэффициент оборачиваемости кредиторской задолженности'})
    autonomy = Column(Float, nullable=True, info={'verbose_name': 'Коэффициент автономии'})
    leverage_de = Column(Float, nullable=True, info={'verbose_name': 'Коэффициент левериджа (D/E)'})
    own_working_capital = Column(Float, nullable=True, info={'verbose_name': 'Собственный оборотный капитал'})
    absolute_liquidity = Column(Float, nullable=True, info={'verbose_name': 'Абсолютная ликвидность'})
    interim_liquidity = Column(Float, nullable=True, info={'verbose_name': 'Промежуточная ликвидность'})
    current_liquidity = Column(Float, nullable=True, info={'verbose_name': 'Текущая ликвидность'})

class ProjectDetails(Base):
    __tablename__ = 'project_details'

    id = Column(Integer, primary_key=True)
    scenario_id = Column(Integer, nullable=False, index=True, info={'verbose_name': 'Сценарий'})

    start_date = Column(Date, nullable=False, info={'verbose_name': 'Начало проекта'})
    end_date = Column(Date, nullable=False, info={'verbose_name': 'Окончание проекта'})
    project_rating = Column(Float, nullable=True, info={'verbose_name': 'Рейтинг проекта'})
    capex_with_vat = Column(Float, nullable=True, info={'verbose_name': 'Сумма CapEx (с НДС)'})
    own_funds = Column(Float, nullable=True, info={'verbose_name': 'Сумма собственных средств'})
    borrowed_funds = Column(Float, nullable=True, info={'verbose_name': 'Сумма заемных средств'})
    debt_to_equity_ratio = Column(Float, nullable=True, info={'verbose_name': 'Коэффициент D/E'})
    average_debt_to_ebitda_ratio = Column(Float, nullable=True, info={'verbose_name': 'Средний коэффициент Debt/EBITDA'})
    annual_revenue_excluding_vat = Column(Float, nullable=True, info={'verbose_name': 'Среднегодовая выручка (без НДС)'})
    annual_operating_expenses = Column(Float, nullable=True, info={'verbose_name': 'Среднегодовые операционные затраты с амортизацией (без НДС)'})
    annual_net_profit = Column(Float, nullable=True, info={'verbose_name': 'Среднегодовая чистая прибыль'})
    average_sales_profitability = Column(Float, nullable=True, info={'verbose_name': 'Средняя рентабельность продаж'})
    annual_vat = Column(Float, nullable=True, info={'verbose_name': 'Среднегодовой НДС'})
    annual_income_tax = Column(Float, nullable=True, info={'verbose_name': 'Среднегодовой налог на прибыль'})
    discount_rate = Column(Float, nullable=True, info={'verbose_name': 'Ставка дисконтирования'})
    refinancing_rate = Column(Float, nullable=True, info={'verbose_name': 'Ставка рефинансирования'})
    net_present_value = Column(Float, nullable=True, info={'verbose_name': 'Чистая приведенная стоимость NPV'})
    profitability_index = Column(Float, nullable=True, info={'verbose_name': 'Индекс рентабельности PI'})
    internal_rate_of_return = Column(Float, nullable=True, info={'verbose_name': 'Внутренняя норма доходности IRR'})
    modified_internal_rate_of_return = Column(Float, nullable=True, info={'verbose_name': 'Модифицированная внутренняя норма доходности MIRR'})
    nominal_payback_period = Column(Float, nullable=True, info={'verbose_name': 'Номинальный срок окупаемости'})
    discounted_payback_period = Column(Float, nullable=True, info={'verbose_name': 'Дисконтированный срок окупаемости'})

    @property
    def project_duration(self):
        return (self.end_date - self.start_date).days / 30

    @property
    def total_financing(self):
        return self.own_funds + self.borrowed_funds