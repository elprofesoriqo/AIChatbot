from fastapi import APIRouter, HTTPException
from API.models.request import RecommendationRequest
from API.models.response import RecommendationResponse
from API.utils.chatbot_utils import get_recommendations

router = APIRouter()

@router.post("/recommend", response_model=RecommendationResponse)
async def recommend_products(request: RecommendationRequest):
    try:
        recommendations = get_recommendations(request.preferences)
        return RecommendationResponse(products=recommendations)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Recommendation generation failed")
