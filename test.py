from ocrpart.ocrclass import Paddleocr

img_path = 'E:/year2(summer)/python_little_semaster/bighw/ocrpart/ppocr_img/ch'
img_type = 'jpg'
ocr = Paddleocr(img_path, img_type)
a = ocr.get_result()
print(a)