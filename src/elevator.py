#coding = utf-8
# Process Digital Tools
# Author : Hicham TNACHERI OUAZZANI (hicham.tnacheri@epitech.eu)
# Date : 08/02/2020 at 00:45AM
# Filename : elevator.py

import sys
import json


class Elevator():
    __floor_position = 0
    __maximum_floor = 0
    __minimum_floor = 0

    # Prototype = __init__(self, dataArray)
    # Argument = self (mandatory argument) & dataArray(JSON packet)
    # Return Value =
    # Description = Elevator's constructor
    def __init__(self, data_array):
        try:
            self.check_json_value(data_array)
            self.set_floor_postion(data_array['startFloor'])
            self.set_max_floor(data_array['maxFloor'])
            self.set_min_floor(data_array['minFloor'])
        except Exception as e:
            raise(e)
    
    # Prototype = set_floor_postion(self, initial_pos)
    # Argument = self(mandatory argument) & initial_pos (interger)
    # Return Value = None
    # Description = setter for __floor_position
    def set_floor_postion (self, initial_pos):
        self.__floor_position = initial_pos

    # Prototype = set_max_floor(self, max_value)
    # Argument = self(mandatory argument) & max_value (interger)
    # Return Value = None
    # Description = setter for __maximum_floor
    def set_max_floor(self, max_value):
        self.__maximum_floor = max_value

    # Prototype = set_min_floor(self, min_value)
    # Argument = self(mandatory argument) & min_value (interger)
    # Return Value = None
    # Description = setter for __minimum_floor
    def set_min_floor(self, min_value):
        self.__minimum_floor = min_value

    # Prototype = get_floor_position(self)
    # Argument = self(mandatory argument)
    # Return Value = None
    # Description = getter for __floor_position
    def get_floor_position(self):
        return self.__floor_position
    
    # Prototype = setFloorPosition(self, initialPos)
    # Argument = self(mandatory argument) & initialPos (interger)
    # Return Value = None
    # Description = setter of __floorPosition
    def get_max_floor(self):
        return self.__maximum_floor

    # Prototype = setFloorPosition(self, initialPos)
    # Argument = self(mandatory argument) & initialPos (interger)
    # Return Value = None
    # Description = setter of __floorPosition
    def get_min_floor(self):
        return self.__minimum_floor
    
    # Prototype = checkJSONValue(self, dataArray)
    # Argument = self (mandatory argument) & dataArray(JSON packet)
    # Return Value = raising Exceptions
    # Description = Check the JSON packet value and their coherences.
    def check_json_value(self, data_array):
        keyWords = ["maxFloor", "minFloor", "startFloor"]
    
        for iterator in range (len(keyWords)):
            try :
                retValue = dataArray[keyWords[iterator]]
            except KeyError:
                raise KeyError("One Value wasn't found.\nJSON value : maxFloor, minFloor, startFloor")
        if data_array['maxFloor'] <= data_array['minFloor']:
            raise ValueError("Maximum floor can't be smaller or egal to minimum floor")
        if data_array['minFloor'] >= data_array['maxFloor']:
            raise ValueError("Minimum floor can't be higher or egal to maximum floor")
        if data_array['startFloor'] > data_array['maxFloor'] or data_array['startFloor'] < data_array['minFloor']:
            raise ValueError("Start Floor can't be smaller than minimum floor or bigger than maximum floor")

    # Prototype = start(self)
    # Argument = self (mandatory argument)
    # Return Value = raising Exception
    # Description = Check the JSON packet value and their coherences.
    def start(self):
        for line in sys.stdin:
            line = line.rstrip()
            if (line.lower() == "end"):
                print (line)
                return(0)
