#coding = utf-8
import json


class elevator():
    __floorPosition = 0
    __maximumFloor = 0
    __minimumFloor = 0

    def __init__(self, dataArray):
        self.checkJSONValue(fileConfiguration)

    def checkJSONValue(dataArray):
        keyWords = ["maxFloor", "minFloor", "startFloor"]
    
        for i in range (len(keyWords)):
            try :
                retValue = data[keyWords[i]]
            except KeyError:
                print ("One Value wasn't found.\nJSON value : maxFloor, minFloor, startFloor")
        if data['maxFloor'] <= data['minFloor']:
            print ("Maximum floor can't be smaller or egal to minimum floor")
            return ERRORCODE
        if data['minFloor'] >= data['maxFloor']:
            print("Minimum floor can't be higher or egal to maximum floor")
            return ERRORCODE
        if data['startFloor'] > data['maxFloor'] or data['startFloor'] < data['minFloor']:
            print("Start Floor can't be smaller than minimum floor or bigger than maximum floor")