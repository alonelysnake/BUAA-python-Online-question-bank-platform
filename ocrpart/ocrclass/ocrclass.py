from paddleocr import PaddleOCR,draw_ocr
import glob
import os
import json

class Paddleocr:
    def __init__(
        self,
        img_path=None,
        img_type='jpg'
    ):
        self.img_path = img_path
        self.type = img_type
    def get_result(self):
        ocr = PaddleOCR(use_angle_cls=True, lang='ch')
        all_img = sorted(glob.glob(os.path.join(self.img_path, '*.' + self.type)))
        res = []
        for img in all_img:
            result = ocr.ocr(img, cls=True)
            all_str = ''
            flag = [False for i in range(4)]
            for j in range(len(result)):
                character = result[j][1][0]
                if character == 'A':
                    flag[0] = True
                    cnt = 1
                elif character == 'B':
                    flag[1] = True
                    cnt = 2
                elif character == 'C':
                    flag[2] = True
                    cnt = 3
                elif character == 'D':
                    flag[3] = True
                    cnt = 4
                else:
                    all_str += character + ' '
            res.append(all_str)
        return res