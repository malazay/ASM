from threading import Thread
import os
import urllib2
import socket
import json
import psutil
import sys
import subprocess
import platform

__author__ = 'Alexis1'

pid = None


def postpone(function):
    def decorator(*args, **kwargs):
        t = Thread(target=function, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()
    return decorator


def get_os():
    uname = platform.uname()
    if "Windows" in uname:
        return "Win"
    if "Linux" in uname:
        return "Linux"
    if "Darwin" in uname:
        return "Mac"


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
    with open(set_log_folder() + logfile, 'w') as out:
        out.write('Starting command: ' + command + '\n')
        out.flush()
        print subprocess.Popen(command, shell=True, universal_newlines=True, stderr=subprocess.PIPE, stdout=out)


def set_appium_executable(node_path, appium_path):
    path = ""
    if node_path is not None:
        path += node_path + " "
    if appium_path is not None:
        path += appium_path
    return path


def set_log_folder():
    log_folder = os.getcwd()
    if "Win" in get_os():
        log_folder += "\\dashboard\\static\\logs\\"
    else:
        log_folder += "/dashboard/static/logs/"
    return log_folder


def set_appium_server(node_path, appium_path, ip, port, chromedriver, bootstrap, selendroid, reset, override, params,
                      logfile):
    cd_argument = ""
    bs_argument = ""
    sp_argument = ""
    if chromedriver is not None and type(chromedriver) is not 'NoneType' and len(chromedriver) > 0:
        cd_argument = " --chromedriver-port " + chromedriver
    if bootstrap is not None and type(bootstrap) is not 'NoneType' and len(bootstrap) > 0:
        bs_argument = " --bootstrap-port " + bootstrap
    if selendroid is not None and type(selendroid) is not 'NoneType' and len(selendroid) > 0:
        sp_argument = " --selendroid-port " + selendroid
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
    return set_appium_executable(node_path, appium_path) + " --address " + ip + " -p " + port + cd_argument + \
        bs_argument + sp_argument + " " + params + " --log " + set_log_folder() + logfile + " --log-no-colors"


@postpone
def start_appium_server(node_path, appium_path, ip, port, chromedriver, bootstrap, selendroid, reset, override, params,
                        logfile):
    command = set_appium_server(node_path, appium_path, ip, port, chromedriver, bootstrap, selendroid, reset, override,
                                params, logfile)
    os.system(command)


def get_list_of_processes_pid(process_name):
    list_of_pids = []
    for process in psutil.process_iter():
        if process_name in str(process.name()):
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
                print 'Process ' + process_name + ' with port ' + port + ' PID is: ' + str(item)
                process_pid = item
                break
        except Exception as e:
            print "No process with name: '" + str(process_name) + "' and port: '" + str(port) + "' was found"
    return process_pid


def kill_process_on_port(process_name, port):
    tries = 0
    pid = get_process_pid_by_port(process_name, port)
    if pid is not None:
        print "Stopping process: '" + process_name + "' on port: " + str(port)
        while get_process_pid_by_port(process_name, port) is not None and tries < 5:
            pid = get_process_pid_by_port(process_name, port)
            p = psutil.Process(int(pid))
            p.terminate()
            tries += 1
            if not "Win" in get_os():
                os.system("kill -9 " + pid)
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


def start_webkit_proxy(node_path, webkit_path, port, udid, params, logfile):
    if params is None:
        params = ""
    if node_path is None:
        node_path = ""
    else:
        node_path += ""
    command = node_path + webkit_path + " -c " + udid + ":" + port + " -d " + params
    print command
    run_command_and_log(command, logfile)


def check_webkit_status(port):
    print("Checking status of iOS WebKit Debug Proxy: " + port)
    status = get_process_pid_by_port('ios_webki', port) is not None
    if status is False:
        status = "ios_webki" in os.popen("lsof -i :"+port).read()
        print ("iOS WebKit Debug Proxy: " + str(status))
    return status


def kill_webkit_proxy(port):
    try:
        print ("Stopping iOS WebKit Debug Proxy on port: " + port)
        kill_process_on_port('ios_webkit_debug_proxy', port)
    except Exception as e:
        print ("WebKit proxy was not running")
    if check_webkit_status(port) and 'Windows' not in get_os():
        try:
            os.system("killall ios_webkit_debug_proxy")
            os.system("kill -9 " + port)
        except Exception as e:
            print ("WebKit proxy could not be stopped.")


def win_kill_process_by_port(port):
    pid = get_node_pid_by_port(port)
    os.system("taskkill /F /pid " + str(pid))
