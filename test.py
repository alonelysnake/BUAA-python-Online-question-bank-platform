from ocrpart.ocrclass import Paddleocr

img_path = 'E:/year2(summer)/python_little_semaster/bighw/ocrpart/ppocr_img/ch/'
img_name = '1.jpg'
ocr = Paddleocr(img_path, img_name)
a = ocr.get_result()
print(a)