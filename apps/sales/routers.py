from fastapi import APIRouter
from common.routers import create_crud_routes
from . import models
from . import schemas

sales_router = APIRouter()
generate_own_fund_routers = create_crud_routes(sales_router, models.Sale, schemas.SalePaginatedResponse,
    schemas.SaleCreate, schemas.SaleUpdate, schemas.Sale)

