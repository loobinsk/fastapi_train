from fastapi import FastAPI, APIRouter
from apps.api.projects import router as project_api_router
from apps.capexs.routers import capex_router
from apps.expenses.routers import expense_router
from apps.fundings.routers import own_fund_router, credit_router, leasing_router
from apps.purchases.routers import purchase_router
from apps.sales.routers import sales_router
from apps.taxes.routers import taxes_router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="API Мониторинга",
    description="CRUD операции для капиталов, лизингов, расходов и других финансовых объектов.",
    version="1.0.0",
)
app.include_router(project_api_router, prefix="/api", tags=["Апи"])
app.include_router(capex_router, prefix="/capexs", tags=["Капексы"])
app.include_router(expense_router, prefix="/expenses", tags=["Расходы"])
app.include_router(own_fund_router, prefix="/own_funds", tags=["Собственные средства"])
app.include_router(credit_router, prefix="/credits", tags=["Кредиты"])
app.include_router(leasing_router, prefix="/leasings", tags=["Лизинги"])
app.include_router(purchase_router, prefix="/purchases", tags=["Закупки (рабочий капитал)"])
app.include_router(sales_router, prefix="/sales", tags=["Продажи"])
app.include_router(taxes_router, prefix="/taxes", tags=["Налоги"])

apps_folder = 'apps'

