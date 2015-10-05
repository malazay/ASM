__author__ = 'Alexis1'
import psutil

def list_of_processes():
    return [proc.name() for proc in psutil.process_iter()]


def get_cpu_usage():
    return str(psutil.cpu_percent(interval=0))
