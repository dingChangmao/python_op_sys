# _*_coding:utf-8_*_

# 作者    ：dingcm
# 创建时间 ：2019/9/3 下午7:08
# 文件    ：解析一组域名的ip地址.py

import dns.resolver
from collections import defaultdict
hosts = ['baidu.com','weibo.com']
s = defaultdict(list)
def query(hosts):
    for host in hosts:
        ip = dns.resolver.query(host,"A")
        for i in ip:
            s[host].append(i)

    return s

for i in query(hosts):

    print(i,s[i])