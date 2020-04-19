from PIL import Image

read = 'coff.PNG'
write = 'logocoff.PNG'

image = Image.open(read)

# image.show()
# print(image.format) # Output: JPEG
#
# print(image.mode) # Output: RGB
#
# print(image.size) # Output: (193, 37)
#
# print(image.palette) # Output: None

new_image = image.resize((193, 37))
new_image.save(write)

print(new_image.size)
