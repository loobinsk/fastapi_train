from fastapi import APIRouter
from common.routers import create_crud_routes
from . import models
from . import schemas


capex_router = APIRouter()
generate_routers = create_crud_routes(
                        capex_router, models.Capex, 
                        schemas.CapexPaginatedResponse,
                        schemas.CapexCreate, 
                        schemas.CapexUpdate, 
                        schemas.Capex)
