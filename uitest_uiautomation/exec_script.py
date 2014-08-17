# -*- coding: utf-8 -*-
__author__ = 'dongdaqing'

import os,time,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/utils/")
import loggingmodule

class ExecScript(object):

    def __init__(self):

        #生成记录日志路径
        common_test_path = os.path.dirname(os.path.abspath(os.path.dirname("."))) + "/uitest_results"
        time_as_path = time.strftime('%Y%m%d%H%M%S',time.localtime())
        rootpath = os.path.join(common_test_path,time_as_path)
        if not os.path.exists(rootpath):
            os.mkdir(rootpath)
        running_file = os.path.join(rootpath,'running_record.txt')

        self.logger = loggingmodule.Logger('execscript',running_file)

    #在真机上执行脚本
    def runOnDevice(self):

        running_info = os.popen("./device_run_smoke_test.sh").read()
        self.logger.log(running_info)

    #在模拟器上执行脚本
    def runOnSimulator(self):

        running_info = os.popen("./simulator_run_smoke_test.sh")
        self.logger.log(running_info)

if __name__ == '__main__':

    exec_obj = ExecScript()
    exec_obj.runOnDevice()