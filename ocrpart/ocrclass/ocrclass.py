from paddleocr import PaddleOCR,draw_ocr
import glob
import os
import json
import fitz

class Paddleocr:
    def __init__(
        self,
        img_dir = None,
        img_name=None,
        img_type='jpg'
    ):
        self.type = img_type
        self.dir = img_dir
        self.img_path = img_dir + img_name + "." + img_type

    def change_img(self, img_dir, img_name, img_type):
        self.dir = img_dir
        self.img_path = img_dir + img_name + "." + img_type
        self.type = img_type
    
    def get_object(self, res_list):
        all_str = ''
        for i in res_list:
            tmp = i
            tmp = tmp.upper()
            if tmp == 'A' or tmp == 'B' or tmp == 'C' or tmp == 'D':
                continue
            else:
                all_str += i + ' '
        return all_str
    
    def get_subject(self, res_list):
        all_str = ''
        for i in res_list:
            all_str += i + ' '
        return all_str

    def get_result(self, result):
        res_list = []
        for j in range(len(result)):
            character = result[j][1][0]
            res_list.append(character)
        # 判断客观题or主观题
        if res_list.count('A') !=0 or res_list.count('B') !=0 or res_list.count('C') !=0 or res_list.count('D') !=0:
            res = self.get_object(res_list)
        else:
            res = self.get_subject(res_list)
        return res    

    def pdf2res(self, ocr):
        pdfdoc=fitz.open(self.img_path)
        res = []
        for pg in range(pdfdoc.page_count):
            page = pdfdoc[pg]
            rotate = int(0)
            # 每个尺寸的缩放系数为2，这将为我们生成分辨率提高四倍的图像。
            zoom_x = 2.0
            zoom_y =2.0
            trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
            pm = page.get_pixmap(matrix=trans, alpha=False)
            pic_path = self.dir + "temp.jpg"
            pm._writeIMG(pic_path, 1)
            result =ocr.ocr(pic_path, cls=True)
            tmp = self.get_result(result)
            res.append(tmp)
        return res

    def img2res(self, ocr):
        result = ocr.ocr(self.img_path, cls=True)
        res = []
        res.append(self.get_result(result))
        return res

    def forward(self):
        ocr = PaddleOCR(use_angle_cls=True, lang='ch')
        if self.type == "pdf":
            return self.pdf2res(ocr)
        else:
            return self.img2res(ocr)