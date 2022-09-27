from PIL import Image
Image1 = Image.open('example.jpg') 
Image2 = Image.open('example1.jpg')
# Image1.show()
# print(Image1.size)
# print(Image1.filename)
# print(Image1.format_description)
# x=200
# y=200
# w=864*0.7
# h=1080*0.5
# cropimage=Image1.crop((x,y,w,h))
# cropimage.show()
# Image2.show()
# Image2.paste(im=cropimage,box=(0,0))
# Image2.show()
# Image1.show()
# d=Image1.resize((2560,2560))
# d.show()
e=Image1.rotate(90)
e.show()
e.putalpha(50)
e.show()