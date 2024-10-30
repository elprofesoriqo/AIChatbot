# API/models/request.py
from pydantic import BaseModel

class ClassificationRequest(BaseModel):
    message: str

class ProductDetailsRequest(BaseModel):
    product_id: str

class OrderRequest(BaseModel):
    order_details: dict

class RecommendationRequest(BaseModel):
    preferences: dict

# API/models/response.py
from pydantic import BaseModel
from typing import List, Dict

class ClassificationResponse(BaseModel):
    intent: str

class ProductDetailsResponse(BaseModel):
    product_name: str
    price: float
    description: str

class OrderResponse(BaseModel):
    order_id: str
    status: str
    details: dict

class RecommendationResponse(BaseModel):
    products: List[Dict[str, str]]
