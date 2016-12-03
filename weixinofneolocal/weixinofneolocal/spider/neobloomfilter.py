# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 09:30:50 2016

@author: root
"""
        
from pybloom import BloomFilter
import logging

def md5(str):
    import hashlib
    import types
    
    if types(str) is types.StringType:
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest
    else:
        return ""

class NeoBloomFilter:
    def __init__(self):
        self.bf = BloomFilter(capacity=10000, error_rate=0.0001)
        
    def isUrlExist(self, url):
        digest = md5(url)
        if digest == "":
            logging.error("md5() input is empty ")
            return True
        if digest in self.bf:
            return True
        else:
            self.bf.add(digest)
            return False


