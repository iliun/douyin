import os,re
out = os.popen('adb devices')
for i in out.readlines():
    if 'List of devices attached' in i :
        pass
    else:
        udid = re.findall(r'(.*)\tdevice',i)
        print(udid)