# -*- coding:utf-8 -*-

import time
import os


# 写文件
def write_log_file(filename=str(time.time()) + '.log', mode='a', log_content='', lines=[]):
    if not os.path.exists(filename):
        print 'file not exists'
        
    log_file = open(filename, mode)
    log_file.write(log_content)
    log_file.writelines(lines)
    log_file.flush()
    log_file.close()
