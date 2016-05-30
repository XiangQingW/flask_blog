# -*- coding:utf-8 -*-
import os
import sys
from PIL import Image

class Untils:
    image_path = "./app/static/image/"


    def __init__(self):
        pass

    @classmethod
    def get_albums(cls):
        cover = []
        all_albums = os.listdir(cls.image_path)
        for album in all_albums:
            tmp_path = cls.image_path + album
            photos = os.listdir(tmp_path)
            try:
                idx = photos.index('1.jpg')
            except:
                idx = 0
            cover_name = photos[idx]
            cover_path = cls.find_and_resize_image(tmp_path, cover_name, photos)
            cover.append(cover_path)
        return cover

    @classmethod
    def find_and_resize_image(cls, path, cover_name, photos):
        resize_name = 'rezie' + cover_name
        src_path = ''.join([path, '/', cover_name])
        dst_path = ''.join([path, '/', resize_name])
        try:
            photos.index(resize_name)
        except:
            cls.resizeImg(ori_img = src_path, dst_img = dst_path, dst_w = 100, dst_h = 100, save_q = 20)
        return ''.join([path[5:], '/', resize_name])
        

    @classmethod
    def resizeImg(cls, **args):
        args_key = {'ori_img':'','dst_img':'','dst_w':'','dst_h':'','save_q':75}
        arg = {}
        for key in args_key:
            if key in args:
                arg[key] = args[key]
            
        im = Image.open(arg['ori_img'])
        ori_w,ori_h = im.size
        widthRatio = heightRatio = None
        ratio = 1
        if (ori_w and ori_w > arg['dst_w']) or (ori_h and ori_h > arg['dst_h']):
            if arg['dst_w'] and ori_w > arg['dst_w']:
                widthRatio = float(arg['dst_w']) / ori_w 
            if arg['dst_h'] and ori_h > arg['dst_h']:
                heightRatio = float(arg['dst_h']) / ori_h

            if widthRatio and heightRatio:
                if widthRatio < heightRatio:
                    ratio = widthRatio
                else:
                    ratio = heightRatio

        if widthRatio and not heightRatio:
            ratio = widthRatio
        if heightRatio and not widthRatio:
            ratio = heightRatio
            
            newWidth = int(ori_w * ratio)
            newHeight = int(ori_h * ratio)
        else:
            newWidth = ori_w
            newHeight = ori_h
            
        im.resize((newWidth,newHeight),Image.ANTIALIAS).save(arg['dst_img'],quality=arg['save_q'])


if __name__ == "__main__":
    src = '../static/image/album1/2.jpg'
    dst = '../static/image/album1/resie2.jpg'
    Untils.resizeImg(ori_img = src, dst_img = dst, dst_w = 100, dst_h = 100, save_q = 35)
