import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../').replace('\\', '/'))
from utils.generator_util import random_int
from user_agent import user_agent_list

from frame import *
 
agent = '%s' % user_agent_list[random_int(len(user_agent_list)-1)]
 
if __name__ == '__main__':
    print agent
    LogIn()
    
    
