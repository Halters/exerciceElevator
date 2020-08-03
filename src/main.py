# Process Digital Tools
# Author : Hicham TNACHERI OUAZZANI (hicham.tnacheri@epitech.eu)
# Date : 08/02/2020 at 00:45AM
# Filename : main.py

import sys
import json
import argparse
from elevator import Elevator
 
#Define global variables for a better understanding


# Prototype : errorHandling(av)
# Argument : av (array of data)
# Return value : integer (ERRORCODE or SUCCESSCODE)
# Description : Manage the potential error with user input
def errorHandling(av):
    try:
        if (av[1] != None):
            file = open(av[1], "r")
            with open(av[1], "r") as f:
                data = json.load(f)
            file.close()
    except IOError:
        raise IOError("File doesn't exist.")

# Prototype : main(av)
# Argument : av (array of string)
# Return Value : interger (SUCCESSCODE or ERRORCODE)
# Description : main function of the program
def main(av):
    actualElevator = None
    data = None

    parser = argparse.ArgumentParser (
        description= "Software for an elevator.\nType up to move up and down to move down."
    )
    parser.add_argument("filename", type=str, default="config.json", help="Configuration file")
    arv = parser.parse_args()
    try:
        errorHandling(av)
        with open(av[1], "r") as f:
            data = json.load(f)
        actualElevator = Elevator(data)
        #actualElevator.start()
    except Exception as e:
        print(type(e).__name__,":", e)
        return(84)


main(sys.argv)