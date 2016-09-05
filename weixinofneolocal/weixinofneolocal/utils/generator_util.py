# -*- coding: utf-8 -*-

from random import Random
import string


def random_str(randomlength=15):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str
    
def random_int(max_num=100):
    random = Random()
    return random.randint(0, max_num)

def random_float(low,high):
    random = Random()
    return random.uniform(low, high)

def random_choice(plist=[]):
    random = Random()
    return random.choice(plist)
    
def random_vericode(randomlength=6):
    random = Random()
   
    return string.join(random.sample(['1','2','3','4','5','6','7','8','9','0'], randomlength)).replace(" ","")