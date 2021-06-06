#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# conda install pillow
import os, glob
import sys
from PIL import Image


def main():
    filepath_list = glob.glob(input_path + '/*.png') 
    for filepath in filepath_list:
        basename  = os.path.basename(filepath)
        save_filepath = out_path + '/' + basename [:-4] + '.jpg'
        img = Image.open(filepath)
        img = img.convert('RGB')
        img.save(save_filepath, "JPEG", quality=100)
        print(filepath, '->', save_filepath)
        if flag_delete_original_files:
            os.remove(filepath)
            print('delete', filepath)

if __name__ == '__main__':

    if len(sys.argv) == 2:

        # input_path = '../dataset/images'
        input_path = str(sys.argv[1])
        out_path = input_path
        flag_delete_original_files = False
        main()
    
    else:
        print("Please check the syntax")