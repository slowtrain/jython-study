#-*- coding: utf-8 -*-
from java.util import ArrayList

class Lesson(object):
    def array1(self):
        arr = ['a','b','c']
        arr.append('d')
        for ar in arr:
            print ar

        for number in range(len(arr)):
            print str(number)+' '+ arr[number]

    def array2(self):
        arr = ArrayList()
        arr.add('a')
        arr.add('b')
        arr.add('c')

        for ar in arr:
            print ar