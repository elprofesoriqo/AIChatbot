from fastapi import APIRouter, HTTPException
from API.models.request import ProductDetailsRequest
from API.models.response import ProductDetailsResponse
from API.utils.chatbot_utils import get_product_details

router = APIRouter()

@router.get("/details/{product_id}", response_model=ProductDetailsResponse)
async def get_product_details(product_id: str):
    try:
        product_details = get_product_details(product_id)
        return ProductDetailsResponse(**product_details)
    except KeyError:
        raise HTTPException(status_code=404, detail="Product not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error fetching product details")
