import ssl
import datetime
ssl._create_default_https_context = ssl._create_unverified_context
#With Python 2.7.9 release the default HTTPS behaviour has changed, which is now to always verify the remote HTTPS certificate to which you are initiating a connection.
#In order to disable HTTPS certificate validation by default in Python versions 2.7.9 or above you could use the above snippet of code.
import mechanize
import time
users=["","","",""]
passwords=["","","",""]
for i in range(12):
    for j in range(len(users)) :
        
        br = mechanize.Browser()
        br.set_handle_robots(False)    # ignore robots
        br.set_handle_refresh(False)   # can sometimes hang without this

        br.open("https://10.100.56.55:8090/")
        br.select_form('frmHTTPClientLogin')
        name  = users[j]
        br.form['username'] = users[j]
        br.form['password'] = passwords[j]
        br.submit()
        info= br.response().read()
        #print info   --> to print the response information 
        if 'login limit' in info:
            pass
        if 'logged in' in info:
            print "  "
            print "Logged in to : " + str(name)
            print "  "
            print datetime.datetime.now()
            break
    time.sleep(1000)
