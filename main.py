# /usr/bin/python
# -*- coding: utf-8; py-indent-offset:4 -*-

import sys, fitz
import os
import time
 
def pyMuPDF_fitz(pdfPath, imagePath):
    fname, ext = os.path.splitext(os.path.basename(pdfPath))
    if(ext != '.pdf'):
        raise Exception("file extendtions is not .pdf, current is ", ext)
    startTime_pdf2img = time.time()#开始时间
    print("imagePath="+imagePath)
    pdfDoc = fitz.open(pdfPath)
    for pg in range(pdfDoc.pageCount):
        text = page.getText() #获取pdf txt内容
        page = pdfDoc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
        # 此处若是不做设置，默认图片大小为：792X612, dpi=96
        zoom_x = 1.33333333 #(1.33333333-->1056x816)   (2-->1584x1224)
        zoom_y = 1.33333333
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pix = page.getPixmap(matrix=mat, alpha=False)
        outpath = '{0}/{1}/{2:03d}.png'.format(imagePath, fname, pg)
        if not os.path.exists(outpath):#判断存放图片的文件夹是否存在
            os.makedirs(outpath) # 若图片文件夹不存在就创建
        pix.writePNG(outpath)#将图片写入指定的文件夹内
    endTime_pdf2img = time.time()#结束时间
    print('pdf2img时间=',(endTime_pdf2img - startTime_pdf2img))

def main():
    pdfPath = './files/life.pdf'
    imagePath = './files/image'
    # pyMuPDF_fitz(pdfPath, imagePath)
    # images(imagePath)
    getbase(imagePath)


def eachbook(fname):
    efnames = []
    for root, dirs, files in os.walk(fname):
        for efname in files:
            fullname = os.path.join(root, efname)
            efnames.append(fullname)
    return sorted(efnames) # , reverse=True

def getbase(images_path):
    books = []
    for root, dirs, files in os.walk(images_path):
        for name in dirs:
            # fname = os.path.join(root, name)
            books.append(name)
            # print(name, fname)
    return books

def images(images_path):
    # abspth = os.path.abspath(images_path)
    for root, dirs, files in os.walk(images_path):
        for name in dirs:
            fname = os.path.join(root, name)
            bookname = os.path.basename(fname) #文件名
            ebfiles = eachbook(fname)
            print(fname)
    pass

if __name__ == "__main__":
    main()