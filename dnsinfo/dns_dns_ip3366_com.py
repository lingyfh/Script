# -*- coding:utf-8 -*-

import realpath
import os
import requests
import time
from util import util

log_path = os.path.dirname(os.path.abspath(__file__))
log_path = str(log_path).replace('dnsinfo', 'log')

log_file_name = log_path + '/dns_dns_ip3366_com.log'
log_err_file_name = log_path + '/dns_dns_ip3366_com.err'


def search_dns_info(domain=None):
    dns_info_url = 'http://dns.ip3366.com/Select.php'

    if domain is None:
        return ''

    '''
    223.5.5.5 阿里云公共dns
    114.114.114.114
    180.76.76.76 百度公共dns
    '''
    params = {
        'domain': domain + '*223.5.5.5|adesk.com*114.114.114.114|adesk.com*180.76.76.76',
    }
    response = requests.post(url=dns_info_url, data=params)
    return response.status_code, response.text


def dns_info(domain=None):

    if domain is None:
        print 'domain is none'

    current_time = time.time()

    dns_info_time = 'dns_info_time_' + str(current_time) + ' normal: ' + str(
        time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(current_time)))

    rs_code, rs_content = search_dns_info('adesk.com')
    if rs_code == 200:
        file_name = log_file_name
    else:
        file_name = log_err_file_name
    util.write_log_file(filename=file_name, log_content=dns_info_time + ' | ')
    util.write_log_file(filename=file_name, log_content=rs_content)


if __name__ == '__main__':
    print 'main'
    #dns_info('adesk.com')


