from fastapi import APIRouter
from common.routers import create_crud_routes
from . import models
from . import schemas

own_fund_router = APIRouter()
generate_own_fund_routers = create_crud_routes(own_fund_router, models.OwnFund, schemas.OwnFundPaginatedResponse,
    schemas.OwnFundCreate, schemas.OwnFundUpdate, schemas.OwnFund)

credit_router = APIRouter()
generate_own_fund_routers = create_crud_routes(credit_router, models.Credit, schemas.CreditPaginatedResponse,
    schemas.CreditCreate, schemas.CreditUpdate, schemas.Credit)

leasing_router = APIRouter()
generate_own_fund_routers = create_crud_routes(leasing_router, models.Leasing, schemas.LeasingPaginatedResponse,
    schemas.LeasingCreate, schemas.LeasingUpdate, schemas.Leasing)


