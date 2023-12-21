from .models import OwnFund, Credit, Leasing
from common.schemas import generate_schema
from pydantic import BaseModel
from typing import List


class OwnFundCreate(generate_schema(OwnFund, exclude='id')):
    pass

class OwnFundUpdate(generate_schema(OwnFund, exclude='id')):
    pass

class OwnFund(generate_schema(OwnFund)):
    pass

class OwnFundPaginatedResponse(BaseModel):
    items: List[OwnFund]
    total_pages: int
    page: int
    page_size: int    

class CreditCreate(generate_schema(Credit, exclude='id')):
    pass

class CreditUpdate(generate_schema(Credit, exclude='id')):
    pass

class Credit(generate_schema(Credit)):
    pass

class CreditPaginatedResponse(BaseModel):
    items: List[Credit]
    total_pages: int
    page: int
    page_size: int    

class LeasingCreate(generate_schema(Leasing, exclude='id')):
    pass

class LeasingUpdate(generate_schema(Leasing, exclude='id')):
    pass

class Leasing(generate_schema(Leasing)):
    pass

class LeasingPaginatedResponse(BaseModel):
    items: List[Leasing]
    total_pages: int
    page: int
    page_size: int    