from paddleocr import PaddleOCR,draw_ocr
# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `fr`, `german`, `korean`, `japan`
# to switch the language model in order.
ocr = PaddleOCR(use_angle_cls=True, lang='ch') # need to run only once to download and load model into memory
img_path = 'E:/year2(summer)/python_little_semaster/bighw/PaddleOCR-release-2.5/ppocr_img/ch/1.jpg'
result = ocr.ocr(img_path, cls=True)
i = 0
m = 0
bbox = {}
strs = {}
tmp = {}
for line in result:
    # print(line)
    bboxs = line[0]
    strings = line[1][0]
    if strings == 'A' or strings == 'B' or strings == 'C' or strings == 'D':
        continue
    bbox[i] = bboxs
    strs[i] = strings
    i += 1
# print(bbox)
# print(strs)
flag = [False for j in range(i)]
for j in range(i):
    for k in range(j, i):
        if flag[k] and flag[j]:
            continue
        bbox1_x1, bbox1_y1 = bbox[j][0][0], bbox[j][0][1]
        bbox1_x2, bbox1_y2 = bbox[j][2][0], bbox[j][2][1]
        bbox2_x1, bbox2_y1 = bbox[k][0][0], bbox[k][0][1]
        bbox2_x2, bbox2_y2 = bbox[k][2][0], bbox[k][2][1]
        y1min = min(bbox1_y1, bbox1_y2)
        y1max = max(bbox1_y1, bbox1_y2)
        y2min = min(bbox2_y1, bbox2_y2)
        y2max = max(bbox2_y1, bbox2_y2)
        x1min = min(bbox1_x1, bbox1_x2)
        x1max = max(bbox1_x1, bbox1_x2)
        x2min = min(bbox2_x1, bbox2_x2)
        x2max = max(bbox2_x1, bbox2_x2)
        if y1min < y2min and y1max > y2min:
            if x1min < x2min:
                string = strs[j] + strs[k]
                tmp[m] = string
            else:
                string = strs[k] + strs[j]
                tmp[m] = string
            m += 1
            flag[j] = flag[k] = True
        elif y1min > y2min and y1min < y2max:
            if x1min < x2min:
                string = strs[j] + strs[k]
                tmp[m] = string
            else:
                string = strs[k] + strs[j]
                tmp[m] = string
            m += 1
            flag[j] = flag[k] = True
        elif y1max < y2min and y2min - y1max < 60:
            string = strs[j] + strs[k]
            tmp[m] = string
            m += 1
            flag[j] = flag[k] = True
        elif y2max < y1min and y1min - y2max < 60:
            string = strs[k] + strs[j]
            tmp[m] = string
            m += 1
            flag[j] = flag[k] = True
for j in range(i):
    if not flag[j]:
        tmp[m] = strs[j]
        m += 1
ans = {}
j = 0
for i in range(m):
    if i == 0:
        continue
    if i == 1:
        ans['题目'] = tmp[i]
    else:
        ans[chr(ord('A') + i - 2)] = tmp[i]
print(ans)