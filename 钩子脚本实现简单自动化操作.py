# _*_coding:utf-8_*_

# 作者    ：dingcm
# 创建时间 ：2019/9/3 下午7:07
# 文件    ：钩子脚本实现简单自动化操作.py
from flask import Flask,request,render_template,make_response,Response
import json,os,re,requests
import subprocess

app = Flask(__name__)
null = ""
cmd = "/var/www/html/ladmin-devel/"
@app.route('/test',methods=['POST'])
def hello():
    json_dict = json.loads(request.data)

    name = json_dict['event_name']
    ref = json_dict['ref'][11:]
    project = json_dict['project']['name']

    if name == 'push' and ref == 'master':
        os.chdir(cmd)
        s = subprocess.getoutput('sudo -u nginx composer install')
        return Response(s)
    else:
        return Response('none')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)