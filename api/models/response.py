from pydantic import BaseModel
from typing import List, Dict, Optional

class ClassificationResponse(BaseModel):
    intent: str

class ProductDetailsResponse(BaseModel):
    product_name: str
    price: float
    description: str

class OrderResponse(BaseModel):
    order_id: str
    status: str
    details: Dict[str, str]

class RecommendationResponse(BaseModel):
    products: List[Dict[str, str]]

class ErrorResponse(BaseModel):
    error: str
    message: str
