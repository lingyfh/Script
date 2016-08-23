# coding=utf-8

from apscheduler.executors.pool import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
from apscheduler.schedulers.blocking import BlockingScheduler

from dnsinfo import dns_nslookup
from dnsinfo import dns_jiexifenxi_51240_com

import logging
logging.basicConfig()

domain = 'androidesk.com'


def dns_nslookup_info():
    print 'dns info'
    dns_nslookup.dns_info(domain=domain)


def dns_jiexifenxi_info():
    dns_jiexifenxi_51240_com.dns_info(domain=domain, contains_value='210.14.154.134')


executors = {
    'default': ThreadPoolExecutor(10),
    'processpool': ProcessPoolExecutor(3),
}

if __name__ == '__main__':
    sched = BlockingScheduler(executors)
    sched.add_job(dns_nslookup_info, 'interval', seconds=10, max_instances=10)
    sched.add_job(dns_jiexifenxi_info, 'interval', seconds=60, max_instances=10)
    sched.start()
