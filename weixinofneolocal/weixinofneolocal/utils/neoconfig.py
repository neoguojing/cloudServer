# coding=utf-8
import json

class NeoConfig:

    def __init__(self):
        pass

    def loadFronJsonFile(self,filename):
        with open(filename,"r") as f:
            return json.load(f)
