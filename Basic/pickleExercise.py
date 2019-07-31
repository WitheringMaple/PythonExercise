# encoding: utf-8
'''
@author: YH
@time: 2019/7/31 11:00
'''

import pickle
a_dict = {'da':111,2:[23,1,4],'23':{1:2,'d':'sad'}}

# file = open('pickle_example.pickle','wb')
# pickle.dump(a_dict,file)
# file.close()
with open('pickle_example.pickle','rb') as file:
#file = open('pickle_example.pickle','rb')
    a_dict1 = pickle.load(file)
#file.close()
print(a_dict1)