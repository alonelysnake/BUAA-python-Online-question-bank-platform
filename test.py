from ocrpart.ocrclass import Paddleocr

#pdf
img_dir = 'E:/year2(summer)/python_little_semaster/bighw/ocrpart/ppocr_img/ch/'
img_name = '1'
imgtype = 'pdf'
ocr = Paddleocr(img_dir, img_name, imgtype)
a = ocr.forward()
print(a)
#img
imgtype = 'jpg'
ocr.change_img(img_dir, img_name, imgtype)
a = ocr.forward()
print(a)