class not_rgba(Exception):
    def __init__(self):
        super().__init__("it`s not rgba\n")

from PIL import Image
image = Image.open(input("input image name"))
if(image.mode != "RGBA"):
    raise not_rgba

width,height = image.size
result_image = Image.new(image.mode,image.size)
pixel = image.load()
newpixel = result_image.load()

for w in range(width):
    for h in range(height):
        newpixel[w,h] = (pixel[w,h][0],pixel[w,h][1],pixel[w,h][2],255)

result_image.show()


