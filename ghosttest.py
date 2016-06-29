#-*- coding:utf-8 -*-
from ghost import Ghost
from ghost import Session
gh = Ghost()
sessin = Session(gh)
while True:
    try:
        page , resource = sessin.open("http://abcabc.gq")
        sessin.wait_for_page_loaded(10000)
    except:
        pass
    #print sessin.content
    try:
        page , resource = sessin.open("http://abcabc.gq")
        sessin.wait_for_page_loaded(10000)
    except:
        pass
    #print sessin.content
    try:
        page , resource = sessin.open("http://abcabc.gq/test.php")
        sessin.wait_for_page_loaded(10000)
    except:
        pass
    #print sessin.content
    try:
        page , resource = sessin.open("http://mxqabc.gq")
        sessin.wait_for_page_loaded(10000)
    except:
        pass
    #print sessin.content
    try:
        page , resource = sessin.open("http://mxqabc.gq/test.php")
        sessin.wait_for_page_loaded(10000)
    except:
        pass
    #print sessin.content
    try:
        page , resource = sessin.open("http://window.gq")
        sessin.wait_for_page_loaded(10000)
    except:
        pass
    #print sessin.content
    try:
        page , resource = sessin.open("http://window.gq/test.php")
        sessin.wait_for_page_loaded(10000)
    except:
        pass
    #print sessin.content

