# encoding: utf-8
'''
@author: YH
@time: 2019/7/31 10:47
'''

char_list = ['a','b','c','c','d','d']
sentence = 'Welcome Back to This Tutorial!'
#print(set(sentence))
print(type({1:2}))
unique_char = set(char_list)
unique_char.add('a')
# unique_char.clear()
# unique_char.remove('c')
# unique_char.discard('y')
# print(unique_char)

set1 = unique_char
set2 = {'a','e','i'}
print(set1)
print(set2)
print(unique_char.difference(set2))
print(unique_char.intersection(set2))