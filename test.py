from multiprocessing.dummy import Array
import json
import urllib.request

CLIENT_ID = "hHR45NTrkCkDRWY_bjJN"
CLIENT_SECRET = "oWds2z7KvP"
REQUEST_URL = "https://openapi.naver.com/v1/datalab/search"

# * Request Params for API
class Param:
    __PARAM = {
        "startDate" : "", # yyyy-mm-dd형식, 2016년 1월 1일부터 조회할 수 있다.
        "endDate" : "",
        "timeUnit" : "", # 구간 단위 - date: 일간 -week : 주간 -month: 월간
        "keywordGroups" : [], #주제어와 주제어에 해당하는 검색의 묶음 쌍의 배열, 최대 5개의 쌍을 배열로 설정할 수 있다.
        # "keywordGroups.groupName" : "", # 주제어, 검색어 묶음을 대표하는 이름
        # "keywordGroups.keywords" : [], # 주제어에 해당하는 검색어. 최대 20개의 검색어를 배열로 설정할 수 있다.
        "device" : "",
        "gender" : "",
        "ages" : []
    }

    
    def __init__(self, startDate: str, endDate: str 
                 ,timeUnit:str, keywordGroups:list , 
                 device:str = "mo", gender:str = "f", ages:list = ["5","6","7"]) -> None:

                 self.__PARAM["startDate"] = startDate
                 self.__PARAM["endDate"] = endDate
                 self.__PARAM["timeUnit"] = timeUnit
                 self.__PARAM["keywordGroups"] = keywordGroups
                 self.__PARAM["device"] = device
                 self.__PARAM["gender"] = gender
                 self.__PARAM["ages"] = ages
                 
    def getParam(self):
        return self.__PARAM


startDate = "2020-01-01"
endDate = "2020-12-30"
groupA = {
    "groupName" : "휘귀식물",
    "keywords": ["몬스테라", "카라멜 마블"]
}
keyGroups = [groupA]
myParam = Param(startDate=startDate, endDate=endDate, timeUnit="month", keywordGroups=keyGroups)
body = json.dumps(myParam.getParam())

request = urllib.request.Request(REQUEST_URL)
request.add_header("X-Naver-Client-Id",CLIENT_ID)
request.add_header("X-Naver-Client-Secret",CLIENT_SECRET)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

