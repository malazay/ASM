import sys

__author__ = 'Alexis1'
import psutil

UNKNOWN = -1
OK = 0
WARNING = 1
CRITICAL = 2


def list_of_processes():
    return [proc.name() for proc in psutil.process_iter()]


# get overall cpu use
def total_cpu():
    total_cpu_use = psutil.cpu_percent(interval=1, percpu=False)
    return total_cpu_use

# get per core cpu use
def percore_cpu():
    print("pidiendo datos")
    percore_cpu_use = []
    cpu_id = 0
    for cpu in psutil.cpu_percent(interval=1, percpu=True):
        array_line = str(cpu_id), cpu
        percore_cpu_use.append(array_line)
        cpu_id += 1
    return percore_cpu_use


def get_ram():
    mem = psutil.swap_memory()
    return mem
