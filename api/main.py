from fastapi import FastAPI
from endpoints import classification, details, order, recommendation

app = FastAPI()

app.include_router(classification.router, prefix="/api/classification", tags=["Classification"])
app.include_router(details.router, prefix="/api/details", tags=["Product Details"])
app.include_router(order.router, prefix="/api/order", tags=["Order Management"])
app.include_router(recommendation.router, prefix="/api/recommendation", tags=["Product Recommendation"])
