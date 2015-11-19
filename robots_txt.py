import urllib


def get_robots_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    req = urllib.urlopen(path + 'robots.txt', data=None)
    return req.read()
