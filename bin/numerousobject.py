#!/usr/bin/env python

import os
import time
import splinter
from bs4 import BeautifulSoup
from datetime import datetime
USERNAME, PASSWORD = open(os.path.expanduser('~/.limited/numerousobject')).read().strip().split(' ')

os.environ['DISPLAY'] = ':99'

from setproctitle import setproctitle
setproctitle('numerousobject')



NOW = datetime.now()
DELAY = 3
BASEDIR = '/mnt/video/numerousobject'
# BASEDIR = '/Volumes/video/numerousobject'
PATTERN = BASEDIR+'/{0:%Y}.{0:%m}.{0:%d}/main_{0:%s}_{0:%Y}.{0:%m}.{0:%d}_{0:%H}_{0:%M}_{0:%S}.png'
OUTDIR = os.path.dirname(PATTERN.format(NOW))
if not os.path.exists(OUTDIR):
    os.makedirs(OUTDIR)



i = 0
lasturl = None
browser_name = 'firefox'
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:37.0) Gecko/20100101 Firefox/37.0"
# browser_name = 'phantomjs'

# b = splinter.Browser(browser_name, user_agent=user_agent)
with splinter.Browser(browser_name, user_agent=user_agent) as b:
    print 'Login...'
    b.visit('https://manything.com/sign-in.html')
    time.sleep(5)
    print b.url
    b.find_by_id('username').first.fill(USERNAME)
    b.find_by_id('password').first.fill(PASSWORD)
    b.find_by_id('signin-btn').first.click()
    print 'Start...'
    while i < 3600:
        print i,
        i += 1
        time.sleep(DELAY)
        b.execute_script("if ( !!ManyThing.liveStill ) { document.getElementById('stillsImage').setAttribute('debug', ManyThing.liveStill.image.src) }")
        try:
            now = datetime.now()
            url = b.find_by_id('stillsImage').first['debug']
            if url == lasturl:
                continue
            if url is not None:
                filename = PATTERN.format(datetime.now())
                outdir = os.path.dirname(filename)
                if not os.path.exists(outdir):
                    os.makedirs(outdir)
                
                os.system('wget -q -O {filename} {url}'.format(filename=filename, url=url))
                lasturl = url
        except Exception as e:
            print e
            raise
        
        
    
    

# b.execute_script("console.log(document.getElementById('stillsImage'))")
#
#
# '''
# // var element = document.createElement("p").createTextNode(out);
# // img.appendChild(element);
#
# http://stackoverflow.com/questions/26070834/how-to-fix-selenium-webdriverexception-the-browser-appears-to-have-exited-befor
# '''
#
#
# # b = splinter.Browser(browser_name, user_agent=user_agent)
# i = 0
# with splinter.Browser(browser_name, user_agent=user_agent) as b:
#     b.visit('https://manything.com/sign-in.html')
#     # b.screenshot('/mnt/video/manything/test.png')
#     print 'logging into system...'
#     b.find_by_id('username')[0].fill(USERNAME)
#     b.find_by_id('password')[0].fill(PASSWORD)
#     b.find_by_id('signin-btn')[0].click()
#     assert u.url == u'https://manything.com/manything/', Exception('Could not get to right URL')
#     time.sleep(DELAY)
#     print 'Starting...'
#     tmp = b.find_by_id('stillsImage')[0]
#     print b.evaluate_script("document.getElementById('stillsImage').toDataURL()")
#     # while True:
#     #     time.sleep(DELAY)
#     #     b.screenshot(PATTERN.format(datetime.now()))
#     #     print i,
#     #     i += 1
#
#
# # b.execute_script("document.getElementById('stillsImage').toDataURL()")