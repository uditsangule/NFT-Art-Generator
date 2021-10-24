import cv2
import os
import glob
import numpy as np
import pandas as pd
import random
import time
import itertools as it
def intersection(lst1, lst2):
    lst3 = [value for value in lst2 if value not in lst1]
    return lst3
class punk_generator():
    def __init__(self):
        self.data_root= '/media/udit/LENOVO_USB_HDD/DataSet_folder/cryptopunk-img_attribute/'
        self.dataset = self.data_root + 'punks.whitelabel-master/basic/'
        self.csv = self.data_root + 'punks.whitelabel-master/punks.csv'
        male_attribute_dict = {'hair': ['bandana','hat','hair','cap' , 'fedora', 'head' , 'hoodie','mohawk','spike' , 'beanie' , 'dorag','shaved'],
                          'eyes': ['glasses' , 'shades' , 'eyes' , 'vr' , 'eye'],
                          'face':['mole','spots'],
                          'cheeks':['cheeks'],
                          'nose':['nose'],
                          'other':['front',],
                          'mouth':['vape' , 'smile' , 'teeth' ,'cigarette','mask','pipe','mustache','handlebars'],
                          'neck':['chain','chinstrap'],
                          'ears':['earring'],
                          'beard':['beard' , 'frown' , 'goat','muttonchops']}
        female_attribute_dict = {'hair': ['bandana','blonde','hair','shaved','head','orangeside','pigtails','helmet','tiara'],
                          'eyes': ['glasses' , 'shades' , 'vr' , 'eye','goggles'],
                          'face':['mole','spots'],
                          'cheeks':['cheeks'],
                          'nose':['nose'],
                          'mouth':['vape' , 'smile','cigarette','mask','pipe','lipstick'],
                          'neck':['chain','choker'],
                          'ears':['earring']}

    def data_analysis(self):
        self.attr_m = os.listdir(self.dataset+'m')
        self.attr_f = os.listdir(self.dataset + 'f')
        self.types = [f for f in os.listdir(self.dataset) if f.endswith('.png')]
        print('m:{} f:{} type:{}'.format(len(self.attr_f),len(self.attr_m) , len(self.types)))
        print(self.types)
        #print(self.attr_f)
        #print(self.attr_m)
        print(intersection(self.attr_f,self.attr_m))

    def process_data(self):
        df = pd.DataFrame(columns = ['type' , 'head' , 'eyes' , 'ears' , 'mouth', 'neck' , 'other' , 'beard'])
        k=1


    def generate_punk(self , type , attribute):
        k=1

    def make_grid(self , punks_list):
        l=1


def main():
    max_punks = 200
    p = punk_generator()
    p.data_analysis()

if __name__ == '__main__':
    main()