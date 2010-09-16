#!/usr/bin/env python
# coding:utf-8

"""
Created by ben on 2010/8/5 .
Copyright (c) 2010 http://sa3.org All rights reserved. 
"""
import os
DEBUG = True

#settings for google storage
gs_access_key_id =""
gs_secret_access_key=""
cname ="http://g.akira.us"
bucket_name = "g.akira.us"

#role
ROLE= {
    'B':['Banned','Banned User'],
    'M':['Member','Member User'],
    'A':['Administrator','Administrator'],
    'G':['Guest','Guest'],
}

#xFox Setting

class Setting():
    title = "Akira"
    description = u"Akira"
    key_words = u"Akira"
    
    domain = "http://xfoxforum.appspot.com"
    timedelta = 0.8
    version = "0.1.2"
    theme = "default"
    hubbub_hub_url ="http://pubsubhubbub.appspot.com/" 
    comment_pagesize=100
    
#OpenID Provider
OPENID = (
    ('Gmail','gmail.com'),
    ('MyOpenID','myopenid.com'),
)
if __name__=='__main__':
    pass