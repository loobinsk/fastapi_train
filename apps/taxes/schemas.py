from .models import Tax
from common.schemas import generate_schema
from pydantic import BaseModel
from typing import List


class TaxCreate(generate_schema(Tax, exclude='id')):
    pass

class TaxUpdate(generate_schema(Tax, exclude='id')):
    pass

class Tax(generate_schema(Tax)):
    pass

class TaxPaginatedResponse(BaseModel):
    items: List[Tax]
    total_pages: int
    page: int
    page_size: int   
