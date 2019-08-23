import base64

fileName = "C:\\temp\\base64.txt"
f = open(fileName, 'r')
imgstring = f.read()
imgdata = base64.b64decode(imgstring)

imageFileName = 'C:\\temp\\image.jpg'
with open(imageFileName, 'wb') as f:
    f.write(imgdata)

print("\nImage file " , imageFileName, "created.\n")

