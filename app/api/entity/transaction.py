from controller.transaction import TransactionController
from models.model import TransactionRequestBody
from utils.migration import modifyData
from config.db import transaction_collection
from schemas.schema import TransSchema
from bson import ObjectId


class Transaction:
    def __init__(self):
        #dependency
        self.collection = transaction_collection
        self.controller = TransactionController()

        #Fields
        self._id = None
        self.trans_date = None
        self.trans_month = None
        self.trans_year = None
        self.trans_amount = None
        self.trans_type = None
        self.trans_tag = None
        self.trans_remarks = None

    def getByID(self,id:str):
        return TransSchema(self.collection.find({"_id":ObjectId(id)}))
    
    def getDashboard(self,month:str,year:str):
        if year is None and  month is not None:
            return {
                "status":"failure",
                "message":"Pass year as query params"
                }
        
        elif year is None and month is None:
            #Overall Transactions
            all_transactions = self.getAll()
            return self.controller.getOverallDashboard(transaction_list=all_transactions)

        elif month is None:
            #Yearly Transactions
            yearly_transactions = TransSchema(self.collection.find({"trans_year":year}))
            return self.controller.getYearlyDashboard(year=year,transaction_list=yearly_transactions)

        else:
            #Monthly Transactions
            monthly_transactions = TransSchema(self.collection.find({"trans_month":month,"trans_year":year}))
            return self.controller.getMonthlyDashboard(month=month,year=year,transaction_list=monthly_transactions)


    def getAll(self):
        return TransSchema(self.collection.find())

    def getAllByMonth(self,month:str):
        return TransSchema(self.collection.find({"trans_month":month}))

    def addOne(self,transaction:TransactionRequestBody):
        modified_transaction = modifyData(transaction)  #Adds month and year field
        transaction_id = self.collection.insert_one(modified_transaction).inserted_id
        return transaction_id

    def addMany(self,transactions:dict):
        self.collection.insert_many(transactions)

    def deleteByID(self,id:str):
        query = self.collection.delete_one({"_id":ObjectId(id)})
        if query.deleted_count == 1:
            return "success"
        return "failure"

    def dropCollection(self):
        transaction_collection.drop()

    def __del__(self):
        print("Deleted object")