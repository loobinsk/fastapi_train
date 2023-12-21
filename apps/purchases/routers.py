from fastapi import APIRouter
from common.routers import create_crud_routes
from . import models
from . import schemas

purchase_router = APIRouter()
generate_own_fund_routers = create_crud_routes(purchase_router, models.Purchase, schemas.PurchasePaginatedResponse,
    schemas.PurchaseCreate, schemas.PurchaseUpdate, schemas.Purchase)

