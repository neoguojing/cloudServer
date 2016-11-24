import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../').replace('\\', '/'))
from utils.generator_util import random_int
from user_agent import user_agent_list
 
 
if __name__ == '__main__':
    print user_agent_list[random_int(len(user_agent_list)-1)]
    
