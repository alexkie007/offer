import re
from collections import OrderedDict


def get_url_msg(url):
    map = OrderedDict()
    if()
    map['protocol'] = re.match("([a-z][a-z0-9+\-.]*)://", url).group().split("://")[0]
    hostname = url.split("://")[1].split("/")[0].split(":")
    map['hostname'] = hostname[0]
    if len(hostname) > 1:
        port = hostname[1]
    else:
        port = ""
    map['port'] = port
    path = url.split("://")[1].split("/")[1]
    map['path'] = "/" + path + "/"
    parameters = url.split("://")
    map['parameters'] = ''
    query = url.split("?")
    if len(query) > 1:
        query = query[1].split("#")
        if len(query) > 1:
            query = query[0]
    else:
        query = ""
    map['query'] = query
    fragmen = url.split("#")[1]
    map['fragmen'] = fragmen
    result = []
    for key, value in map.items():
        string = key + "='" + value + "'"
        result.append(string)
    print(",".join(result))


url = input().strip()
# url = "https://www.google.com:80/search/?q=HTTP#page1"
get_url_msg(url)
# print(text)
