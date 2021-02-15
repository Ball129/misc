import os
from glob import glob

import cv2

path = '/home/paparn/Downloads/raw'
dest = '/home/paparn/Downloads/rec'
x, y = 177, 236
w, h = 2185, 2835

for f_path in sorted(glob(path + '/*')):
    print(f_path)
    file_name = f_path.split('/')[-1]
    image = cv2.imread(f_path)
    start_point = (x, y)
    end_point = (w+x, h+y)
    color = (0, 0, 0)
    thickness = 10
    image = cv2.rectangle(image, start_point, end_point, color, thickness)
    cv2.imwrite(os.path.join(dest, file_name), image)

os.system(f'img2pdf {dest}/* -o {dest}/flickers_qr.pdf')
