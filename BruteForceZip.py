#!/usr/bin/python3
from zipfile import ZipFile
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
 eg. [[LPURPLE]]./BruteForceZip.py -z file.zip -p pwd.txt[[NC]]
"""
# Print Header
print(ColorText(header))

# Set argument
parser = argparse.ArgumentParser(prog=" BruteForceZip", description=" Brutefore Zip File")
parser.add_argument("-z", "--zipfile", metavar='', required=True, help="Zip File")
parser.add_argument("-p", "--passfile", metavar='', required=True, help="Password File")
args = parser.parse_args()

try:
    zfile = ZipFile(args.zipfile)
    passfile = open(args.passfile, 'r')
    test_amount = 0
    # with ZipFile(args.zipfile) as myzip:
    for line in passfile.readlines():
        password = line.strip('\n')
        # myzip.extractall(pwd=password)
        try:
            zfile.extractall(pwd=password)
            show_results = " [+] Password Found =[[GREEN]] {}[[NC]]\n".format(password)
            print(ColorText(show_results))
            exit(0)
        except Exception as e:
            test_amount += 1
except Exception as e:
    show_error = "[+][[RED]] [-] " + e + " [NC]]"
    # print(ColorText(show_error))
    print("Quit after " + test_amount + "tries")
