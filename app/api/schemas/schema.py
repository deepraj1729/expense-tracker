def Serializer(transaction) ->dict:
    return {
        "id": str(transaction["_id"]),
        "date":str(transaction["trans_date"]),
        "month":str(transaction["trans_month"]),
        "year":str(transaction["trans_year"]), 
        "amount":float(transaction["trans_amount"]), 
        "type":str(transaction["trans_type"]), 
        "tag":str(transaction["trans_tag"]), 
        "remarks":str(transaction["trans_remarks"])
    }



def TransSchema(transactions) -> list:
    return [Serializer(trans) for trans in transactions]
