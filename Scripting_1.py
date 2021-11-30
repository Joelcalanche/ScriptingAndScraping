from PIL import Image, ImageFilter


# img = Image.open('C:/Users/calanche/Desktop/Zero_to_Mastery_Python_script/images/pikachu.jpg')

img = Image.open('./astro.jpg')


# filtered_img = img.filter(ImageFilter.BLUR)

# print(img.size)
# new_img = img.resize((400, 400))
img.thumbnail((400, 200)) # mantiene la relacion de aspecto

img.save('thumnail.jpg')
# filtered_img = img.convert('L')

# filtered_img.save("grey.png", 'png')

# crooked = filtered_img.rotate(90)
# crooked.save('grey.png', 'png')
# crooked.show()
# print(filtered_img.size)

# resize = filtered_img.resize((300, 300))
# resize.save('grey.png', 'png')
# print(resize.size)
# box = (100, 100B, 400, 400)
# region =filtered_img.crop(box)
# region.save("grey.png", 'png')