import urllib2
import sys
import io
from signal import signal, SIGINT

# Header
header = """[[YELLOW]]
 #############################################
 ############## WEBSITE CLONER ###############
 #############################################

 The Script allows you to clone the FrontEnd
 of any website (Online / Local). By Nzanoa.[[NC]]
 ie. [[LPURPLE]]python3 WebsiteCloner.py[[NC]]
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

# Cloning function
def cloning():
	print("Enter Website ie. http://hackingtut.com")
	input_hey = " [+][[BLUE]] Website >>  [[NC]]"
	hey = input("{}".format(ColorText(input_hey)))
	# Go to page
	response = urllib2.urlopen(hey)
	# Fetch content of page
	page_source = response.read()
	# Save source code in html file
	with io.FileIO("websitesource.html","w") as file:
		file.write(page_source)
	anounce_end = " [+][[GREEN]]  [+] Finished !!![[NC]]"
	print(anounce_end)

cloning()
