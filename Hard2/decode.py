from PIL import Image

def decodeImage():

    image = Image.open('test.png')
    for color in image.getdata():
        print(chr(color[2]))


if __name__ == '__main__':
    decodeImage()
