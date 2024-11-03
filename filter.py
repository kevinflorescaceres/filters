from PIL import Image, ImageFilter

path = input("Please provide the path to the image to filter: ")
before = Image.open(path)
after = before.filter(ImageFilter.FIND_EDGES)
after.save("out.bmp")