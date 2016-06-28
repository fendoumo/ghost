#-*- coding:utf-8 -*-
from ghost import Ghost
from ghost import Session
gh = Ghost()
sessin = Session(gh)
page , resource = sessin.open("http://abcabc.gq")
sessin.wait_for_page_loaded(10000)
print page.url
print page.http_status
print page.headers
print sessin.content

