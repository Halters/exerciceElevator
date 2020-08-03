# Process Digital Tools
# Author : Hicham TNACHERI OUAZZANI (hicham.tnachgeri@epitech.eu)
# Date : 08/02/2020 at 00:45AM
# Filename : main.py

import sys
import json
from math import *
from elevator import Elevator
 
#Define global variables for a better understanding
ERRORCODE = -1
SUCCESSCODE = 0
USAGE = "\nUsage : pyhton main.py \"path to configuration file\""

# Prototype : errorHandling(av)
# Argument : av (array of data)
# Return value : integer (ERRORCODE or SUCCESSCODE)
# Description : Manage the potential error with user input
def errorHandling(av):

        try:
            if (len(av) != 2):
                raise IndexError("Too few arguments")
            if (av[1] != None):
                file = open(av[1], "r")
                with open(av[1], "r") as f:
                    data = json.load(f)
                #checkJSONFileValidity(data)
                file.close()
        except IOError:
            raise IOError("File doesn't exist.")


# Prototype : checkJSONFileValidity(data)
# Argument : data (JSON packet)
# Return Value : bool (true or false)
# Description :  check the format of configuration file
#def checkJSONFileValidity(data):
#    keyWords = ["maxFloor", "minFloor", "startFloor"]
#    
#    for i in range (len(keyWords)):
#        try :
#            retValue = data[keyWords[i]]
#        except KeyError:
#            print ("One Value wasn't found.\nJSON value : maxFloor, minFloor, startFloor")
#    if data['maxFloor'] <= data['minFloor']:
#        print ("Maximum floor can't be smaller or egal to minimum floor")
#        return ERRORCODE
#    if data['minFloor'] >= data['maxFloor']:
#        print("Minimum floor can't be higher or egal to maximum floor")
#        return ERRORCODE
#    if data['startFloor'] > data['maxFloor'] or data['startFloor'] < data['minFloor']:
#        print("Start Floor can't be smaller than minimum floor or bigger than maximum floor")



# Prototype : main(av)
# Argument : av (array of string)
# Return Value : interger (SUCCESSCODE or ERRORCODE)
# Description : main function of the program
def main(av):
    actualElevator = None
    data = None

    try:
        errorHandling(av)
        with open(av[1], "r") as f:
            data = json.load(f)
        actualElevator = elevator(data)
    except Exception as e:
        print(type(e).__name__,":", e)
        return(84)


main(sys.argv)