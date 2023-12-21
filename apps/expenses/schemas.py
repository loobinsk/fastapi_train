from .models import Expense
from common.schemas import generate_schema
from pydantic import BaseModel
from typing import List


class ExpenseCreate(generate_schema(Expense, exclude='id')):
    pass

class ExpenseUpdate(generate_schema(Expense, exclude='id')):
    pass

class Expense(generate_schema(Expense)):
    pass

class ExpensePaginatedResponse(BaseModel):
    items: List[Expense]
    total_pages: int
    page: int
    page_size: int