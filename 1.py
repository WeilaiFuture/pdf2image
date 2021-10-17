# -*- coding: utf-8 -*-

from configparser import ConfigParser
import fitz
import re
import os

#读取配置文件
def config():
    cp = ConfigParser()
    cp.read('conf.ini',encoding='UTF-8')
    file_path = cp.get('path', 'file_path')
    dir_path = cp.get('path', 'dir_path')
    w = cp.get('size', 'width')
    h = cp.get('size', 'height')
    return file_path,dir_path,h,w

#file_path = r'C:\Users\94294\Desktop\Gaillot-2007-CdP-晚二叠有孔虫.pdf' # PDF 文件路径
#dir_path = r'C:\Users\94294\Desktop\test' # 存放图片的文件夹
def pdf2image1(path, pic_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    checkIM = r"image"
    pdf = fitz.open(path)
    lenXREF = pdf.xref_length()
    count = 1
    for i in range(1, lenXREF):
        text = pdf.extract_image(i)
        # print(text)
        isImage = re.search(checkIM, str(text))
        if not isImage:
            continue
        pix = fitz.Pixmap(pdf, i)
        if pix.height<int (h) or pix.width<int(w):
            continue   
        new_name = f"img_{count}.png"
        pix.writePNG(os.path.join(pic_path, new_name))
        count += 1
        pix = None
if not os.path.exists('config.ini'):
    conf = ConfigParser()
    conf.add_section('path')
    conf.add_section('size')
    conf.set('path', 'file_path','.pdf')
    conf.set('path', 'dir_path','out')
    conf.set('size', 'width','0')
    conf.set('size', 'height','0')
    with open('conf.ini', 'w') as fw:
        conf.write(fw)
file_path,dir_path,h,w=config()
pdf2image1(file_path, dir_path)
os.system("pause")