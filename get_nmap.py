import os


def get_nmap(options, ip):
    command = "nmap " + options + " " + ip
    process = os.popen(command)
    result = str(process.read())
    return result
