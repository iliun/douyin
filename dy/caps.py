import os,time,re,random
import multiprocessing

import yaml
from appium import webdriver

devices_list = ['34f5aa6e','c126e881']

def appium_desired(udid,port):
    with open("./capsYaml.yaml",'r',encoding='utf-8') as file:
        data = yaml.load(file,Loader=yaml.FullLoader)
    desired_caps = {}
    desired_caps['platformName']=data['platformName']
    desired_caps['platformVersion']=str(data['platformVersion'])
    desired_caps['deviceName']=data['deviceName']
    desired_caps['udid']=udid
    dirname = os.path.abspath('./')
    app_path = os.path.join(dirname,data['app'])
    desired_caps['app']= app_path
    desired_caps['appActivity']=data['appActivity']
    desired_caps['appPackage']=data['appPackage']
    desired_caps['noReset']=data['noReset']
    desired_caps['unicodeKeyboard']=data['unicodeKeyboard']
    desired_caps['resetKeyboard']=data['resetKeyboard']
    desired_caps['ip']=data['ip']
    desired_caps['port']=port

    print('-----启动app-----')
    driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(port)+'/wd/hub',desired_caps)

    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']

    print(time.strftime('%Y-%m-%d%H:%M:%S'))

    time.sleep(7)

    for i in range(700):
        driver.swipe(x * 0.5, y * 0.9, x * 0.5, y * 0.1)
        print(i)
        time.sleep(random.randint(5, 7))
    print('-' * 20)
    for i in range(400):
        driver.swipe(x * 0.5, y * 0.1, x * 0.5, y * 0.9)
        print(300 - i)
        time.sleep(random.randint(5, 7))

    print(time.strftime('%Y-%m-%d%H:%M:%S'))

desired_process = []

for i in range(len(devices_list)):
    port = 4723 + 2 * i
    desired = multiprocessing.Process(target=appium_desired,args=(devices_list[i],port))
    desired_process.append(desired)

if __name__ == '__main__':
    for desired in desired_process :
        desired.start()
    for desired in desired_process:
        desired.join()
