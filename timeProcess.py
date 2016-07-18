# coding: utf-8

import os
import time

if os.name = "nt":
	inputDir = ""
else:
	inputDir = ""

startTime = time.time()
startTimeReadable = str(time.strftime("%Y-%m-%d %H:%M:%S"))
print "Start Time: " + startTimeReadable

count = 0
totalCount = len(os.listdir(inputDir))
startTime = time.time()
totelTime = 0
for thing in os.listdir(inputDir):
	count = count + 1
	
	#for limiting images for testing purposes
	if count > 0:
		print "reading " + thing
		print str(count) + " of " + str(totalCount)
		
		#do stuff here
		time.sleep(10)
		
		
		
		processTime = time.time() - startTime
		totelTime = totelTime + processTime
		print "Process took " + str(processTime) + " seconds or " + str(processTime/60) + " minutes or " + str(processTime/3600) + " hours"
		avgTime = totelTime/count
		print "Average is " + str(avgTime)
		remaning = totalCount-count
		print str(remaning) + " Remaining"
		estimateTime = avgTime*remaning
		print "Estimated time left: " + str(estimateTime) + " seconds or " + str(estimateTime/60) + " minutes or " + str(estimateTime/3600) + " hours"
		diskStartTime = time.time()
		
		