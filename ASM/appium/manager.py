__author__ = 'Alexis1'
import os


def set_appium_server(ip,port,chromedriver,bootstrap, selendroid, params):
    if params is None:
        params = ""
    return "appium --address " + ip + " -p " + port + " --chromedriver-port " + chromedriver + " --bootstrap-port " + \
           bootstrap + " --selendroid-port " + selendroid + " " + params


def start_appium_server(ip,port,chromedriver,bootstrap, selendroid, params):
    os.system(set_appium_server(ip, port, chromedriver, bootstrap, selendroid, params))

#start_appium_server("127.0.0.1", "4723", "9516", "4725", "8082", "--no-reset --local-timezone")
