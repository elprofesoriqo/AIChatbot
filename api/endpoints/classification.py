from fastapi import APIRouter, HTTPException
from API.models.request import ClassificationRequest
from API.models.response import ClassificationResponse
from API.utils.chatbot_utils import get_classification

router = APIRouter()

@router.post("/classify", response_model=ClassificationResponse)
async def classify_intent(request: ClassificationRequest):
    try:
        intent = get_classification(request.message)
        return ClassificationResponse(intent=intent)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Classification failed")
