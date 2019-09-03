# _*_coding:utf-8_*_

# 作者    ：dingcm
# 创建时间 ：2019/9/3 下午7:05
# 文件    ：查看网段里有多少ip地址.py
import IPy

ip = IPy.IP('172.16.0.0/26')

print(ip.len())
for i in ip:
    print(i)