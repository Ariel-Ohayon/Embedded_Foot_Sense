# Python program to explain cv2.circle() method 
	
# importing cv2 
import cv2 
	
# path 
path = 'img.png'
	
# Reading an image in default mode 
image = cv2.imread(path) 
	
# Window name in which image is displayed 
window_name = 'Image'

# Center coordinates 
center1_coordinates = (181, 1225)
center2_coordinates = (307,876)
center3_coordinates = (136,843)
center4_coordinates = (133,410)
center5_coordinates = (248,413)
center6_coordinates = (380,400)
center7_coordinates = (170,170)
center8_coordinates = (300,170)

# Radius of circle 
radius = 30

# Red color in BGR 
color = (0, 0, 255) 

# Line thickness of -1 px 
thickness = -1

# Using cv2.circle() method 
# Draw a circle of red color of thickness -1 px 
image = cv2.circle(image, center1_coordinates, radius, color, thickness)
image = cv2.circle(image, center2_coordinates, radius, color, thickness)
image = cv2.circle(image, center3_coordinates, radius, color, thickness)
image = cv2.circle(image, center4_coordinates, radius, color, thickness)
image = cv2.circle(image, center5_coordinates, radius, color, thickness)
image = cv2.circle(image, center6_coordinates, radius, color, thickness)
image = cv2.circle(image, center7_coordinates, radius, color, thickness)
image = cv2.circle(image, center8_coordinates, radius, color, thickness)

# Displaying the image 
cv2.imshow(window_name, image) 
while True:
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Destroy all windows
cv2.destroyAllWindows()