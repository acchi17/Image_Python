import sys
#pip3 install opencv-python
import cv2
import numpy
#sudo apt install python3-tk
#as tk: it means "define tkinter tk"
import tkinter as mytk
#It seems default installed on python3
from PIL import Image
#pip3 install Pillow (it needs on ubuntu, maybe)
from PIL import ImageTk

args = sys.argv

#argv[1]:Read file name
#Image file read mode is "BGR" mode by OpenCV
#Image data is treated as "ndarray" on python-opencv
cvimg_bgr = cv2.imread(args[1], 1)

#First  argument:window name
#Second argument:NumPy arrayargs[1]
#cv2.imshow(args[1], img)

#while True:
    #waitkey() argument:integer value of key
   #keycode = cv2.waitKey(0)
    #"27":ESC key
   #if keycode == 27:
       #break

#pip
from PIL import ImageTk
#cv2.destroyAllWindows()

#Define callback function
def mscallback(event):
    line = 'x:' + str(event.x) + ' ' + 'y:' + str(event.y)
    ent.delete(0, 20)
    ent.insert(0, line)


root = mytk.Tk() #Create & show a window
root.title(args[1])
root.geometry("450x450")

ent = mytk.Entry(width=12)
ent.place(x=0, y=0)
#ent.pack()

cvimg_rgb = cv2.cvtColor(cvimg_bgr, cv2.COLOR_BGR2RGB) #Convert BGR to RGB
image_pil = Image.fromarray(cvimg_rgb) #Convert RGB to PIL
image_tk  = ImageTk.PhotoImage(image_pil)

#Create a canvas in "root"
cvs = mytk.Canvas(root, width = 450, height = 450)
#Create rectangle on a canvas
#canvas.create_rectangle(0, 0, 800, 300, fill = 'green')

#Create image on the canvas
cvs.create_image(0, 0, image = image_tk, anchor=mytk.NW)
#Place image on the canvas
cvs.place(x=0, y=20)
#cvs.pack()

cvs.bind('<Motion>', mscallback)


#Show a canvas x=0,y=0:upper left max
#canvas.place(x=0, y=0)

root.mainloop()
