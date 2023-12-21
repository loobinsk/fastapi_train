from .models import Sale
from common.schemas import generate_schema
from pydantic import BaseModel
from typing import List


class SaleCreate(generate_schema(Sale, exclude='id')):
    pass

class SaleUpdate(generate_schema(Sale, exclude='id')):
    pass

class Sale(generate_schema(Sale)):
    pass

class SalePaginatedResponse(BaseModel):
    items: List[Sale]
    total_pages: int
    page: int
    page_size: int   
