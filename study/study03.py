#-*- coding: utf-8 -*-
import sys
from operator import eq 

class Lesson(object):
    def input(self):
        print 'type text !!!'
        a = sys.stdin.readline()
        sys.stdout.write("input value : %s" % a)
    
    def calcurate(self):
        
        while True:

            print u'그만하실려면 "q" 를 입력해주세요'
            print u'첫번째 수를 입력하세요'
            result=0
            first = sys.stdin.readline()
            first = first.strip()
            if first == 'q':
                break
            first = int(first)
            print u'연산자를 입력하세요 + - * / '
            operator = sys.stdin.readline()
            operator = operator.strip()
            if operator == 'q':
                break
            elif  operator != '+' and  operator != '+' and  operator != '*' and  operator != '/':
                print u'연산자를 잘못눌렀으므로 다시 시작합니다.'
                continue
            
            print u'두번째 수를 입력하세요'
            second = sys.stdin.readline()
            second = second.strip()
            if second == 'q':
                break
            second = int(second)
            if operator == '+':
                result=first+second
            elif operator == '-':
                result=first-second
            elif operator == '*':
                result=first*second
            elif operator == '/':
                result = first/second
            else:
                break

            print str(first)+operator+str(second)+' = '+ str(result)