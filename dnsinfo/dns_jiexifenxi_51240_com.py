# -*- coding:utf-8 -*-

import realpath
import os
import requests
import time
from util import util

log_path = os.path.dirname(os.path.abspath(__file__))
log_path = str(log_path).replace('dnsinfo', 'log')

log_file_name = log_path + '/dns_jiexifenxi.log'
log_err_file_name = log_path + '/dns_jiexifenxi.err.log'

def search_dns_info(domain=None):
    dns_info_url = 'http://jiexifenxi.51240.com/web_system/51240_com_www/system/file/jiexifenxi/get/'

    if domain is None:
        return ''

    params = {
        'ajaxtimestamp': int(time.time() * 1000),
        'q': domain,
        'type': 'a'
    }
    response = requests.get(url=dns_info_url, params=params, timeout=30)
    return response.status_code, response.text


def dns_info(domain=None, contains_value=None):
    if domain is None:
        print 'domain is none'
        return
    current_time = time.time()

    dns_info_time = 'dns_info_time_' + str(current_time) + ' normal: ' + str(
        time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(current_time)))

    rs_code, rs_content = search_dns_info(domain)
    rs_content = rs_content.encode('utf-8')

    if contains_value is not None and rs_content.__contains__(contains_value):
        file_name = log_file_name
    else:
        file_name = log_err_file_name
    util.write_log_file(filename=file_name, log_content=dns_info_time + '\n')
    util.write_log_file(filename=file_name, log_content=rs_content)
    util.write_log_file(filename=file_name, log_content='\n')
    util.write_log_file(filename=file_name, log_content='------------------------split------------------------\n')
    print 'rs__code = ', rs_code
    print 'file name = ', file_name

if __name__ == '__main__':
    #dns_info(domain='androidesk.com', contains_value='210.14.154.134')
    pass