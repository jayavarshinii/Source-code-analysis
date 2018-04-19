#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author     : Swissky
# How to use : python index.py --dir test
# Educational purpose only !

# TODO afficher toutes les modifications de la variable

import sys
import argparse
import os, re
from detection import *
from indicators import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', action ='store', dest='dir', help="Directory to analyse")
    results = parser.parse_args()

    if os.path.isfile(results.dir):
        analysis(results.dir)
    else:
        recursive(results.dir,0)
    scanresults()

else:
    parser.print_help()
