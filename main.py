#!/usr/bin/env python3

import requests
import json
import pyexiv2


def download(havenid, api_key=None):
    if api_key is None:
        url = "https://wallhaven.cc/api/v1/w/{0}".format(havenid)
    else:
        url = "https://wallhaven.cc/api/v1/w/{0}?apikey={1}".format(havenid, api_key)
    data = json.loads(requests.get(url).content)["data"]
    path = data["path"]
    frmt = path[::-1][:path[::-1].find('.')][::-1]
    filepath = "wallhaven-{0}.{1}".format(havenid, frmt)

    img = open(filepath, 'wb')
    img.write(requests.get(path).content)
    img.close()

    img = pyexiv2.Image(filepath)
    dic = img.read_iptc()
    dic["Iptc.Application2.Keywords"] = []
    for tag in data["tags"]:
        dic["Iptc.Application2.Keywords"].append(tag["name"])
    img.modify_iptc(dic)
