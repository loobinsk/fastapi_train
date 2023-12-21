from fastapi import APIRouter
from common.routers import create_crud_routes
from . import models
from . import schemas

expense_router = APIRouter()
generate_routers = create_crud_routes(expense_router, models.Expense, schemas.ExpensePaginatedResponse, schemas.ExpenseCreate, schemas.ExpenseUpdate, schemas.Expense)
