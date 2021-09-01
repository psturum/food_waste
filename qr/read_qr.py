import cv2 as cv

im = cv.imread('Vegetable.png')
im2 = cv.imread('Grains.png')


det = cv.QRCodeDetector()
retval, points, straight_qrcode = det.detectAndDecode(im)
print(retval)
retval1, points1, straight_qrcode1 = det.detectAndDecode(im2)
print(retval1)