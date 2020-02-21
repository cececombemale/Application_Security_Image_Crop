from PIL import Image
import sys
import math 
  
# get the file name  
try:
	name = sys.argv[1]
except:
	print("You did not enter the file name of the image you would like to crop, try again by rerunning the program")
	sys.exit(0)
#open the image
try:
	im = Image.open(name)
except: 
	print("The image could not be opened, try again with another format")
	sys.exit(0)
  
# Size of the image in pixels (size of orginal image) 
width, height = im.size 
print(width)
print(height)

#instantiate new variable for cropped image
new = 0

#if the image is wider than it is long, take pixels off the left and right
#side so that the width equals the height (square) and the image is centered
if width > height:
	dif = width-height
	dif = dif/2
	new = im.crop((dif,0, width-dif, height)) 

#if the image is longer than it is wide, take pixels off the top and bottom
#so that the height equals the width (square) and the image is centered
elif height > width:
	dif = height-width
	dif = dif/2
	new = im.crop((0, dif, width, height-dif)) 
  
# save new image 
new.save("new"+name)