from sys import exit

import os
import cv2

import numpy as np



BASE_DIR = os.getcwd()
OUT_DIR = os.path.join(BASE_DIR, "output")
IN_DIR = os.path.join(BASE_DIR, "input")
TEMPLATE = "\nuint8_t <NAME>[32][19] = {"
THRESHOLDING = 200


if not os.path.exists(IN_DIR):
    os.makedirs(IN_DIR)
    exit()

if not os.path.exists(OUT_DIR):
    os.makedirs(OUT_DIR)
    

def in_pth(img_name: str) -> str:
    return os.path.join(IN_DIR, img_name)

def out_pth(img_name: str) -> str:
    return os.path.join(OUT_DIR, img_name)


if __name__ == '__main__':
    with open(out_pth('all.txt'), mode='w', encoding='utf-8') as out_f:
        for in_file in os.listdir(IN_DIR):
            if not in_file.endswith(".png"):
                continue
            
            name: str = in_file.replace('.png', '')
            with open(out_pth(name + '.txt'), mode='w', encoding='utf-8') as f:
                img = cv2.imread(in_pth(in_file), -1)
                img.astype(np.uint8)

                out = TEMPLATE.replace('<NAME>', name)

                for row in img:
                    out += '\n\t\t\t\t\t\t  {'
                    for pixel in row:
                        if pixel[3] >= THRESHOLDING:
                            out += '0xFF, '
                        else:
                            out += '0x00, '
                    out = out[:-2]
                    out += '},'
                
                out = out[:-1]
                out += '\n\t\t\t\t\t};'

                f.write(out)
            out_f.write(out+'\n')