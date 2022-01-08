#!/bin/bash
#Code written by Patzy 1/8/22
for i in $* # For each parameter passsing in to the script
do
echo "The IP address" $i "is hosted in:" #Show the IP address that is being looked up
curl -s http://ipinfo.io/$i | grep -i "country" | awk '{print $2}'; done # Grabs the info from the ipinfo website, searches for the 'country' line, and returns the two letter country code provided. 