# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 23:51:47 2022

@author: Haris.Mallick
"""

file = open('English_words_list.txt')

words = []
for line in file:
    words.append(line.strip())

scrambled = 'nees'#'freong' #'luinosocc'
x = sorted(scrambled)
print(x)
# test = 'luinosoccxyz'
# check = all(item in test for item in x)

# if check == True:
#     print('Success!')
# else:
#     print('This did not work')


candidates = []    
for word in words:
    y = sorted(word)
    check = all(item in x for item in y)
    
    if check == True:
        candidates.append(word)
        
#print(candidates)
second_list = []
for word in candidates:
    if len(word) == 5:
        second_list.append(word)
        
print(second_list)
    

