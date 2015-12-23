# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 13:23:47 2015

@author: Ekta
"""

import numpy as np

# Considering only 4*4 images
intensity_array = np.zeros((4,4));

print("Enter the intensity array : ")

for i in range(0,4): 
    for j in range(0,4):
        intensity_array[i,j] = float(input())


rows = intensity_array.shape[0];
cols = intensity_array.shape[1];

int_string = np.zeros((rows*cols));
idx = 0;

#Creating a string of all intensity values

for i in range(0,rows): 
    for j in range(0,cols):
        int_string[idx] = intensity_array[i,j];
        idx = idx+1
        

crs = "" ; # currently recognized sequence
curr = "" ; # current sequence

output = {}
out_idx = 0;

dict_val = {};
dict_idx = 0;

for i in range(0,255) :
    dict_val[str(i)] = i;
        
#next unused location
dict_idx = 256;

curr = int_string[0];

crs = str(int(curr));

for i in range(1,idx) :
    curr = int_string[i];
    
    t_str = crs + "-" + str(int(curr))
    
    #print("t_str is " + t_str)
    
    if t_str in dict_val :
        #print(t_str + " Already exists");
        crs = t_str;
    else:
        # if not found in the dictionary
    
        #print("Creating a new entry for the dictionary ")
        output[out_idx] = dict_val[crs]
        #print("Output " , + output[int(out_idx)])
        out_idx = out_idx + 1;
        crs = str(int(curr));
        
        # add the new entery to the dictionary
        dict_val[t_str] = dict_idx;
        dict_idx = dict_idx + 1
    

#Last entry will always be found in the dictionary
if crs in dict_val : 
    output[out_idx] = dict_val[crs]
    #print("Output " , + output[int(out_idx)])
    out_idx = out_idx + 1;
    
#printing the encoded output
print(output.values());
    