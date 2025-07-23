# IMAGE STEGANOGRAPHY PROJECT USING LSB(LEAST SIGNIFICANT BIT)
    In this code what we are trying to achieve is hiding a text in plain sight by the manipulation of the LSB of each
    color channel(RGB)

## What actually happens in the code?
    ->We take the image and convert it into a 3D array (Row,column,Color channel)
    ->Next we find the length of the text and convert it into 16bit binary and store it as header in the starting pixels
        by changing LSBs
    ->After the header is filled,the secret message is converted into binary and again embedded into each pixel
    ->After the encryption we convert the array back into an image and save it as a png
    ->the main reason for using a png is because while sending a png there is no compression and hence no loss of data
    ->After the other party recieves the image they can use the decoder and decode the message

## How To use the program?
    ->Place the path of the image in the project folder
    ->Next run the Encoder code
    ->You will be prompted to write a secret message
    ->After typing the secret message a new png will be saved in project folder called "Modified_Image.png"
    ->this png can be sent through any communication channel
    ->After the other part recieves the code they will use the Decoder code with the Modified image in the folder
    ->The text will be shown to them after running the code

## How the code works
### Encoder:
    Basically what the encoders work is to embed the MSBs of the secret message into the LSBs of the pixels
    This is achieved by the following method:
#### Process
    ->First the image is converted into a 3D array(Row,coloumn,color channel) using numpy
    ->Next we move onto the text.Here we find the total length of the secret message and convert it into a 16bit format
    ->The main reason for converting it into 16 bits is because it can the text length can be between 0 and (2^16)-1
    ->Next we run a for loop from 0 to 15 and access each pixel and its 3 color channels and change its LSB to the 
    corresponding MSb
    ->Example: 16 is represented as 0000000010000000.So the LSB of first pixel's red channel is changed to 0 and 
    next blue channel  and green channel 0 and after this we move onto next pixel and continue until all bits are done
    ->This first 16 bits take about 6 pixels and is called the header
    ->Next we move onto the actual text which is converted into 8-bit ASCII binary and the same process is done starting
    from 6th pixel until all Bits are done.
    ->This array is then converted back into an image and saved as "Modified_Image.png".

### Decoder:
    The decoder is the script that reads the image and finds out the secret message by checking all the LSBs
    This is achieved in the following method:
#### Process
    ->First the image is converted into a 3D array(Row,coloumn,color channel) using numpy
    ->We run a for loop from 0 to 15 and check all the lsb and store it as a seperate string and convert it to an integer
    ->This loop reads the header file and finds out the length of the secret text.
    ->this acts as a delimiter 
    ->From the 6th pixel we start reading all LSBs and every 8bit,we convert the whole string into a character and store
        it in a seperate string which will hold the final message
    ->We continue until we reach the length of the text we found out using the header
    ->Finally the whole message is revealed.

## Important Notes
    -> Use .PNG format — don't use JPEG , it compresses and destroys hidden bits
    ->When sending via WhatsApp or similar apps:
        - Send the image as a document, not from the gallery
        - Or zip the image before sending

## Requirements:
    ->Install the following libraries:
        -pip install numpy
        -pip install pillow
