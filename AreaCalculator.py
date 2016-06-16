"""
This program creates a calculator that will compute the area of a given shape, as selected by the user. 
v1.0 includes Circle and Triangle and Rectangle
By: Brian McKeown
"""

from math import pi
from time import sleep
from datetime import datetime

#set current date and time
now = datetime.now()

#variables
hint = "\nDon't forget to include the correct units! \n"
repeat = True #initiates repeat variable to start loop

#Functions/Methods

#Prints the calculated area of a given shape
def outputCalc(pArea):  
	mArea = pArea
	print '\nCalculating...'
	sleep(1)
	print ("\nArea: %.2f. \n%s" % (mArea, hint))

#Invalid input prompt
def invalid():
	print "\nInvalid input! Please try again!"
	sleep(1)

#Calculates the area of a circle
def circleArea(userInput): 
	userInput = radius
	area = pi * radius ** 2
	return area

#Calculates the area of a triangle
def triangleArea(pBase, pHeight):
	base = pBase
	height = pHeight
	area = (0.5) * base * height
	return area

#Calculates the area of a rectangle
def rectArea(pWidth, pHeight):
	width = pWidth
	height = pHeight
	area = width * height
	return area

#Calculates the area of a square
def squareArea(pSide):
	side = pSide
	area = side * side
	return area

"""
********************
Program Run:
********************
"""

#startup message
print "\nCalculator is starting up..."

#print date and time
print '%s/%s/%s  %s:%s' % (now.month, now.day, now.year, now.hour, now.minute)

#simulate thinking calculator (delay 1 second)
sleep(1)

while repeat == True: #Start of outer loop
    
	#user input prompt
	option = raw_input("\nEnter C for Circle\nEnter T for Triangle\nEnter R for Rectangle\nEnter S for Square\nEnter Here: ")
	option = option.upper() #corrects lowercase input
    
	if option == 'C':
		
		while repeat == True:
			try:
				radius = float(raw_input("Enter radius: "))
				area = circleArea(radius)
				outputCalc(area)
 				repeat = False
			except ValueError:
				invalid()
				repeat = True
	
	elif option == 'T':

		while repeat == True:
			try:
				base = float(raw_input("Enter the length of the base: "))
				height = float(raw_input("Enter the height: "))
				area = triangleArea(base, height)
				outputCalc(area)
				repeat = False
			except ValueError:
				invalid()
				repeat = True

	elif option == 'R':

		while repeat == True:
			try:
				width = float(raw_input("Enter the width: "))
				height = float(raw_input("Enter the height: "))
				area = rectArea(width, height)
				outputCalc(area)
				repeat = False
			except ValueError:
				invalid()
				repeat = True

	elif option == 'S':

		while repeat == True:
			try:
				side = float(raw_input("Enter the side length: "))
				area = squareArea(side)
				outputCalc(area)
				repeat = False
			except ValueError:
				print "\nInvalid input! Please try again!"
				sleep(1)
				repeat = True
	
	else:
		print "\nYou entered an invalid character!\nRestarting..."
		sleep(1)
		repeat = True
    
    #Go again prompt
	if repeat == False:
		goAgain = raw_input("\nEnter AGAIN to go again. \nEnter any other key to quit.\n")
		goAgain = goAgain.upper() # corrects lowercase input
        
		if goAgain == 'AGAIN':
			repeat = True
		else:
			print "\nThank you! See you next time!"
			sleep(1)
			print "Program terminated."
			
