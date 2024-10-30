from fastapi import APIRouter, HTTPException
from API.models.request import OrderRequest
from API.models.response import OrderResponse
from API.utils.chatbot_utils import create_order

router = APIRouter()

@router.post("/order", response_model=OrderResponse)
async def place_order(request: OrderRequest):
    try:
        order_confirmation = create_order(request.order_details)
        return OrderResponse(order_id=order_confirmation["order_id"],
                             status="confirmed",
                             details=order_confirmation)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Order processing failed")
