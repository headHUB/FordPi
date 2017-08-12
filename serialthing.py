from arduino import Arduino
import httplib, urllib
from time import localtime, strftime
# download from http://code.google.com/p/psutil/
import psutil
import time

b = Arduino('/dev/ttyUSB0')
TMP = 0
TPS = 1
JOY = 2
b.output([])
while (True):
	temp=b.analogRead(TMP)
	TpS=b.analogRead(TPS)
	JoY=b.analogRead(JOY)
	params = urllib.urlencode({'field1': temp, 'field2': TpS, 'field3': JOY,'key':'EGHEAWLI2UISSAR8'})
	headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
	conn = httplib.HTTPConnection("api.thingspeak.com:80")
	print temp, ', ', TpS,', ',JoY
	print TpS
	print JoY
	time.sleep(.5)
	try:
		conn.request("POST", "/update", params, headers)
		response = conn.getresponse()
		print temp
		print TpS
		print strftime("%a, %d %b %Y %H:%M:%S", localtime())
		print response.status, response.reason
		data = response.read()
		conn.close()
	except:
		print "connection failed"	
###sleep for 16 seconds (api limit of 15 secs)
##if __name__ == "__main__":
##	
##    time.sleep(16) 
