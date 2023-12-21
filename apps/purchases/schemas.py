from .models import Purchase
from common.schemas import generate_schema
from pydantic import BaseModel
from typing import List

class PurchaseCreate(generate_schema(Purchase, exclude='id')):
    pass

class PurchaseUpdate(generate_schema(Purchase, exclude='id')):
    pass

class Purchase(generate_schema(Purchase)):
    pass

class PurchasePaginatedResponse(BaseModel):
    items: List[Purchase]
    total_pages: int
    page: int
    page_size: int   