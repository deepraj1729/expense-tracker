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


def modifyData(prev_data):
    month,year = parseDate(prev_data["trans_date"])
    return (
        {
            "trans_date": prev_data["trans_date"],
            "trans_month": MONTH_LIST[month-1],
            "trans_year": year,
            "trans_amount": prev_data["trans_amount"],
            "trans_type": prev_data["trans_type"],
            "trans_tag": prev_data["trans_tag"],
            "trans_remarks": prev_data["trans_remarks"]
        }
    )


def loadFile(path):
    with open(path,"r") as f:
        data = json.load(f)
    return data


def saveFile(data,path):
    with open(path,"w") as f:
        json.dump(data,f,indent=6)
