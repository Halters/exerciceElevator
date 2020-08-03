# Process Digital Tools
# Author : Hicham TNACHERI OUAZZANI (hicham.tnacheri@epitech.eu)
# Date : 08/02/2020 at 00:45AM
# Filename : elevator.py

import sys
import time
import json


class Elevator():
    __floor_position = 0
    __maximum_floor = 0
    __minimum_floor = 0

    # Prototype = __init__(self, data_array)
    # Argument = self (mandatory argument) & data_array(JSON packet)
    # Return Value = None
    # Description = Elevator's object constructor
    def __init__(self, data_array):
        print ('Initialization of Elevator software ..')
        self.check_json_value(data_array)
        self.set_floor_postion(data_array['startFloor'])
        self.set_max_floor(data_array['maxFloor'])
        self.set_min_floor(data_array['minFloor'])
    
    # Prototype = set_floor_postion(self, initial_pos)
    # Argument = self(mandatory argument) & initial_pos (integer)
    # Return Value = None
    # Description = setter for __floor_position attribute
    def set_floor_postion (self, initial_pos):
        self.__floor_position = initial_pos

    # Prototype = set_max_floor(self, max_value)
    # Argument = self(mandatory argument) & max_value (integer)
    # Return Value = None
    # Description = setter for __maximum_floor attribute
    def set_max_floor(self, max_value):
        self.__maximum_floor = max_value

    # Prototype = set_min_floor(self, min_value)
    # Argument = self(mandatory argument) & min_value (integer)
    # Return Value = None
    # Description = setter for __minimum_floor attribute
    def set_min_floor(self, min_value):
        self.__minimum_floor = min_value

    # Prototype = get_floor_position(self)
    # Argument = self(mandatory argument)
    # Return Value = None
    # Description = getter for __floor_position attribute
    def get_floor_position(self):
        return self.__floor_position
    
    # Prototype = get_max_floor(self)
    # Argument = self(mandatory argument)
    # Return Value = None
    # Description = getter for __maximum_floor attribute
    def get_max_floor(self):
        return self.__maximum_floor

    # Prototype = get_min_floor(self)
    # Argument = self(mandatory argument)
    # Return Value = None
    # Description = getter for __minimum_floor attribute
    def get_min_floor(self):
        return self.__minimum_floor
    
    # Prototype = checkJSONValue(self, data_array)
    # Argument = self (mandatory argument) & dataArray(JSON packet)
    # Return Value = raising Exceptions
    # Description = Check the JSON packet value and their coherences.
    def check_json_value(self, data_array):
        keyWords = ["maxFloor", "minFloor", "startFloor"]
    
        for iterator in range(len(keyWords)):
            try :
                retValue = data_array[keyWords[iterator]]
            except KeyError:
                raise KeyError("One Value wasn't found.\nJSON value : maxFloor, minFloor, startFloor")
        if data_array['maxFloor'] <= data_array['minFloor']:
            raise ValueError("Maximum floor can't be smaller or egal to minimum floor")
        if data_array['minFloor'] >= data_array['maxFloor']:
            raise ValueError("Minimum floor can't be higher or egal to maximum floor")
        if data_array['startFloor'] > data_array['maxFloor'] or data_array['startFloor'] < data_array['minFloor']:
            raise ValueError("Start Floor can't be smaller than minimum floor or bigger than maximum floor")
        return

    # Prototype = move_up(self, order_to_exec)
    # Argument = self (mandatory argument) & order_to_exec(str list)
    # Return Value = raising Exception
    # Description = Manages the upward movement of the elevator
    def move_up(self, order_to_exec):
        actual_floor = self.get_floor_position()
        to_move = 1

        if (len(order_to_exec) > 1):
            if (order_to_exec[1] != None):
                try :
                    to_move = int(order_to_exec[1])
                except ValueError:
                    raise ValueError("Floor can only be an integer.")
        if ((actual_floor + to_move) > self.get_max_floor()):
            print("You can't go higher. Maximum floor already reach or you will be out of band.")
            return
        else:
            for temp in range (actual_floor, actual_floor + to_move):
                print ("Stage", actual_floor , "to Stage", actual_floor + 1)
                self.set_floor_postion(actual_floor + 1)
                actual_floor += 1
                time.sleep(2)

    # Prototype = move_down(self, order_to_exec)
    # Argument = self (mandatory argument) & order_to_exec (str list)
    # Return Value = raising Exception
    # Description = manages the downward movement of the elevator
    def move_down(self, order_to_exec):
        actual_floor = self.get_floor_position()
        to_move = 1

        if (len(order_to_exec) > 1):
            if (order_to_exec[1] != None):
                try :
                    to_move = int(order_to_exec[1])
                except ValueError:
                    raise ValueError("Floor can only be an integer.")
        if ((actual_floor - to_move) < self.get_min_floor()):
            print("You can't go higher. Minimum floor already reach or you will be out of band.")
            return
        else:
            for temp in range (actual_floor, actual_floor + to_move):
                print ("Stage", actual_floor , "to Stage", actual_floor - 1)
                self.set_floor_postion(actual_floor - 1)
                actual_floor -= 1
                time.sleep(2)


    # Prototype = print_status(self)
    # Argument = self (mandatory argument)
    # Return Value = raising Exception
    # Description = Print the actual status of our elevator.
    def print_status(self) :
        print("Elevator is at floor", self.__floor_position, "(max=",self.get_max_floor(), "& min=",self.get_min_floor(),")")


    # Prototype = start(self)
    # Argument = self (mandatory argument)
    # Return Value = raising Exception
    # Description = Check the JSON packet value and their coherences.
    def start(self):
        print ("Enter a command :")
        print ("Starting floor : ", self.get_floor_position(), "(max=",self.get_max_floor(), "& min=",self.get_min_floor(),")")
        for line in sys.stdin:
            line = line.rstrip().split()
            print ("You are actually stage", self.get_floor_position())
            if (line[0].lower() == "end"):
                return(0)
            if (line[0].lower() == "up"):
                try:
                    self.move_up(line)
                    self.print_status()
                except Exception as e:
                    print(type(e).__name__,":", e)
                    pass
            elif (line[0].lower() == "down"):
                try:
                    self.move_down(line)
                    self.print_status()
                except Exception as e:
                    print(type(e).__name__,":", e)
                    pass
            else :
                print("Wrong command. Use up or down commands.")
                pass