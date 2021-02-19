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

fileIn = input("Arquivo de entrada: ")
fileOut = input("Arquivo de saida: ")
imageWidth = input("Largura da imagem: ")
imageHeight = input("Altura da imagem: ")

image = Image.open(fileIn)
pixels = image.load()

out_file = open(fileOut, "w")

for y in range(imageHeight):
    for x in range(imageWidth):
        out_file.write(toString(pixels[x,y]))
