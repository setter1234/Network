from PIL import Image
class not_rgba(Exception):
    def __init__(self):
        super().__init__("it`s not rgba\n")


def remove_transperency(image):
    width,height = image.size
    result_image = Image.new(image.mode,image.size)
    pixel = image.load()
    newpixel = result_image.load()

    for w in range(width):
        for h in range(height):
            newpixel[w,h] = (pixel[w,h][0],pixel[w,h][1],pixel[w,h][2],255)
    return result_image

if __name__=="__main__":
    image = Image.open(input("input image name"))
    if(image.mode != "RGBA"):
        raise not_rgba
    result_image = remove_transperency(image)
    result_image.save(input("input storename"),"PNG")

