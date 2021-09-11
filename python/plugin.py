#!/usr/bin/env python3
# imports
import os
import sys
# import the drum api
home = os.path.expanduser('~')
mymodule_dir = os.path.join( home, 'drumbash', 'api')
sys.path.append( mymodule_dir )
import api
from sys import exit

args = sys.argv
if len(args) > 1 or len(args) == 0:
    exit()
if args[1] == "-h":
    print("indev")
