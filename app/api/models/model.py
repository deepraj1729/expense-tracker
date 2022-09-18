from pydantic import BaseModel

class TransactionModel(BaseModel):
    id:str                      #Transaction ID
    trans_date:str              #Transaction Date
    trans_month:str             #Transaction Month
    trans_year: str             #Transaction Year
    trans_amount:float          #Transaction Amount
    trans_type:str              #Debit or Credit
    trans_tag:str               #Expense,Investment,Savings
    trans_remarks:str           #Swiggy,Zomato etc


class TransactionRequestBody(BaseModel):
    trans_date:str
    trans_month:str             #Transaction Month
    trans_year: str             #Transaction Year
    trans_amount: str
    trans_type: str
    trans_tag: str
    trans_remarks: str


class RequestBody(TransactionModel):
    pass


class ResponseBody(BaseModel):
    status:str
    message:str
    data:dict