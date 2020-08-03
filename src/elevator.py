#coding = utf-8
# Process Digital Tools
# Author : Hicham TNACHERI OUAZZANI (hicham.tnacheri@epitech.eu)
# Date : 08/02/2020 at 00:45AM
# Filename : elevator.py

import sys
import json


class Elevator():
    __floorPosition = 0
    __maximumFloor = 0
    __minimumFloor = 0

    def __init__(self, dataArray):
        try:
            self.checkJSONValue(dataArray)
        except Exception as e:
            raise(e)

    def checkJSONValue(self, dataArray):
        keyWords = ["maxFloor", "minFloor", "startFloor"]
    
        for iterator in range (len(keyWords)):
            try :
                retValue = dataArray[keyWords[iterator]]
            except KeyError:
                raise KeyError("One Value wasn't found.\nJSON value : maxFloor, minFloor, startFloor")
        if dataArray['maxFloor'] <= dataArray['minFloor']:
            raise ValueError("Maximum floor can't be smaller or egal to minimum floor")
        if dataArray['minFloor'] >= dataArray['maxFloor']:
            raise ValueError("Minimum floor can't be higher or egal to maximum floor")
        if dataArray['startFloor'] > dataArray['maxFloor'] or dataArray['startFloor'] < dataArray['minFloor']:
            raise ValueError("Start Floor can't be smaller than minimum floor or bigger than maximum floor")
