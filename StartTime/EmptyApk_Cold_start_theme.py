#!/usr/bin/env python
#-*- coding : utf-8 -*-
import subprocess
import time
import optparse
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
#import  atx

cmd_install_num = 'adb -s '
cmd_install_in = ' install '
cmd_install_dev = ' install -r '
cmd_uninstall = ' uninstall '
package_name ="com.ksmobile.launcher"
cmd_install_num = 'adb -s '
cmd_install_in = ' install '
cmd_install_dev = ' install -r '
cmd_uninstall = ' uninstall '
rmfile = 'rm '
mkfile = 'echo nul >'
chmodfile = 'chmod 777 '
package_name = "com.ksmobile.launcher"
splashpath = os.getcwd()
casepath = os.getcwd()
adb_s = 'adb -s '
install_s = ' install '
uninstall_s = ' uninstall '
launcher = ' com.ksmobile.launcher '
start_launcher = ' shell am start com.ksmobile.launcher/.Launcher '
stop_launcher = ' shell am force-stop com.ksmobile.launcher '
back_back = ' shell input keyevent 4'
home_home = ' shell input keyevent 3'
adb_clear = ' shell pm clear com.ksmobile.launcher '
adb_push = ' push  '
adb_data_local_tmp = ' data/local/tmp '
run_jar_shell = '  shell uiautomator runtest Locker_and_Launcher.jar -c  '
Enter_the = 'Util.click_cm_setting'
judge_screensaverss = 'Util.judge_screensaver'
click_smart_screen_settings = 'Util.click_smart_screen_settings'
click_smart_screen_con_ads = 'Util.click_Smart_Scree'
click_smart_screen_con_ads2 = 'Util.click_Smart_Scree2'
click_savescreen_con_ads = 'Util.savescreen'
click_savescreen_con_ads2 = 'Util.savescreen2'
adb_jar = casepath + '/Locker_and_Launcher.jar'
Destroy_the_screenss = 'Util.Destroy_the_screen'
light_screens = 'Util.light_screen'
launcher = ' com.ksmobile.launcher '
start_launcher = ' shell am start com.ksmobile.launcher/.Launcher '
stop_launcher = ' shell am force-stop com.ksmobile.launcher '
cm_setting = ' shell am start -n com.ksmobile.launcher/.wallpaper.PersonalizationActivity'
setting_home = ' Util.splash_home_app '
ps_pid = '  shell  ps  |findstr "com.ksmobile.launcher"'

LAUNCHER_PKG_NAME = 'com.ksmobile.launcher'
LAUNCHER_MAIN_ACTIVITY = 'com.ksmobile.launcher/.wallpaper.PersonalizationActivity'
AM_THIS_TIME = 'ThisTime'
AM_TOTAL_TIME = 'TotalTime'
AM_WAIT_TIME = 'WaitTime'

def devicesConnectInfo():

    devicesId = []

    connResult = os.popen('adb devices').readlines()

    connDevicesInfo = connResult[1:len(connResult)-1]

    connDevicesNum = len(connDevicesInfo)


    if connDevicesNum > 0 :
        for i  in range(connDevicesNum):
            address = connDevicesInfo[i].split('\t')[0]

            if address.find('.')<0:

                devicesId.append(address)

    return devicesId


def getapk():
    apkmap = []
    path=os.getcwd()
    for parent, dirnames, filenames in os.walk(path):
        for files in filenames:
            if files.endswith('.apk'):
                apkmap.append(parent+'/'+files)
    return apkmap
def install(devicesID, appmapnamepath, package_name):
    try:
        comma = cmd_install_num + devicesID + cmd_uninstall + package_name
        os.popen(comma)
        time.sleep(7)
    except Exception:
        print 'chu cuo le '

    commands = 'adb -s ' + devicesID + '  install  ' + '"%s"' % str(appmapnamepath)
    os.popen(commands)
    time.sleep(7)
def home_homes(devicesID):
    
    os.popen(adb_s + devicesID + home_home)

def setting_homes(devicesID):

    push_jar(devicesID)
    
    command = adb_s + devicesID + run_jar_shell + setting_home
    os.system(command)
def push_jar(devicesid):
    command = adb_s + devicesid + adb_push + adb_jar + adb_data_local_tmp
    os.system(command)
    time.sleep(2)
def start_activity(activiy,devicesID,g_dict):
    result = {}
    p = subprocess.Popen('adb -s '+devicesID + ' shell am start -W  {}'.format(activiy),shell=True,stdout=subprocess.PIPE)
    out,err = p.communicate()
    for line in out.splitlines():
        cmds = line.decode('utf-8').split(':')
        if len(cmds) == 2 and cmds[0] in g_dict.keys():
            result[cmds[0]] = cmds[1]
    return result

def del_splash(devicesID):
    print 'Skip the splash page'
    try:
        for i in range(4):
            os.popen(adb_s + devicesID + ' shell am force-stop com.ksmobile.launcher')
            time.sleep(5)
            os.popen(adb_s + devicesID + ' shell am start com.ksmobile.launcher/.Launcher')
            time.sleep(15)
        for i in range(10):
            os.popen(adb_s + devicesID + ' shell input keyevent 4')
            time.sleep(1)
        print 'Skip the splash page complete '
    except Exception:
        print 'Skip the splash page error'

def startActivity(devicesID):
    start_activity = os.popen(adb_s + devicesID + ' shell am start com.ksmobile.launcher/.Launcher').readlines()
    return start_activity

def start_cold_run():
    number = sys.argv[1]
    #number = 10
    packagepath = getapk()
    print packagepath
    devicesInfo = devicesConnectInfo()
    devicesnum = len(devicesInfo)
    if devicesnum > 0:
        devicesID = devicesInfo[0]
    #devicesID = '063288cc00605eee'
    for iitem in range(len(packagepath)):
        g_dict = {'ThisTime': [], 'TotalTime': [], 'WaitTime': []}
        print '-------------------------loop execution ' + str(number) + '----------------------'
        print '\n\n'
        packagenames = packagepath[iitem].split('/')
        filenames=packagenames[-1].split('.apk')
        print packagenames
        for i in range(int(number)):
            print '=====================' + devicesID + '====================='
            print 'In installation'
            install(devicesID, packagepath[iitem], package_name)
            time.sleep(7)
            home_homes(devicesID)
            time.sleep(2)
            setting_homes(devicesID)
            time.sleep(2)
            startActivity(devicesID)
            time.sleep(2)
            del_splash(devicesID)
            #print 'adb -s ' + devicesID + ' shell input keyevent 3'
            os.popen('adb -s ' + devicesID + ' shell input keyevent 3')
            print 'In startup'
            row = start_activity(LAUNCHER_MAIN_ACTIVITY,devicesID,g_dict)
            #print g_dict
            [g_dict[i].append(int(row[i])) for i in row.keys()]
            print(row)
            time.sleep(1)
            print '=====================' + 'end' + '====================='
            print '\n\n'
        df = pd.DataFrame(g_dict)
        df.to_csv(filenames[0]+'.csv')
        print(df)
        df['WaitTime'].plot(kind='bar')
        # plt.show()

if __name__ == '__main__':

    start_cold_run()
