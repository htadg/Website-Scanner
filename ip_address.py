import os


def get_ip_address(url):
    command = "nslookup " + url
    process = os.popen(command)
    result = str(process.read())
    data = result.split()
    ip_address = data[len(data)-1]
    return ip_address
