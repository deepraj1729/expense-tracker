from datetime import datetime
# from .model import TransactionRequestBody

def validateRequestBody(content:dict):
    try:
        date = datetime.strptime(content.trans_date, '%d/%m/%y')
        amt = float(content.trans_amount)
        tag = content.trans_tag
        transType = content.trans_type
        remarks = content.trans_remarks
        return True

    except Exception as e:
        return False


