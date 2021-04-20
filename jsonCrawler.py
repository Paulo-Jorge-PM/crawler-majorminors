#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import ndjson
import time
from urllib.request import urlopen

#URL = input("URL to Crawl?\n")
#https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html

class jsonCrawler:

    def __init__(self, url=None):
        self.SAVE_DIR = "output/links/"
        self.BASE_URL = "https://arquivo.pt/noFrame/replay/"
        self.startFlow()

    def startFlow(self):
        self.url = self.getUrl()
        jsonLinks = self.getLinks(self.url)
        jsonLinks = self.prettyJson(jsonLinks)

        timestamp = time.time()
        fileName = self.url.split("/")[0]
        self.saveJSON(jsonLinks, fileName+"_"+str(timestamp)+".ndjson")
        self.saveLinks(self.linksFromJSON(jsonLinks), fileName+"_homepages_"+str(timestamp)+".txt")

        self.printJson(jsonLinks)
        self.startFlow()

    def getLinks(self, url):
        resource = urlopen("http://arquivo.pt/wayback/cdx?url="+url+"&output=json")
        #resource = urlopen("http://arquivo.pt/wayback/http://publico.pt")
        links = resource.read()
        return links

    def getText(self):
        resource = urlopen("http://arquivo.pt/wayback/cdx?url="+url+"&output=json")
        links = resource.read()
        return links

    def prettyJson(self, data):
        parsed = ndjson.loads(data)
        #pretty = ndjson.dumps(parsed, indent=4, sort_keys=True)
        #pretty = ndjson.dumps(parsed)
        return parsed

    def printJson(self, data):
        print(data)

    def saveJSON(self, data, fileName):
        #f = open("output/links/"+fileName+"_"+, "w")
        #f.write(data)
        #f.close()
        with open(self.SAVE_DIR+fileName, "w") as f:
            #ndjson.dump(data, f, ensure_ascii=False, indent=4)
            ndjson.dump(data, f)

    def saveLinks(self, data, fileName):
        with open(self.SAVE_DIR+fileName, "w") as f:
            for item in data:
                f.write("%s\n" % item)

    def linksFromJSON(self, json):
        linksList = []
        for row in json:
            link = self.BASE_URL + row["timestamp"] + "/" + row["url"]
            linksList.append(link)
            print("LINK ADDED: " + link)
        return linksList

    def getUrl(self):
        print("\n\n===========\nExemplos: publico.pt")
        url = input("\n===========\nURL to Crawl?\n>>>")
        return url


jsonCrawler()

#if __name__ == '__main__':
#    main = Crawler()
