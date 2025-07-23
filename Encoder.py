import numpy as np
from PIL import Image
from util import String_to_Binary, image_comparision
im = Image.open("Cat_image.jpeg").convert("RGB")

#Storage of pixel values in a 3D Array and Conversion of Secret text into binary and storing them in a 1D array

arr = np.array(im)#array is in the form(Row,column,color)
input_text=input("Enter a secret text: ")
array2=String_to_Binary(input_text)

#Implementing fixed length termination.This is where u first encode the length of the message as header and while decoding we read the first 16bits and convert it to the length of the secret message
length_of_array=len(array2)
size=[int(bit) for bit in format(length_of_array ,'016b')]  #Conversion of an integer into 16Bit ASCII form
for i, bit in enumerate(size):
    color_channel=i%3
    pixel_value=i//3
    Color_value = arr[0, pixel_value, color_channel]
    if bit == 0 and Color_value < 255 and Color_value%2!=0:
        arr[0, pixel_value, color_channel] = Color_value + 1
    elif bit == 1 and Color_value > 0 and  Color_value%2==0:
        arr[0, pixel_value, color_channel] = Color_value - 1

#Changing the LSB of required number of pixels (All three channels)

for i, bit in enumerate(array2): #Enumerate gives a tuple with (Index,element).Here i takes all the index and bit takes the index element
    skipped_bits=16
    color_channel=(i+skipped_bits)%3#The main reason we are finding remainder is that we have set separate color channels for different remainder(0->Red,1->Green,2->Blue)
    pixel_value=(i+skipped_bits)//3 #the main reason we are doing integer division here is that 3sets of numbers will share the same number as 0,1,2 will share number 0 and 3,4,5 will share 1 etc.
    Color_value = arr[0, pixel_value, color_channel]
    if bit == 0 and Color_value < 255 and Color_value%2!=0:
        arr[0, pixel_value, color_channel] = Color_value + 1
    elif bit == 1 and Color_value > 0 and  Color_value%2==0:
        arr[0, pixel_value, color_channel] = Color_value - 1

im_modified = Image.fromarray(arr)
im_modified.save("Modified_image.png")

image_comparision(im,im_modified)