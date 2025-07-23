import numpy as np
from PIL import Image

im2 = Image.open("Modified_image.png").convert("RGB")
arr3 = np.array(im2)
size_of_secret_message_string=""
for i in range(16):         #Here we are taking 16 bits because we are reading the header with 16 bits of the length of secret message
    color_channel=i%3
    pixel_value=i//3
    Color_value = arr3[0, pixel_value, color_channel]
    if Color_value & 1==1:
        size_of_secret_message_string+="1"
    else:
        size_of_secret_message_string+="0"
size_of_secret_message= int(size_of_secret_message_string, 2)   #Converting the 16Bit ASCII binary back into an integer

secret_message = ""
secret_message_binary = ""
for i in range(size_of_secret_message):
    skipped_bits = 16
    color_channel = (i + skipped_bits) % 3
    pixel_value = (i + skipped_bits) // 3
    Color_value = arr3[0, pixel_value, color_channel]
    if (Color_value & 1) == 0:
        secret_message_binary += "0"
    else:
        secret_message_binary += "1"
    if len(secret_message_binary) == 8: #Here we are keeping 8 because almost every character is represented by a 7bits and the 8th bit is 0 and hence there we are skipping over it as it has no value
        Ascii_value = int(secret_message_binary, 2)
        secret_message+=(chr(Ascii_value))
        secret_message_binary = ""
print(secret_message)



