from fastapi import APIRouter,Depends
from models.model import ResponseBody
from entity.transaction import Transaction
from middlewares.jwt import oauth2_scheme,decodeJWT


# API Instance
dashboard_router = APIRouter()


######################################################################################
# Dashboard
######################################################################################

@dashboard_router.get("/dashboard")
async def getDashboard(year:str=None,month:str=None,token: str = Depends(oauth2_scheme)):
    print("Token: ",token)
    print("Decoded JWT: {}".format(decodeJWT(token)))
    entity = Transaction()
    data = entity.getDashboard(month=month,year=year)
    del entity

    return ResponseBody(
        status="200 ok",
        message=data["message"],
        data=data
    )