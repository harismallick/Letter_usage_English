# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt# plot, title, xlabel, ylabel, savefig, legend

file = open('English_words_list.txt')

words = []
for line in file:
    words.append(line.strip())
    
#print(len(words))

letter_count = {}
for word in words:
    for letter in word:
        letter_count[letter] = letter_count.get(letter, 0) + 1
        
print(letter_count)

sorted_count = {k:v for k,v in sorted(letter_count.items(), key=lambda item:item[1])}
print(sorted_count)
a = plt.figure()
ax = a.add_axes([0,0,1,1])
ax.bar(list(sorted_count.keys()), list(sorted_count.values()))
#plt.plot(list(sorted_count.keys()), list(sorted_count.values())) 
plt.title('English Letter Usage Statistics')
plt.ylabel('Occurrence in English Dictionary')
plt.xlabel('Letters')
#plt.show()
plt.savefig('English_letter_usage_statistics.jpg',bbox_inches='tight', dpi=150)
#plt.close()

# test = 'abrakadabra'
# count = {}
# for letter in test:
#     count[letter] = count.get(letter, 0) + 1
    
# print(count)