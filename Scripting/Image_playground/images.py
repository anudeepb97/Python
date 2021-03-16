from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
print(img)
print(img.format)
print(img.size)
print(img.mode)
# print(dir(img)) # shows all the methods we can access
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('blur.png', 'png')

filtered_img2 = img.filter(ImageFilter.SMOOTH)
filtered_img2.save('smooth.png', 'png')

filtered_img3 = img.convert('L')
crooked = filtered_img3.rotate(90)
crooked.show()
cro_res = crooked.resize((300,300))
cro_res.show()
filtered_img3.save('grey.png','png')
filtered_img3.show()

box = (100, 100, 400, 400)
region = filtered_img3.crop(box)
region.show()
