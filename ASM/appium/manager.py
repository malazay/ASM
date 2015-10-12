__author__ = 'Alexis1'
import os
import urllib2
import socket
import json
import psutil
import sys
import subprocess
import platform
from threading import Thread




pid = None


def postpone(function):
    def decorator(*args, **kwargs):
        t = Thread(target = function, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()
    return decorator


def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)


def log_to_file(command):
    logfile = open('logfile', 'w')
    proc = subprocess.Popen([command], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in proc.stdout:
        sys.stdout.write(line)
        logfile.write(line)
    proc.wait()


def run_command_and_log(command, logfile):
    with open(os.getcwd() + "/dashboard/static/logs/" + logfile, 'w') as out:
        out.write('Starting the Appium Server with parameters: ' + command + '\n')
        out.flush()
        print subprocess.Popen(command, shell=True, universal_newlines=True, stderr=subprocess.STDOUT, stdout=out)


def set_appium_executable(node_path, appium_path):
    path = ""
    if node_path is not None:
        path += node_path + " "
    if appium_path is not None:
        path += appium_path
    return path

def set_appium_server(node_path, appium_path, ip, port, chromedriver, bootstrap, selendroid, reset, override, params, logfile):
    if params is None:
        params = ""
    if reset is "full":
        params += " --full-reset"
    elif reset is "no":
        params += " --no-reset"
    else:
        params += ""
    if override is True:
        params += " --session-override"
    return set_appium_executable(node_path, appium_path) + " --address " + ip + " -p " + port + " --chromedriver-port " + chromedriver + " --bootstrap-port " + \
           bootstrap + " --selendroid-port " + selendroid + " " + params + " --log " + os.getcwd() + \
           "\\dashboard\\static\\logs\\" + logfile + " --log-no-colors"


@postpone
def start_appium_server(node_path, appium_path, ip, port, chromedriver, bootstrap, selendroid, reset, override, params, logfile):
    command = set_appium_server(node_path, appium_path, ip, port, chromedriver, bootstrap, selendroid, reset, override, params, logfile)
    print command
    os.system(command)


def get_list_of_processes_pid(process_name):
    list_of_pids = []
    for process in psutil.process_iter():
        if process_name in str(process):
            list_of_pids.append(process.pid)
    return list_of_pids


def get_process_pid_by_port(process_name, port):
    process_list = get_list_of_processes_pid(process_name)
    process_pid = None
    for item in process_list:
        try:
            p = psutil.Process(int(item))
            connections = p.connections()
            if port in str(connections):
                print 'Process Node with port ' + port + ' PID is: ' + str(item)
                process_pid = item
                break
        except Exception as e:
            print "No process with name: '" + process_name + "' and port: '" + port + "' where found" + e
    return process_pid


def kill_process_on_port(process_name, port):
    pid = get_process_pid_by_port(process_name, port)
    print "Stopping process: '" + process_name + "' on port: " + str(port)
    p = psutil.Process(int(pid))
    p.terminate()
    print "process: '" + process_name + "' on port: " + str(port) + " was killed"


def get_node_pid_by_port(port):
    node_pid = get_process_pid_by_port("node", port)
    if node_pid is None:
        print "Server with port: " + str(port) + " is not running"
    return node_pid


@postpone
def stop_appium_server(port):
    print "Stopping Appium Server on port: " + str(port)
    kill_process_on_port("node", port)
    print "Appium Server stopped"


def check_server_status(ip, port):
    ip_address = ip
    if "0.0.0.0" in ip:
        try:
            ip_address = socket.gethostbyname(socket.gethostname())
        except Exception as e:
            print "Exception thrown: " + str(e) + ". Using localhost as hostname"
            ip_address = socket.gethostbyname('localhost')
    url = "http://"+ip_address+":"+port+"/wd/hub/status/"
    if get_node_pid_by_port(port) is not None:
        print("Checking status of server: " + url)
        try:
            server = urllib2.urlopen(url, None, 5)
            data = json.load(server)
            status = True
        except:
            status = False
            print "Server timed out... This means that the server is online but not working."
        print ("Server Running: " + str(status))
    else:
        status = False
    return status


def adb():
    devices = []
    proc = subprocess.Popen('adb devices', shell=True, stdout=subprocess.PIPE)
    for line in iter(proc.stdout.readline, ''):
        devices.append(line.strip())
    return devices


def reboot(name):
    command = "adb -s " + name + " reboot"
    os.system(command)


def adb_get_name(name):
    device_name = []
    command = "adb -s " + name + " shell getprop ro.product.model"
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    for line in iter(proc.stdout.readline, ''):
        device_name.append(line.strip())
    return device_name



def is_chromedriver_running(port):
    if get_process_pid_by_port("chromedriver", port) is None:
        return False
    else:
        return True


def kill_chromedriver(port):
    chromedriver_pid = get_process_pid_by_port("chromedriver", port)
    print "Stopping Chromedriver on port: " + str(port)
    p = psutil.Process(int(chromedriver_pid))
    p.terminate()
    print "Chromedriver stopped"


