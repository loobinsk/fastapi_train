from .models import Capex as CapexDB
from common.schemas import generate_schema
from pydantic import BaseModel
from typing import List


class CapexCreate(generate_schema(CapexDB, exclude='id')):
    pass

class CapexUpdate(generate_schema(CapexDB, exclude='id')):
    pass

class Capex(generate_schema(CapexDB)):
    pass 

class CapexPaginatedResponse(BaseModel):
    items: List[Capex]
    total_pages: int
    page: int
    page_size: int