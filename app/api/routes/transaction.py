from fastapi import APIRouter,Request,Depends
from models.model import ResponseBody,TransactionRequestBody
from entity.transaction import Transaction
from utils.migration import loadFile,OUT_FILE_PATH
from middlewares.jwt import oauth2_scheme


# API Instance
transaction_router = APIRouter()


######################################################################################
# Transactions
######################################################################################

#Get All Transactions
@transaction_router.get("/transaction/all")
async def getAllTransactions(token: str = Depends(oauth2_scheme)):
    try:
        entity = Transaction()
        transactions = entity.getAll()
        del entity

        return ResponseBody(
            status="200 ok",
            message="All the transactions",
            data={"transactions":transactions}
        )

    except Exception as e:
        return ResponseBody(
            status = "400 failure",
            message = "error",
            data = {"error":f"{e}"}
        )



#Get Transaction by id
@transaction_router.get("/transaction/{id}")
async def getTransaction(id:str,token: str = Depends(oauth2_scheme)):
    entity = Transaction()
    transaction = entity.getByID(id)
    del entity

    return ResponseBody(
        status="200 ok",
        message="Transaction found",
        data={"transaction":transaction}
    )



#Add Transaction
@transaction_router.post("/transaction/add")
async def addTransaction(content:TransactionRequestBody,request:Request,response_model=ResponseBody,token: str = Depends(oauth2_scheme)):
    try:
        entity = Transaction()
        transaction_id = entity.addOne(content.dict())
        del entity

        return ResponseBody(
            status = "200 ok",
            message = "Added transaction successfully",
            data = {
                "msg":"success",
                "transaction_id":str(transaction_id)
            }
        )

    except Exception as e:
        return ResponseBody(
            status = "400 failure",
            message = "error",
            data = {"error":f"{e}"}
        )



#Add multiple transactions 
@transaction_router.post("/transaction/add_many")
async def addMultipleTransaction(response_model=ResponseBody,token: str = Depends(oauth2_scheme)):
    try:
        entity = Transaction()
        trans_data = loadFile(OUT_FILE_PATH)
        all_transactions = trans_data["transactions"]
        entity.addMany(all_transactions)

        return ResponseBody(
            status = "200 ok",
            message = "Added multiple transactions successfully",
            data = {
                "msg":"success"
            }
        )

    except Exception as e:
        return ResponseBody(
            status = "400 failure",
            message = "error",
            data = {"error":f"{e}"}
        )

#Get Transactions for a month
@transaction_router.get("/transactions/{month}")
async def getMonthlyTransactions(month:str,token: str = Depends(oauth2_scheme)):
    entity = Transaction()
    transactions = entity.getAllByMonth(month)
    del entity

    return ResponseBody(
        status="200 ok",
        message=f"All the transactions for month: {month}",
        data={"transactions":transactions}
    )



#Delete Trnasaction
@transaction_router.delete("/transaction/{id}")
async def deleteTransaction(id:str,token: str = Depends(oauth2_scheme)):
    entity = Transaction()
    status = entity.deleteByID(id)
    del entity

    if status == "success":
        return ResponseBody(
            status="200 ok",
            message=f"Deleted transaction successfully",
            data={"transaction_id":id}
        )
    
    else:
        return ResponseBody(
            status = "400 failure",
            message = "error",
            data = {"error":"Something went wrong!!!"}
        )


#Delete collection (overall transactions)
@transaction_router.delete("/transactions")
async def deleteAllTransactions(token: str = Depends(oauth2_scheme)):
    entity = Transaction()
    entity.dropCollection()
    del entity

    return ResponseBody(
        status="200 ok",
        message=f"Dropped Collection Successfully",
        data = {"msg":"Dropped Collection Successfully"}
    )