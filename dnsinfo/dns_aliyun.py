# -*- coding:utf-8 -*-
import json

import realpath
import os
import requests
import time
from util import util


log_path = os.path.dirname(os.path.abspath(__file__))
log_path = str(log_path).replace('dnsinfo', 'log')

log_file_name = log_path + '/dns_aliyun_com.log'
log_err_file_name = log_path + '/dns_aliyun_com.err.log'


def search_dns_info(domain=None):
    if domain is None:
        print 'domain is none'
        return -1, 'domain is none'

    dns_info_url = 'http://zijian.aliyun.com/detectApi/detectAll.json'
    params = {
        'domain': domain,
        'action': 'ResolveValueA'
    }
    response = requests.get(url=dns_info_url, params=params)
    return response.status_code, response.text


def dns_info(domain=None):
    if domain is None:
        print 'domain is none'

    current_time = time.time()

    dns_info_time = 'dns_info_time_' + str(current_time) + ' normal: ' + str(
        time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(current_time)))

    rs_code, rs_content = search_dns_info(domain)
    rs_content = rs_content.encode('utf-8')

    util.write_log_file(filename=log_file_name, log_content=dns_info_time + ' | ')
    if rs_code == 200:
        rs_json = json.loads(rs_content)
        if rs_json['success'] is True:
            rs_data = rs_json['module']['data']
            rs_ip = rs_data[0]['ip']
            # rs_location = rs_data[0]['location']
            util.write_log_file(filename=log_file_name, log_content=rs_ip + '\n')
        else:
            util.write_log_file(filename=log_err_file_name, log_content=dns_info_time + ' | ')
            util.write_log_file(filename=log_err_file_name, log_content=rs_content + '\n')
    else:
        util.write_log_file(filename=log_err_file_name, log_content=dns_info_time + ' | ')
        util.write_log_file(filename=log_err_file_name, log_content=rs_content + '\n')

if __name__ == '__main__':

    dns_info('androidesk.com')
    print 'main'