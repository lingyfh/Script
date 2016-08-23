# -*- coding:utf-8 -*-

import realpath
import os
import time
from util import util

log_path = os.path.dirname(os.path.abspath(__file__))
log_path = str(log_path).replace('dnsinfo', 'log')

dns_all_info_file_name = log_path + '/dns_nslookup_allinfo.log'
dns_rs_info_file_name = log_path + '/dns_nslookup_rs_info.log'


def dns_info(domain=None):

    if domain is None:
        print 'domain is none'
        return

    current_time = time.time()

    dns_info_time = 'dns_info_time_' + str(current_time) + ' normal: ' + str(
        time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(current_time)))

    rs = os.popen('nslookup ' + domain)
    output_lines = rs.readlines()

    # 写入所有日志
    util.write_log_file(filename=dns_all_info_file_name, log_content=dns_info_time + '\n', lines=output_lines)

    # 写入dns结果日志
    if len(output_lines) > 1:
        util.write_log_file(filename=dns_rs_info_file_name, log_content=dns_info_time + ' | ', lines=output_lines[-2])
    else:
        temp_lines = output_lines
        temp_lines.insert(0, '-exception-start----------------------------\n')
        temp_lines.insert(1, dns_info_time + ' | \n')
        temp_lines.append('-exception-end-------------------------------\n')
        util.write_log_file(filename=dns_rs_info_file_name, lines=temp_lines)


if __name__ == '__main__':
    # dns_info('androidesk.com')
    pass

