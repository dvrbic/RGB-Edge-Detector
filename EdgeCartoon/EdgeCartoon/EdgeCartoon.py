import numpy as np
import cv2
import math


if __name__ == '__main__': 
   input_image = cv2.imread('mandrill.png',1) #Reads the input image
   output_image = input_image.copy()
   #Thresholding function
def threshfunc(in_img):
    img_out = np.copy(in_img)
    new_img = np.copy(in_img)
    vert_edge = np.array([[1,0,1],[0,0,0],[-1,0,-1]]) #Verticle array representing a Prewitt filter
    horz_edge = np.array([[-1,0,1],[-1,0,1],[-1,0,1]]) #Verticle array representing a Prewitt filter
    #Loops through the range of the image and moves the filter over each pixel for convolution
    for i in range(new_img.shape[0]):
        for j in range(in_img.shape[1]):
            #Checks to see if the filter mask is within range of the image
            #Does nothing if it is out of range
            if i<1 or i>(in_img.shape[0]-2) or j<1 or j>(in_img.shape[1]-2):
                pass
            else:
                vert = 0
                horz=0
                #Loops through the range of the 2d filter
                for x in range(-1,2):
                    for y in range(-1,2):
                        #Convolves the vertical and horizontal filters with the image
                        horz += new_img[i+x,j+y]*horz_edge[x+1,y+1]
                        vert += new_img[i+x,j+y]*vert_edge[x+1,y+1]
                #Finds the magnitude of the vertical and horizontal
                img_out[i,j] = int(math.sqrt(math.pow(horz,2)+math.pow(vert,2)))
                #Thresholding the output image, sets it to max value if its greater than a certain intensity, in this case 80
                if img_out[i,j] > 80:
                    img_out[i,j] = 255
                else:
                    #Threshold sets limit to 0 or black intensity of less than a certain arbitrary value, this case it is 80
                    img_out[i,j] = 0
    return img_out

def Edge_Dectection_func(in_img):
    new_img = np.copy(in_img)
    img_grey = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY) # line turns the colored rgb image to grayscale
    r = np.copy(img_grey) #Each of the 3 colors will have the same size as
    g = np.copy(img_grey)
    b = np.copy(img_grey) 
    #The loop gathers the intensity in the RBG image associated with each color and places them into an array, with each color having a coordinate
    for i in range (in_img.shape[0]):
        for j in range (in_img.shape[1]):
            r[i,j] = new_img[i,j][0]
            g[i,j] = new_img[i,j][1]
            b[i,j] = new_img[i,j][2] 
    #Passes each color array through the thresholding method
    r = threshfunc(r)
    g = threshfunc(g)
    b = threshfunc(b) 
    #Places each color into the image with their respective coordinate
    for x in range (in_img.shape[0]):
        for y in range (in_img.shape[1]):
            new_img[x,y][0]=r[x,y]
            new_img[x,y][1]=g[x,y]
            new_img[x,y][2]=b[x,y] 

    return new_img

if __name__ == '__main__': 
   output_image  = Edge_Dectection_func(input_image) #calls upon edge detection function
   cv2.imwrite('threshed_snow.png',output_image)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
