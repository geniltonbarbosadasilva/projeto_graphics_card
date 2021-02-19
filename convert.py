from PIL import Image

def complete(s):
    if len(s) > 1:
        return s
    return "0" + s

def toString(number):
    r = complete(hex(number[0]).replace("0x", ""))
    g = complete(hex(number[1]).replace("0x", ""))
    b = complete(hex(number[2]).replace("0x", ""))
    
    return r + g + b + " "

image = Image.open("image.png")
pixels = image.load()

out_file = open("image", "w")

for y in range(32):
    for x in range(64):
        # print(toString(pixels[x,y]))
        out_file.write(toString(pixels[x,y]))
