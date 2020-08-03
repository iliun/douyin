import subprocess
from time import ctime

def appium_start(host,port):
    bp = str(port+1)
    cmd = 'start /b appium -a' + str(host) +  '-p' + str(port) + '-bp' + bp
    print('%s at %s' %(cmd,ctime()))
    subprocess.Popen(cmd,shell=True,stdout=open('./'+str(port)+'.log','a'),stderr=subprocess.STDOUT)

if __name__ == '__main__':
    host='127.0.0.1'
    port=4723
    appium_start(host,port)


