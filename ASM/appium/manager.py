__author__ = 'Alexis1'
import os
import urllib2
import json


def set_appium_server(ip,port,chromedriver,bootstrap, selendroid, params):
    if params is None:
        params = ""
    return "appium --address " + ip + " -p " + port + " --chromedriver-port " + chromedriver + " --bootstrap-port " + \
           bootstrap + " --selendroid-port " + selendroid + " " + params


def start_appium_server(ip,port,chromedriver,bootstrap, selendroid, params):
    os.system(set_appium_server(ip, port, chromedriver, bootstrap, selendroid, params))


def check_server_status(ip, port):
    url = "http://"+ip+":"+port+"/wd/hub/status/"
    print("Checking status of server: " + url)
    server = urllib2.urlopen(url)
    try:
        data = json.load(server)
        status = True
    except:
        status = False
    print ("Server Running: " + str(status))
    return status


