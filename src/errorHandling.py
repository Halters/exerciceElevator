#coding = utf-8
# Process Digital Tools
# Author : Hicham TNACHERI OUAZZANI (hicham.tnacheri@epitech.eu)
# Date : 08/02/2020 at 00:45AM
# Filename : errorHandling.py


import sys
import json

# Prototype : errorHandling(av)
# Argument : av (array of data)
# Return value : integer (ERRORCODE or SUCCESSCODE)
# Description : Manage the potential error with user input
def errorHandling(av):
    try:
        if (av[1] == None):
            file = open(av[1], "r")
            with open(av[1], "r") as f:
                data = json.load(f)
            file.close()
    except IOError:
        raise IOError("File doesn't exist or Filename can't be None")
        