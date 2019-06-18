#-*- coding: utf-8 -*-

import urllib2

class Lesson(object):
    
    def url(self):
        res = urllib2.urlopen("https://www.naver.com")
        print res.read().decode("utf-8")
    