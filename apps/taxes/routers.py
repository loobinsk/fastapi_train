from fastapi import APIRouter
from common.routers import create_crud_routes
from . import models
from . import schemas

taxes_router = APIRouter()
generate_own_fund_routers = create_crud_routes(taxes_router, models.Tax, schemas.TaxPaginatedResponse,
    schemas.TaxCreate, schemas.TaxUpdate, schemas.Tax)

