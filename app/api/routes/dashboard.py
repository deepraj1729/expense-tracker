from fastapi import APIRouter
from models.model import ResponseBody
from entity.transaction import Transaction


# API Instance
dashboard_router = APIRouter()


######################################################################################
# Overview & Analysis
######################################################################################


@dashboard_router.get("/dashboard/")
async def getDashboard(year:str=None,month:str=None):
    entity = Transaction()
    data = entity.getDashboard(month=month,year=year)
    del entity

    return ResponseBody(
        status="200 ok",
        message=data["message"],
        data=data
    )