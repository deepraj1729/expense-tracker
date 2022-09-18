from models.model import TransactionRequestBody
from config.db import transaction_collection
from schemas.schema import TransSchema
from bson import ObjectId


class Transaction:
    def __init__(self):
        #dependency
        self.collection = transaction_collection

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


    def getAll(self):
        return TransSchema(self.collection.find())

    def getAllByMonth(self,month:str):
        return TransSchema(self.collection.find({"trans_month":month}))

    def addOne(self,transaction:TransactionRequestBody):
        transaction_id = self.collection.insert_one(transaction).inserted_id
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