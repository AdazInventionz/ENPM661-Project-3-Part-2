#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Imported libraries
import numpy as np
import cv2 as cv
import time
import math





#Sets up arena with obstacles
def setup(s, r):

    global arena
    
    #Colors
    white = (255, 255, 255)
    gray = (177, 177, 177)
    darkGray = (104, 104, 104)
    
    #Draw Radial Clearance
    for x in range(0, 600):

        for y in range(0, 200):
        
            if checkClearance(x, y, s, r):
                arena[y, x] = darkGray
    
    #Draw Obstacle Borders
    for x in range(0, 600):

        for y in range(0, 200):
        
            if checkBorder(x, y, s):
                arena[y, x] = gray
    
    #Draw Obstacles
    for x in range(0, 600):

        for y in range(0, 200):
        
            if checkObstacle(x, y):
                arena[y, x] = white
                
#Checks to see if a point is within an obstacle
def checkObstacle(x, y):
    
    #Left Rectangle
    if x >= 150 and x < 165:
        
        if y < 125 and y >= 0:
            return True
    
    #Right Rectangle
    if x >= 250 and x < 265:
        
        if y < 200 and y >= 75:
            return True
        
    #Circle
    if (x - 400) * (x - 400) + (y - 90) * (y - 90) <= 50*50:
        return True
        
    return False
  
#Checks to see if a point is within the border of an obstacle
def checkBorder(x, y, s):
    
    #Left Rectangle
    if x >= 150 - s and x < 165 + s:
        
        if y < 125 + s and y >= 0:
            return True
    
    #Right Rectangle
    if x >= 250 - s and x < 265 + s:
        
        if y < 200 + s and y >= 75 - s:
            return True
        
    #Circle
    if (x - 400) * (x - 400) + (y - 90) * (y - 90) <= (50 + s) * (50 + s):
        return True
        
    return False

#Checks to see if a point is within radial clearance of a border
def checkClearance(x, y, s, r):
    
    rr = r - 1
    
    if rr == 0:
        return False
    
    #Left Rectangle
    if x >= 150 - s - rr and x < 165 + s + rr:
        
        if y < 125 + s + rr and y >= 0:
            return True
    
    #Right Rectangle
    if x >= 250 - s - rr and x < 265 + s + rr:
        
        if y < 200 + s + rr and y >= 75 - s - rr:
            return True
        
    #Circle
    if (x - 400) * (x - 400) + (y - 90) * (y - 90) <= (50 + s + rr) * (50 + s + rr):
        return True
        
    return False

#Checks to see if a point is valid (by checking obstacle, border, and clearance, as well as making sure the point is within arena bounds)
def checkValid(x, y, s, r):
    
    if checkObstacle(x, y):
        return False
    
    if checkBorder(x, y, s):
        return False
    
    if checkClearance(x, y, s, r):
        return False
    
    if (x < 0 or x >= 600 or y < 0 or y >= 250):
        return False
    
    return True





#Main Code
arena = np.zeros((200, 600, 3), dtype = "uint8")

setup(5, 10) #Change the values to change border size and robot radius, respectively
cv.imshow("Arena", arena)
cv.waitKey()
cv.destroyAllWindows()


# In[ ]:




