from multiprocessing.dummy import Array
import string
import requests
import sys

CLIENT_ID = "hHR45NTrkCkDRWY_bjJN"
CLIENT_SECRET = "oWds2z7KvP"
REQUEST_URL = "https://openapi.naver.com/v1/datalab/search"

# * Request Params for API
class Param:
    __PARAM = {
        "startDate" : "",
        "endDate" : "",
        "timeUnit" : "",
        "keywordGroups" : "",
        "keywordGroups.groupName" : "",
        "keywordGroups.keywords" : "",
        "device" : ""
    }

    __DEVICE = {
        "male" : "m",
        "female" : "f"
    }
    
    def __init__(self, startDate: str, endDate: str 
                 ,timeUnit:string, keywordGroups:list , 
                 keywordGroup_groupName: list, 
                 keyWords: list, device= "mo" : str, 
                 gender = "" : str, age = "": str) -> None:
        pass
