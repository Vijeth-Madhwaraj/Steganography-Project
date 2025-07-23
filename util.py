import  numpy as np
def String_to_Binary(text):
    return [int(bit) for char in text for bit in format(ord(char), '08b')]

def image_comparision(Original_Image,Modified_Image):
    arr_original = np.array(Original_Image)
    arr_modified = np.array(Modified_Image)
    diff = np.abs(arr_original.astype(int) - arr_modified.astype(int))
    total_diff = np.sum(diff)
    print("Total pixel difference:", total_diff)