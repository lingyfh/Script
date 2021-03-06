# coding=utf-8

from apscheduler.executors.pool import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
from apscheduler.schedulers.blocking import BlockingScheduler

from dnsinfo import dns_nslookup
from dnsinfo import dns_jiexifenxi_51240_com
from dnsinfo import dns_dns_ip3366_com
from dnsinfo import dns_aliyun

import logging
logging.basicConfig()

domain = 'androidesk.com'
domain_ip = '210.14.154.134'

domain = 'adesk.com'
domain_ip = '210.14.154.133'


def dns_nslookup_info():
    print 'dns info'
    dns_nslookup.dns_info(domain=domain)


def dns_jiexifenxi_info():
    dns_jiexifenxi_51240_com.dns_info(domain=domain, contains_value=domain_ip)
    

def dns_ip3366_info():
    dns_dns_ip3366_com.dns_info(domain=domain)


def dns_aliyun_info():
    dns_aliyun.dns_info(domain=domain)

executors = {
    'default': ThreadPoolExecutor(10),
    'processpool': ProcessPoolExecutor(3),
}

if __name__ == '__main__':
    sched = BlockingScheduler(executors)
    sched.add_job(dns_nslookup_info, 'interval', seconds=10, max_instances=10)
    sched.add_job(dns_jiexifenxi_info, 'interval', seconds=60, max_instances=10)
    sched.add_job(dns_ip3366_info, 'interval', seconds=50, max_instances=10)
    sched.add_job(dns_aliyun_info, 'interval', seconds=30, max_instances=10)
    sched.start()
