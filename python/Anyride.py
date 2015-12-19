#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import os
#from twilio.rest import TwolioRestClient
#import subprocecess
import urllib2
import re
from bs4 import BeautifulSoup

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#returns 'None' if the key doesn't exist
#TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
#TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')

# Phone numbers
#my_number  ='+xxx'

dictionary = ["提供","DC"]
returnList = []
base_url = 'http://bbs.psucssa.com/'
destination_url = base_url+'index.php?p=/categories/拼车租车'
request = urllib2.Request(destination_url)
response = urllib2.urlopen(request).read()
soup = BeautifulSoup(response)
#A minor logic fault need to be fixed, right now, we are not requiring all the words in dictionary must be included
for target in soup.find_all('div',attrs={'class':"Title"}):
    if target.find("a"):
        tag = False
        for word in dictionary:
            p = re.compile(word)
            if not p.search(target.a.text.encode('utf-8')):
                tag = False
            else:
                tag = True
        if tag == True:
            returnList.append(target.a.text.encode('utf-8'))

for message in returnList:
    print message.encode('utf-8')
