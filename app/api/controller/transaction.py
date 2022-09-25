from models.model import TransactionRequestBody
from utils.migration import modifyData

class TransactionController:
    def __init__(self):
        pass

    def sendResponseDict(self,data,default=False):
        if default == True:
            return ({
                "dashboard":{
                    "earnings": round(0, 2),
                    "expenses": round(0,2),
                    "investments": round(0,2),
                    "savings": round(0,2)
                    },
                "transactions":[],
                "message":"No Transactions found"
            })

        return ({
                "dashboard":{
                    "earnings": round(data["earnings"], 2),
                    "expenses": round(data["expenses"],2),
                    "investments": round(data["investments"],2),
                    "savings": round(data["savings"],2)
                    },
                "transactions":data["transactions"],
                "message":data["message"]
        })

    def getTransactionData(self,transaction_list:list):
        netEarnings = 0
        netExpenses = 0
        netInvested = 0
        netSavings = 0

        if len(transaction_list) == 0:
            return netEarnings,netExpenses,netInvested,netSavings

        for transaction in transaction_list:
            amt = float(transaction["amount"])
            # Earnings
            if transaction["tag"] == "savings" and transaction["type"] == "credit":
                netEarnings+=amt

            # Debit Expenses (actual expenses)
            elif transaction["tag"] == "expense" and transaction["type"] == "debit":
                netExpenses+=amt

            # Credit Expenses (e.g. refunds,offers,cashback)
            elif transaction["tag"] == "expense" and transaction["type"] == "credit":
                netExpenses-=amt

            # Debit Investments (e.g. SIP in mutual fund,stock,etc)
            if transaction["tag"] == "investment" and transaction["type"] == "debit":
                netInvested+=amt

            # Credit Investments (e.g.withdrawn from mutual fund,stock,etc)
            elif transaction["tag"] == "investment" and transaction["type"] == "credit":
                netInvested-=amt

        # Savings = netEarnings - (netExpenses + netInvested)
        netSavings = netEarnings - (netExpenses + netInvested)
        return netEarnings,netExpenses,netInvested,netSavings
    
    def isListNull(self,transaction_list:list):
        if len(transaction_list) == 0:
            return True
        else:
            return False
    
    def extractMonthyear(self,date:str):
        month = int(date.split("/")[1])
        year = date.split("/")[2]
        return month,year
    
    def modifyTransaction(self,transaction:TransactionRequestBody):
        return modifyData(transaction)
    
    def getYearlyDashboard(self,year:str,transaction_list:list):
        if self.isListNull(transaction_list) == False:
            netEarnings,netExpenses,netInvested,netSavings = self.getTransactionData(transaction_list)
            return self.sendResponseDict({
                "earnings":netEarnings,
                "expenses":netExpenses,
                "investments":netInvested,
                "savings":netSavings,
                "transactions": transaction_list,
                "message":"Yearly Dashboard for {}".format(year)
            })
        else:
            return self.sendResponseDict(data=None,default=True)

    def getMonthlyDashboard(self,month:str,year:str,transaction_list:list):
        if self.isListNull(transaction_list) == False:
            netEarnings,netExpenses,netInvested,netSavings = self.getTransactionData(transaction_list)
            return self.sendResponseDict({
                "earnings":netEarnings,
                "expenses":netExpenses,
                "investments":netInvested,
                "savings":netSavings,
                "transactions": transaction_list,
                "message":"Monthly Dashboard for month:{}  year:{}".format(month,year)
            })
        else:
            return self.sendResponseDict(data=None,default=True)
    
    def getOverallDashboard(self,transaction_list:list):
        if self.isListNull(transaction_list) == False:
            netEarnings,netExpenses,netInvested,netSavings = self.getTransactionData(transaction_list)
            return self.sendResponseDict({
                "earnings":netEarnings,
                "expenses":netExpenses,
                "investments":netInvested,
                "savings":netSavings,
                "transactions": transaction_list,
                "message":"Overall Dashboard"
            })
        else:
            return self.sendResponseDict(data=None,default=True)
