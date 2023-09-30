import cv2 as cv
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\aradi\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

img = cv.imread('Sample1.png')
# (height1, width1) = img.shape[:2]
# size = 640 #size must be multiple of 32. Haven't tested with smaller size which can increase speed but might decrease accuracy.
# (height2, width2) = (size, size)  
# img2 = cv.resize(img, (width2, height2)) 

blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 125, 175)
dialated = cv.dilate(canny, (3,3), iterations=3)

def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

# rotated = rotate(dialated, -45)


text = pytesseract.image_to_string(dialated)
if text == '':
    print("nada")
else:
    print("Watermark")
cv.imshow("Canny", dialated)
cv.waitKey(0)