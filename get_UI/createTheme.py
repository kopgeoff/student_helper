from PIL import Image
import numpy


# color is an array of 1*3, height and width is the size of application
def create_theme(height, width, color):
    array = numpy.array(numpy.zeros((height, width, 3)))
    for i in range(height):
        array[i][0] = [x + 50 - (100 / height * i) for x in color]
        for j in range(width):
            array[i][j] = array[i][0]
            for k in range(3):
                if array[i][j][k] < 0:
                    array[i][j][k] = 0
                elif array[i][j][k] > 255:
                    array[i][j][k] = 255
                else:
                    continue
    img = Image.fromarray(numpy.uint8(array)).convert("RGB")
    img.save("test.png")


create_theme(800, 800, [0, 162, 232])
