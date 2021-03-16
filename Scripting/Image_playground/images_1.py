from PIL import Image, ImageFilter

img = Image.open('astro.jpg')
# img.show()
# img.ImageFilter()
img.thumbnail((400,400))
img.show()
print(img.size)