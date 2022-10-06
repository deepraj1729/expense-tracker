from fastapi import APIRouter,Depends
from models.model import ResponseBody,TransactionRequestBody
from entity.transaction import Transaction
from middlewares.jwt import oauth2_scheme


# API Instance
profile_router = APIRouter()