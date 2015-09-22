__author__ = 'Alexis1'
import os
import urllib2
import json
import psutil

pid = None

def set_appium_server(ip,port,chromedriver,bootstrap, selendroid, params):
    if params is None:
        params = ""
    return "appium --address " + ip + " -p " + port + " --chromedriver-port " + chromedriver + " --bootstrap-port " + \
           bootstrap + " --selendroid-port " + selendroid + " " + params


def start_appium_server(ip,port,chromedriver,bootstrap, selendroid, params):
    os.system(set_appium_server(ip, port, chromedriver, bootstrap, selendroid, params))


def get_node_pid_list():
    return [item.split()[1] for item in os.popen('tasklist').read().splitlines()[4:] if 'node.exe' in item.split()]

def get_node_pid_by_port(port):
    pid_list = get_node_pid_list()
    node_pid = None
    for item in pid_list:
        try:
            p = psutil.Process(item)
            if port in p.connections():
                print 'Process Node with port ' + port + ' PID is: ' + str(item)
                node_pid = item
                break
        except:
            print('Server not running')
    if node_pid is not None:
        return node_pid





def check_server_status(ip, port):
    url = "http://"+ip+":"+port+"/wd/hub/status/"
    print("Checking status of server: " + url)
    try:
        server = urllib2.urlopen(url)
        data = json.load(server)
        status = True
    except:
        status = False
    print ("Server Running: " + str(status))
    return status


