from paddleocr import PaddleOCR,draw_ocr
import glob
import os
import json

class Paddleocr:
    def __init__(
        self,
        img_path=None,
        img_name='1.jpg'
    ):
        self.img = img_path + img_name
    
    def get_object(self, res_list):
        all_str = ''
        for i in res_list:
            if i == 'A' or i == 'B' or i == 'C' or i == 'D':
                continue
            else:
                all_str += i + ' '
        return all_str
    
    def get_subject(self, res_list):
        all_str = ''
        for i in res_list:
            all_str += i + ' '
        return all_str

    def get_result(self):
        ocr = PaddleOCR(use_angle_cls=True, lang='ch')
        result = ocr.ocr(self.img, cls=True)
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