import pandas as pd
import os
import glob
import numpy as np
import csv
import itertools
import time
import math
def type_maker(file,Archetypes):
    rr=list()
    with open(file , 'rt') as f:
        lines = f.read()
        #for types
        for i,type in enumerate(Archetypes):
            last= '<!--' if i == len(Archetypes)-1 else Archetypes[i+1]
            new_lines = lines[lines.find(type):lines.find(last)].split()
            for i in new_lines:
                if '.png' in i:
                    i=i.replace('![](' ,'')
                    i=i.replace(')','')
                    i=i.replace(',', '')
                    rr.append(i)
    return rr
def attr_maker(file,Attributes):
    res=[]
    attr_dict = {k:None for k in Attributes}
    with open(file, 'rt') as f:
        lines1 = f.read()
        # for attributes
        for i, attr in enumerate(Attributes):
            last = 'break' if i == len(Attributes) - 1 else Attributes[i + 1]
            new_lines = lines1[lines1.find(attr):lines1.find(last)].split()
            art=[]
            for i in new_lines:
                if '.png' in i:
                    i = i.replace('![](', '')
                    i = i.replace(')', '')
                    i = i.replace(',' , '')
                    art.append(i)
            res.append(art)
    return res



def main():
    tic=time.time()
    root_path = os.getcwd()+'/'
    file = root_path+'README.md'
    Attributes = ['Hat', 'Hair', 'Eyes', 'Blemishes', 'Nose', 'Ears', 'Mouth', 'Beard', 'Neck']
    Archetypes = ['Male', 'Female', 'Zombie', 'Ape', 'Alien']
    types=type_maker(file, Archetypes)
    atr=attr_maker(file, Attributes)
    res=[]
    res.append(types)
    for i in atr:
        res.append(i)
    header=['type']+Attributes
    data=itertools.zip_longest(*res,fillvalue='')
    with open(root_path+'selector_db.csv' , 'w' ,encoding="ISO-8859-1", newline='') as myfile:
        w = csv.writer(myfile)
        w.writerow(header)
        w.writerows(data)
    myfile.close()
    print('Counters:')
    total_bits=0
    for i,list in enumerate(res):
        bit_counter=math.ceil(math.log(len(list),2))
        total_bits+=bit_counter
        print("{} contains unique files :{} with min bits_req={}".format(header[i],len(list),bit_counter),end='\n')
    print('{} bits needed for image key generation'.format(total_bits))
    print('Done:{} sec'.format(time.time()-tic))
    



if __name__ == '__main__':
    main()
