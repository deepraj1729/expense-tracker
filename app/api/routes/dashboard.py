from fastapi import APIRouter
from models.model import ResponseBody
from entity.transaction import Transaction
from config.db import DB_CONN_URL


# API Instance
dashboard_router = APIRouter()


######################################################################################
# Overview & Analysis
######################################################################################

@dashboard_router.get("/dashboard/all")
async def getOverallDashboard():
    return ResponseBody(
        status="200 ok",
        message="Overall Dashbaord",
        data={"db_url":DB_CONN_URL,"net_expense":120000,"net_invested":135000,"net_savings":65000}
    )



@dashboard_router.get("/dashboard/{month}")
async def getAnalysis(month:str):
    entity = Transaction()
    data = entity.getDashboardByMonth(month)

    return ResponseBody(
        status="200 ok",
        message="All the transactions",
        data=data
    )
