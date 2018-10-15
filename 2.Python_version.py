'''2. Write a Python program to get the Python version you are using.'''

import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

'''3. Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14'''

import datetime
dt=datetime.datetime.now()
print dt

'''4. Write a Python program which accepts the radius of a circle from the user and compute the area.  
Sample Output :
r = 1.1
Area = 3.8013271108436504'''

rad=float(input("Enter radius of circle"))
area=3.14*rad*rad
print "Area of circle is: ",area,


