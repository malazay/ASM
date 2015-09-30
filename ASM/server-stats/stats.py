__author__ = 'Alexis1'
import psutil

def list_of_processes():
    return [proc.name() for proc in psutil.process_iter()]


