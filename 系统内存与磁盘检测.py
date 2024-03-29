# _*_coding:utf-8_*_

# 作者    ：dingcm
# 创建时间 ：2019/9/3 下午7:02
# 文件    ：系统内存与磁盘检测.py
import psutil

def memissue():
    print('内存信息：')
    mem = psutil.virtual_memory()
    # 单位换算为MB
    memtotal = mem.total/1024/1024
    memused = mem.used/1024/1024
    membaifen = str(mem.used/mem.total*100) + '%'

    print('%.2fMB' % memused)
    print('%.2fMB' % memtotal)
    print(membaifen)

def cuplist():
    print('磁盘信息：')
    disk = psutil.disk_partitions()
    diskuse = psutil.disk_usage('/')
    #单位换算为GB
    diskused = diskuse.used / 1024 / 1024 / 1024
    disktotal = diskuse.total / 1024 / 1024 / 1024
    diskbaifen = diskused / disktotal * 100
    print('%.2fGB' % diskused)
    print('%.2fGB' % disktotal)
    print('%.2f' % diskbaifen)

memissue()
print('*******************')
cuplist()