#!/usr/bin/python3
import argparse, io
from signal import signal, SIGINT
from urllib.request import urlopen

# Header
header = """[[YELLOW]]
 ###############################################
 ############### HTTP PAGE CLONER ##############
 ###############################################

 The Script allows you to clone the HTML Source
 code of any web page (Online/Local). By Nzanoa.[[NC]]
 ie. [[LPURPLE]]python3 HTTPageCloner.py -u https://moyindugeek.com[[NC]]
"""

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

# Print Header
print(ColorText(header))

# Set argument
parser = argparse.ArgumentParser(prog=" HTMLPageCloner", description=" Clone HTML Source code")
parser.add_argument("-u", "--url", metavar='', required=True, help="URL of the page you want to copy")
parser.add_argument("-f", "--filename", metavar='', required=True, help="Where you want to save HTML code")
args = parser.parse_args()

# print("Enter Website ie. http://hackingtut.com")
try:
    # Go to url
    response = urlopen(args.url)
    reach_url = " [+][[GREEN]] URL reached ... [[NC]]"
    print(ColorText(reach_url))
    # Fetch content of page
    page_source = response.read()
    copy_url = " [+][[GREEN]] Copying source code ... [[NC]]"
    print(ColorText(copy_url))
    # Save source code in html file
    with io.FileIO(args.filename, "w") as file:
    	file.write(page_source)
    copied_page = " [+][[GREEN]] The page was successfully copied![[NC]]"
    copied_result = " [+] The source code was saved in [[BLUE]]"+ args.filename + "[[NC]]\n"
    print(ColorText(copied_page))
    print(ColorText(copied_result))
except Exception as e:
    show_error = "[+][[RED]] [-] " + e + " [NC]]"
    print(ColorText(show_error))
