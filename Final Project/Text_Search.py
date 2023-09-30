import cv2 as cv
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\aradi\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

AllImgs = []
WaterImg = []
SafeImg = []
files = 'Sample1.png', 'Sample2.png', 'Test2.png', 'proof.png', 'ice.png', 'pup.jpg', 'sky.jpg', 'flower.jpg', 'ring.png', 'trees.jpg'


def edit(img):
    blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
    canny = cv.Canny(blur, 125, 175)
    dialated = cv.dilate(canny, (3,3), iterations=3)
    return dialated

def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2,height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)
    return cv.warpAffine(img, rotMat, dimensions)

for name in files:
    img = cv.imread(name)
    AllImgs.append(img)
    # print(len(AllImgs))
    #Make image more legible
    fixed = edit(img)
    # cv.imshow('MyFile'+name, fixed)
    text = pytesseract.image_to_string(fixed)
    if text != '':
        WaterImg.append(fixed)
    else: 
        for x in range(361):
            rotated = rotate(fixed, x)
            text = pytesseract.image_to_string(rotated)
            if text != '':
                break
        SafeImg.append(rotated)
    print(len(AllImgs), len(WaterImg), len(SafeImg))
       
         
# cv.waitKey(0)
