#!/usr/bin/python3
import zipfile
import argparse
from signal import signal, SIGINT

# Colors
COLORS = {
    'NC': '\033[0m',
    'RED': '\033[1;31m',
    'GREEN': '\033[0;32m',
    'BLUE': '\033[0;34m',
    'YELLOW': '\033[1;33m',
    'LPURPLE': '\033[1;35m'
}

# Replace color by ANSI COLOR CODE
def ColorText(text):
    for color in COLORS:
        text = text.replace('[[' + color + ']]', COLORS[color])
    return text

# Handle signal
def handler(signal_received, frame):
    # Handle any cleanup here
    signal_error = "\n [-][[RED]] Exiting gracefully [[NC]]\n"
    print(ColorText(signal_error))
    exit(0)

signal(SIGINT, handler)

# Header
header = """[[YELLOW]]
 ###########################################
 ############# BRUTEFORCE ZIP ##############
 ###########################################

 This Script will help you bruteforce a zip
 file. By Nzanoa.[[NC]]
 eg. [[LPURPLE]]python3 BruteForceZip.py -z file.zip -p pwd.txt[[NC]]
"""

# Print Header
print(ColorText(header))

# Set argument
parser = argparse.ArgumentParser(prog=" BruteForceZip", description=" Brutefore Zip File")
parser.add_argument("-z", "--zipfile", type=int, metavar='', required=True, help="Zip File")
parser.add_argument("-p", "--passfile", type=int, metavar='', required=True, help="Password File")
args = parser.parse_args()

try:
    zfile = open(args.zipfile, 'r')
    passfile = open(args.passfile, 'r')

    for line in passfile.readlines():
    	password = line.strip('\n')
    	zfile.extractall(pwd=password)
    	print(" [+][[GREEN]] Password Found = {}[[NC]]\n".format(password))
    	exit(0)
except:
    print(args.help)
