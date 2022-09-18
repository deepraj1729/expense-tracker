from models.model import TransactionRequestBody
from utils.migration import modifyData

class TransactionController:
    def __init__(self):
        #Set the initial values
        self.netEarnings = 0
        self.netExpenses = 0
        self.netInvested = 0
        self.netSavings = 0

    def getTransactionData(self,month,transactionList:list):
        if len(transactionList) == 0:
            return ({
                "month":month,
                "dashboard":{
                    "earnings": self.netEarnings,
                    "expenses": self.netExpenses,
                    "investments": self.netInvested,
                    "savings": self.netSavings
                    },
                "transactions":[]
            })

        for transaction in transactionList:
            amt = float(transaction["amount"])
            # Earnings
            if transaction["tag"] == "savings" and transaction["type"] == "credit":
                self.netEarnings+=amt

            # Debit Expenses (actual expenses)
            elif transaction["tag"] == "expense" and transaction["type"] == "debit":
                self.netExpenses+=amt

            # Credit Expenses (e.g. refunds,offers,cashback)
            elif transaction["tag"] == "expense" and transaction["type"] == "credit":
                self.netExpenses-=amt

            # Debit Investments (e.g. SIP in mutual fund,stock,etc)
            if transaction["tag"] == "investment" and transaction["type"] == "debit":
                self.netInvested+=amt

            # Credit Investments (e.g.withdrawn from mutual fund,stock,etc)
            elif transaction["tag"] == "investment" and transaction["type"] == "credit":
                self.netInvested-=amt

        # Savings = netEarnings - (netExpenses + netInvested)
        self.netSavings = self.netEarnings - (self.netExpenses + self.netInvested)

        dashboard_info = {
            "month":month,
            "dashboard":{
                "earnings": round(self.netEarnings, 2),
                "expenses": round(self.netExpenses,2),
                "investments": round(self.netInvested,2),
                "savings": round(self.netSavings,2)
                },
            "transactions":transactionList
        }
        return dashboard_info
    
    def extractMonthyear(self,date:str):
        month = int(date.split("/")[1])
        year = date.split("/")[2]
        return month,year
    
    def modifyTransaction(self,transaction:TransactionRequestBody):
        return modifyData(transaction)
