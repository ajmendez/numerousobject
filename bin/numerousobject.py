#!/usr/bin/env python
'''

pip install splinter[zope.testbrowser]
pip install splinter[django]

'''




import os
import splinter
USERNAME, PASSWORD = open(os.path.expanduser('~/.limited/manything')).read().strip().split(' ')
browser_name = 'phantomjs'
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:37.0) Gecko/20100101 Firefox/37.0"
b = splinter.Browser(browser_name, user_agent=user_agent)
# b = splinter.Browser('zope.testbrowser', ignore_robots=True, user_agent=user_agent)
b.visit('https://manything.com/sign-in.html')
b.find_by_id('username').first.fill(USERNAME)
b.find_by_id('password').first.fill(PASSWORD)
b.find_by_id('signin-btn').first.click()




import os
import splinter
USERNAME, PASSWORD = open(os.path.expanduser('~/.limited/numerousobject')).read().strip().split(' ')
browser_name = 'phantomjs'
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:37.0) Gecko/20100101 Firefox/37.0"
service_log_path='/Users/ajmendez/tmp/ghostdriver.log'
service_args=['--remote-debugger-port=9000']
b = splinter.Browser(browser_name, user_agent=user_agent, service_log_path=service_log_path, service_args=service_args)
# b = splinter.Browser('zope.testbrowser', ignore_robots=True, user_agent=user_agent)
b.visit('https://manything.com/sign-in.html')
b.find_by_id('username').first.fill(USERNAME)
b.find_by_id('password').first.fill(PASSWORD)
b.find_by_id('signin-btn').first.click()



import os
from selenium import webdriver
USERNAME, PASSWORD = open(os.path.expanduser('~/.limited/numerousobject')).read().strip().split(' ')
driver = webdriver.PhantomJS()
driver.get("https://manything.com/sign-in.html")
driver.find_element_by_id('username').send_keys(USERNAME)
driver.find_element_by_id('password').send_keys(PASSWORD)
driver.find_element_by_id('signin-btn').click()

# driver.find_element_by_id('search_form_input_homepage').send_keys("realpython")
# driver.find_element_by_id("search_button_homepage").click()
driver.quit()





import time

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

document.getElementById('noflash').setAttribute('visible', 'false')

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