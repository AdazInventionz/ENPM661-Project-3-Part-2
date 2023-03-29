#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Imported libraries
import numpy as np
import cv2 as cv
import time
import math





#Sets up arena with obstacles
def setup():

    global arena
    
    #Colors
    white = (255, 255, 255)
    gray = (177, 177, 177)
    darkGray = (104, 104, 104)
    
#     #Draw Radial Clearance
#     for x in range(0, 600):

#         for y in range(0, 200):
        
#             if checkClearance(x, y, 4):
#                 arena[y, x] = darkGray
    
#     #Draw Obstacle Borders
#     for x in range(0, 600):

#         for y in range(0, 200):
        
#             if checkBorder(x, y):
#                 arena[y, x] = gray
    
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
    if (x - 400) * (x - 400) + (y - 90) * (y - 90) <= 2500:
        return True
    
    #Pentagon (Left Half)
#     if x >= 235 and x <= 300:
        
#         if (y >= (-38/65)*x + (2930/13)) and (y <= (38/65)*x + (320/13)):
#             return True
    
#     #Pentagon (Right Half)
#     if x >= 300 and x <= 366:
        
#         if (y >= (38/65)*x + (-1630/13)) and (y <= (-38/65)*x + (4880/13)):
#             return True
    
#     #Triangle
#     if x >= 460 and x <= 510:
        
#         if (y >= 2*x - 895) and (y <= -2*x + 1145):
#             return True
        
    return False
  
#Checks to see if a point is within the border of an obstacle
def checkBorder(x, y):
    
    triHeight = int(round(5/math.cos(math.radians(63.4))))
    hexHeight = int(round(5/math.cos(math.radians(30.3))))
    
    #Both Rectangles
    if x >= 100 - 5 and x <= 150 + 5:
        
        if y < 100 + 5 or y >= 150 - 5:
            return True
    
    #Pentagon (Left Half)
    if x >= 235 - 5 and x <= 300:
        
        if (y >= (-38/65)*x + (2930/13) - hexHeight) and (y <= (38/65)*x + (320/13) + hexHeight):
            return True
    
    #Pentagon (Right Half)
    if x >= 300 and x <= 366 + 5:
        
        if (y >= (38/65)*x + (-1630/13) - hexHeight) and (y <= (-38/65)*x + (4880/13) + hexHeight):
            return True
    
    #Triangle
    if x >= 460 - 5 and x <= 510 + 5:
        
        if (y >= 2*x - 895 - triHeight) and (y <= -2*x + 1145 + triHeight) and (y >= 25 - 5) and (y <= 225 + 5):
            return True
        
    return False

#Checks to see if a point is within radial clearance of a border
def checkClearance(x, y, r):
    
    rr = r - 1
    
    if rr == 0:
        return False
    
    triHeight = int(round((5 + rr)/math.cos(math.radians(63.4))))
    hexHeight = int(round((5 + rr)/math.cos(math.radians(30.3))))
    
    #Both Rectangles
    if x >= 100 - 5 - rr and x <= 150 + 5 + rr:
        
        if y < 100 + 5 + rr or y >= 150 - 5 - rr:
            return True
    
    #Pentagon (Left Half)
    if x >= 235 - 5 - rr and x <= 300:
        
        if (y >= (-38/65)*x + (2930/13) - hexHeight) and (y <= (38/65)*x + (320/13) + hexHeight):
            return True
    
    #Pentagon (Right Half)
    if x >= 300 and x <= 366 + 5 + rr:
        
        if (y >= (38/65)*x + (-1630/13) - hexHeight) and (y <= (-38/65)*x + (4880/13) + hexHeight):
            return True
    
    #Triangle
    if x >= 460 - 5 - rr and x <= 510 + 5 + rr:
        
        if (y >= 2*x - 895 - triHeight) and (y <= -2*x + 1145 + triHeight) and (y >= 25 - 5 - rr) and (y <= 225 + 5 + rr):
            return True
        
    return False

#Checks to see if a point is valid (by checking obstacle, border, and clearance, as well as making sure the point is within arena bounds)
def checkValid(x, y, r):
    
    if checkObstacle(x, y):
        return False
    
    if checkBorder(x, y):
        return False
    
    if checkClearance(x, y, r):
        return False
    
    if (x < 0 or x >= 600 or y < 0 or y >= 250):
        return False
    
    return True





#Main Code
arena = np.zeros((200, 600, 3), dtype = "uint8")



setup()
cv.imshow("Arena", arena)
cv.waitKey()
cv.destroyAllWindows()


# In[ ]:




