import cv2
from PIL import Image

image_path = 'cat.jpeg'
face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image = cv2.imread(image_path)
cat_face = face_cascade.detectMultiScale(image)


cat = Image.open(image_path)
glasses = Image.open('glasses.png')
cmiler = Image.open('2н2й.png')
cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")
cmiler = cmiler.convert("RGBA")
for (x, y, w, h) in cat_face:
    glasses = glasses.resize((w, int(h/3)))
    cat.paste(glasses, (x, int(y+h/4)), glasses)
    cmiler = cmiler.resize((w, int(h / 2)))
    cat.paste(cmiler, (x, int(y+h/2)), cmiler)
    cat.save("catZokylaramuCmehno.png")
    catZokylaramu = cv2.imread("catZokylaramuCmehno.png")
    cv2.imshow("Cat with glasses i cmiller", catZokylaramu)
    cv2.waitKey()