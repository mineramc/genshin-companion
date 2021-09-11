import cv2
import pytesseract
import os
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import numpy as np

def detect_artifact(image_path):
    pytesseract.pytesseract.tesseract_cmd = os.getcwd() + '\\tesseract\\tesseract.exe'

    img = cv2.imread(image_path, 0)
    template = cv2.imread('artifact-template.png', 0)
    w, h = template.shape[::-1]
    method = eval('cv2.TM_SQDIFF')

    # Apply template Matching
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = min_loc
    crop_img = img[top_left[1]:top_left[1]+h, top_left[0]:top_left[0]+w]

    pil_img = Image.fromarray(cv2.cvtColor(crop_img, cv2.COLOR_BGR2RGB))
    sharpened1 = pil_img.filter(ImageFilter.SHARPEN)
    contrast = ImageEnhance.Contrast(sharpened1)
    pil_img = contrast.enhance(2)
    crop_img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

    cv2.imshow("cropped", crop_img)
    cv2.waitKey(0)

    d = pytesseract.image_to_data(crop_img, output_type=pytesseract.Output.DICT)
    print(d.keys())
    text = []
    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(float(d['conf'][i])) > 20:
            text.append(d['text'][i])
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            crop_img = cv2.rectangle(crop_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    print(text)
    cv2.imshow('img', crop_img)
    cv2.waitKey(0)


detect_artifact('test2.png')
detect_artifact('Main artifact Page.png')