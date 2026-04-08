from fastapi import APIRouter

from app.api.v1 import auth, categories, expenses, policies, receipts, reports

api_router = APIRouter()

api_router.include_router(auth.router)
api_router.include_router(expenses.router)
api_router.include_router(receipts.router)
api_router.include_router(categories.router)
api_router.include_router(reports.router)
api_router.include_router(policies.router)
