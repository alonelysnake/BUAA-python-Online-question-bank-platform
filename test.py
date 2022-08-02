from ocrpart.ocrclass import Paddleocr

img_path = 'E:/'
img_name = '1.jpg'
ocr = Paddleocr(img_path, img_name)
a = ocr.get_result()
print(a)
img_name = '2.jpg'
ocr.change_img(img_path, img_name)
a = ocr.get_result()
print(a)