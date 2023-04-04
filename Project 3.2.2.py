#!/usr/bin/env python
# coding: utf-8

# In[13]:


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
        
            if checkClearance(float(x/100 - 0.5), float(y/100 - 1), s, r):
                arena[y, x] = darkGray
    
    #Draw Obstacle Borders
    for x in range(0, 600):

        for y in range(0, 200):
        
            if checkBorder(float(x/100 - 0.5), float(y/100 - 1), s):
                arena[y, x] = gray
    
    #Draw Obstacles
    for x in range(0, 600):

        for y in range(0, 200):
            
            if (x == 0 and y == 0) or (x == 600 - 1 and y == 200 - 1):
                print(float(x/100 - 0.5), float(y/100 - 1))
            
            if checkObstacle(float(x/100 - 0.5), float(y/100 - 1)):
                arena[y, x] = white
                
#Checks to see if a point is within an obstacle
def checkObstacle(x, y):
    
    #Left Rectangle
    if x >= 1 and x < 1.15:
        
        if y < 1 and y >= -0.25:
            return True
    
    #Right Rectangle
    if x >= 2 and x < 2.15:
        
        if y < 0.25 and y >= -1:
            return True
        
    #Circle
    if (x - 3.5) * (x - 3.5) + (y - 0.1) * (y - 0.1) <= 0.5*0.5:
        return True
        
    return False
  
#Checks to see if a point is within the border of an obstacle
def checkBorder(x, y, s):
    
    #Left Rectangle
    if x >= 1 - s and x < 1.15 + s:
        
        if y < 1 + s and y >= -0.25 - s:
            return True
    
    #Right Rectangle
    if x >= 2 - s and x < 2.15 + s:
        
        if y < 0.25 + s and y >= -1:
            return True
        
    #Circle
    if (x - 3.5) * (x - 3.5) + (y - 0.1) * (y - 0.1) <= (0.5 + s) * (0.5 + s):
        return True
        
    return False

#Checks to see if a point is within radial clearance of a border
def checkClearance(x, y, s, r):
    
    rr = r - 0.01
    
    if rr == 0:
        return False
    
    #Left Rectangle
    if x >= 1 - s - rr and x < 1.15 + s + rr:
        
        if y < 1 + s + rr and y >= -0.25 - s - rr:
            return True
    
    #Right Rectangle
    if x >= 2 - s - rr and x < 2.15 + s + rr:
        
        if y < 0.25 + s + rr and y >= -1:
            return True
        
    #Circle
    if (x - 3.5) * (x - 3.5) + (y - 0.1) * (y - 0.1) <= (0.5 + s + rr) * (0.5 + s + rr):
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

setup(0.05, 0.1) #Change the values to change border size and robot radius, respectively
cv.imshow("Arena", arena)
cv.waitKey()
cv.destroyAllWindows()


# In[ ]:





# In[ ]:




