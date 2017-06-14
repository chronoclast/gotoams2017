"""
DESCRIPTION:
	Example script to read data from 1x sensor connected to the ifm AL1100 IO-Link master.
	For simplicity, the following code is blocking (as it's using "time.sleep()" between intervals).
	This is the most basic script and it can be used as a building block, so it has been heavily commented.

AUTHOR:
	Jaime Gonzalez-Arintero
	<jaime@relayr.io>

SENSOR(S) USED IN THIS EXAMPLE:
	Reference: ifm TA2105
	Type: Temperature transmitter
	Raw data format: 2 bytes, hexadecimal
	Scale factor: 0.1

TO-DO:
	- Take the IP address out of the POST request, and add field so it can be modified easily.
"""

import requests
import json
import time


# Let's fire this up!
# ---------------

longstring = """\
                                                                 
               )                               )    )    )      )  
 (  (       ( /(            )     )           ( /( ( /( ( /(   ( /(  
 )\))(  (   )\()) (      ( /(    (     (      )(_)))\()))\())  )\()) 
((_))\  )\ (_))/  )\     )(_))   )\  ' )\    ((_) ((_)\((_)\  ((_)\  
 (()(_)((_)| |_  ((_)   ((_)_  _((_)) ((_)   |_  )/  (_)/ (_)|__  /  
/ _` |/ _ \|  _|/ _ \   / _` || '  \()(_-<    / /| () | | |    / /   
\__, |\___/ \__|\___/   \__,_||_|_|_| /__/   /___|\__/  |_|   /_/    
|___/                                                           
"""

print longstring

# ---------------

# The header "content-length" is mandatory according to the ifm specifications.
headers = {'content-type': 'text/json', 'content-length': '25'}

# The temperature transmitter is connected in port 2; "gpd" stands for "get process data".
# The index "i" and subindex "s" are to be provided but should be 0. 
data = {'p': 2, 'req': 'gpd', 'i': 0, 's': 0}

while True:
	
	try:
		r = requests.post('http://192.168.1.100:80', data=json.dumps(data), headers=headers)
		response = json.loads(r.text)
		# Uncomment the line below for debugging
		# print response

		# Parse the value in raw hexadecimal format from the JSON object
		raw_hex_value = response['v']
		# Convert the value from hexadecimal (base 16) to integer (base 10)
		scaled_int_value = int(raw_hex_value, 16)
		# Apply the scale factor to get the actual value
		int_value = scaled_int_value * 0.1
		# Print the current value on the terminal
		print 'Temperature:' + str(int_value) + ' C'


		# Sending the data via HTTP to the relayr platform...
		# ---------------

		try:
			headersCloud = {'content-type': 'application/json', 'Authorization': 'Bearer IUnpyKShxOIa7j7qpBq8COkiGsOms2IAkWI2OSTNiQ8AsTEoIYUIu9tnU8U6VHqD', 'Cache-Control':'no-cache'}
			dataCloud = {'meaning': 'temperature', 'value': int_value}
			rCloud = requests.post('https://api.relayr.io/devices/b421ceaf-7443-43bb-bdd0-74291b44ec87/data', data=json.dumps(dataCloud), headers=headersCloud)
			print "Request sent to the relayr Platform!"

		except:
			print "Unable to publish data onto the cloud! Check the token and the device ID!"

		# ---------------


	except:
		print "Unable to read from device! Check the IP address and the IO-Link port!"
	
	# This sets the polling frequency 
	time.sleep(0.5)