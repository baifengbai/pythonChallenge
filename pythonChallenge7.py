"""
* Download the image
* Get pixel values of that gray strip
* Treat pixel value as ascii code and print the corresponding character
* Output: you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
"""

from PIL import Image

img = Image.open('oxygen.png')
cropped = img.crop((95/2, 95/2 - 1, 629, 95/2))

im_gray = a.convert('LA') # convert to grayscale
width, _ = im_gray.size

prev = None
for i in range(0, width):
    pixel = a.getpixel((i, 0))[0]
    if prev != pixel:
        print chr(pixel),
        prev = pixel

result = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print ''.join(map(lambda x: chr(x), result))
# OR
print ''.join([chr(i) for i in b])
