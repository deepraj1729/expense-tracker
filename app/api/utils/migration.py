import json

MONTH_LIST = [
    "jan","feb","mar",
    "apr","may","jun",
    "jul","aug","sep",
    "oct","nov","dec"
]

IN_FILE_PATH = "data.json"
OUT_FILE_PATH = "output.json"

def parseDate(date):
    month = int(date.split("/")[1])
    year = date.split("/")[2]
    return month,year


def modifyData(prev_data:dict):
    month,year = parseDate(prev_data["date"])
    return (
        {
            "trans_date": prev_data["date"],
            "trans_month": MONTH_LIST[month-1],
            "trans_year": year,
            "trans_amount": prev_data["amount"],
            "trans_type": prev_data["type"],
            "trans_tag": prev_data["tag"],
            "trans_remarks": prev_data["remarks"]
        }
    )


def loadFile(path):
    with open(path,"r") as f:
        data = json.load(f)
    return data


def saveFile(data,path):
    with open(path,"w") as f:
        json.dump(data,f,indent=6)
