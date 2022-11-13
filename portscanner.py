import socket
import subprocess
import sys
import getopt
from datetime import datetime

#Blank your screen
subprocess.call('clear', shell=True)

argumentList = sys.argv[1:]

#Options
options = "hr:o:"

#long Options
longOptions = ["help", "range=", "output="]

outputFile = None

try:
    #Parsing Arguments
    arguments, values = getopt.getopt(argumentList, options, longOptions)

    #checking each argument
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-h", "--help"):
            print ("Displaying Help")
            sys.exit()
        elif currentArgument in ("-r", "--range"):
            print (("Port Range Selected (% s)") % currentValue)
        elif currentArgument in ("-o", "--output"):
            print (("Output file set as %s") % currentValue)
            outputFile = currentValue

except getopt.error as err:
    #output error, and return with an error code
    print (str(err))

#Ask for input

print ("Welcome to Patzy's Port Scanner")
scanServer = input("Enter a remote host to scan: ")

scanServerIP = socket.gethostbyname(scanServer)


#Print a nice banner with information on which host we are about to scan
print ("_" * 60)
print ("Please wait, scanning remote host", scanServerIP)
print ("_" * 60)

#Check the date and time the scan was started
t1 = datetime.now()

#Using the range function to specify portsscan
#Also we will do error handling

try:
        for port in range (1,5000):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((scanServerIP, port))
            if result == 0:
                print ("Port {}:    Open".format(port) + " Protocol - " + socket.getservbyport(port))
            sock.close()

except KeyboardInterrupt:
    print ("Aborting Scan")
    sys.exit()

except socket.gaierror:
    print ("Hostname could not be resolved. Exiting")
    sys.exit()

except socket.error:
    print ("Couldn't connect to server")
    sys.exit()

#Checking time again
t2 = datetime.now()

#Calculate the difference in time to know how long the scan took
total = t2 - t1

#Printingg the information on the screen
print ('Scanning Completed in: ', total)
     