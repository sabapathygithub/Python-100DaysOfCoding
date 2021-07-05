from PIL import Image

im = Image.open(r'C:\\Users\\nambi\\Desktop\\Peppa Pig.png')
new_image = im.resize((600, 180))
new_image.save("test-200.png")
print("Done")