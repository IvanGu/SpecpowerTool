# -*- coding: utf-8 -*-

#from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog,QApplication,QTableWidgetItem
from SpecpowerUI0_5 import Ui_Form
from CallCheckConfig import CheckConfigInterface
from CallResetTime import ResetOSDateTimeInterface
from CallClearSut import ClearSUTInterface  
from CallExit import ExitInterface
from CallHelp import HelpInterface
from CallQuestion import QuestionInterface
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt
from Get_Basicinfo import get_configFile_set_ver



import datetime
import sys
import os 
import linecache
import configparser 


class Form(QDialog, Ui_Form):

    def __init__(self, parent=None):

        super(Form, self).__init__(parent)
        self.setupUi(self)
        
        ####   Test Path  ####
        self.ccs_test_path = 'C:\Auto_Script'
        #self.ccs_ccsfolder_path = 'C:\Auto_Script\CCS'
        #self.ccs_cmfolder_path = 'C:\Auto_script\CM'
        #self.ccs_logfolder_path = 'C:\Auto_Script\LOG'
        #self.ccs_sutfolder_path = 'C:\Auto_Script\SUT'
        self.ccs_result_path = 'C:\Auto_Script\TestResult'
        self.ccs_result_config_path = 'C:\Auto_Script\TestResult\configinfo'
       # self.ccs_ipconfig_filepath = 'C:\Auto_Script\Config\IPLIST.txt'
        self.ccs_test_log_file = 'C:\Auto_Script\TestResult\\testlog.txt'
        self.ccs_reset_ostime_file = "C:\Auto_Script\TestResult\ostime.txt"

        ####   Check SUT Basicinfo ####
        self.sutbasicinfo_file = 'C:\Auto_Script\SUT\T_Basicinfo.bat'
        self.cmbasicinfo_file = 'C:\Auto_Script\CM\CM_config.bat'
        self.iplist_file = 'C:\Auto_Script\Config\IPLIST.txt'
        self.ccsip_file = 'C:\Auto_Script\SUT\T_del.bat'
        #self.ccs_runbasicinfo_script = 'run_Basiccheck_InterfaceCall.bat'
        
        ####   Reset SUT Os datetime ####
        self.ccs_resettimeformat = 'MM/dd/yyyy HH:mm'
        
        
        #### Run Main Program Script ####
        self.ccs_runspecpower_script = 'run_specpower_InterfaceCall.bat'
        self.ccs_runptu_script = 'run_PTU_InterfaceCall.bat'
        self.ccs_runbasiccheck_script = 'run_Basiccheck_InterfaceCall.bat'
        self.ccs_runclear_script = 'run_ClearPTU_InterfaceCall.bat'
        self.ccs_runclearPTU_script = 'run_PTU_InterfaceCall.bat'
        self.ccs_runautosetostime_script = 'run_Resettime_InterfaceCall.bat'

        ##### Upload Log  ######
        self.ccs_logset_prepath = "C:\Auto_script\result"
        self.ccs_logset_testmode_highperf = 'highperformance'
        self.ccs_logset_testmode_balance = 'balance'
        self.ccs_logset_testtemp_1 = '25C'
        self.ccs_logset_testtemp_2 = '30C'
        self.ccs_logset_testtemp_3 = '35C'
        self.ccs_logset_ptu = 'ptu'
        self.ccs_upload_path = 'C:\Auto_script\Script'
        self.ccs_upload_highper25C_script = 'run_ULH25C_InterfaceCall.bat'
        self.ccs_upload_highper30C_script = 'run_ULH30C_InterfaceCall.bat'
        self.ccs_upload_highper35C_script = 'run_ULH35C_InterfaceCall.bat'
        self.ccs_upload_highperPTU_script = 'run_ULHPTU_InterfaceCall.bat'
        self.ccs_upload_balance25C_script = 'run_ULB25C_InterfaceCall.bat'
        self.ccs_upload_balance30C_script = 'run_ULB30C_InterfaceCall.bat'
        self.ccs_upload_balance35C_script = 'run_ULB35C_InterfaceCall.bat'
        self.ccs_upload_balancePTU_script = 'run_ULBPTU_InterfaceCall.bat'

        ####  Data Analysis  #####
        self.ccs_dataanalysis_path = 'C:\Auto_script\Script'
        self.ccs_dataanalysis_highper25C_script = ''
        self.ccs_dataanalysis_highper30C_script = ''
        self.ccs_dataanalysis_highper35C_script = ''
        self.ccs_dataanalysis_highperPTU_script = ''
        self.ccs_dataanalysis_balance25C_script = ''
        self.ccs_dataanalysis_balance30C_script = ''
        self.ccs_dataanalysis_balance35C_script = ''
        self.ccs_dataanalysis_balancePTU_script = ''
        
        #### Monitor Flag File For Specpower ####
        self.flag_sut_basicinfo = '_Local_Basicinfo'
        self.flag_sut_runssjnodec = '_T_runssj_node_call_runssjnodec'
        self.flag_sut_fpga = '_T_fpga_run'
        self.flag_sut_iometer = '_T_run_io_meter'
        self.flag_sut_del = '_T_del'
        self.flag_ccs_autobaiscall = '_autoBasiccheck_sut'
        self.flag_ccs_autofpgacall = '_autoSpecPower_SUT_fpga'
        self.flag_ccs_autoiometercall = '_autoSpecPower_SUT_iometer'
        self.flag_ccs_runccscall = '\Run_Specpower_CCS_runccs'
        self.flag_ccs_rundirectorcall = '\Run_Specpower_CCS_rundirector'
        self.flag_ccs_runpowecall = '\Run_Specpower_CCS_runpower'
        self.flag_ccs_runtempcall = '\Run_Specpower_CCS_runtemp'
        self.flag_ccs_wcsgetfancall = '\Run_Specpower_CCS_Wcs_Get_Fan'
        self.flag_ccs_wcsgettempcall = '\Run_Specpower_CCS_Wcs_Get_Temp_ALL'
        self.flag_ccs_wcsgetpowercall = '\Run_Specpower_CCS_Wcs_Get_PSU'
        
        
        #### Monitor Flag File For PTU ####
        self.flag_ccs_runptu = 'Run_PTU'
        self.flag_ccs_ptu_callpredel = '_autoSpecPower_PTU_SUT_predel'
        self.flag_ccs_ptu_autocallptu = '_autoSpecPower_PTU_SUT_PTU'
        self.flag_ccs_setcmfan_100= '\CM_fan_100'       ###CM Script Path
        self.flag_ccs_setcmfan_auto = '\CM_fan_auto'   ###CM Script Path
        self.flag_ccs_setcmfan_auto_overtest = '\CM_fan_auto_aftertest'   ###CM Script Path
        self.flag_ccs_wcsgetfancall = '\Run_Specpower_CCS_Wcs_Get_Fan'
        self.flag_ccs_wcsgettempcall = '\Run_Specpower_CCS_Wcs_Get_Temp_ALL'
        self.flag_ccs_wcsgetpowercall = '\Run_Specpower_CCS_Wcs_Get_PSU'
        
        self.flag_ptu_sut_callPTUscript = '_autoSpecPower_PTU_SUT_PTU'
        self.flag_ptu_sut_callfpga = '_autoSpecPower_PTU_SUT_fpga'
        self.flag_ptu_sut_calliometer = '_autoSpecPower_PTU_SUT_iometer'
        self.flag_ptu_sut_calldel = '_autoSpecPower_PTU_SUT_predel'
        self.flag_ptu_sut_PTUscript = '_T_run_PTU'
        self.flag_ptu_sut_fpga = '_T_fpga_runptu'
        self.flag_ptu_sut_iometer = '_T_run_io_meter_ptu'
        self.flag_ptu_sut_del = '_autoSpecPower_PTU_SUT_predel'
        



        self.pB_1checkSUTconfig.clicked.connect(self.check_config)
        self.pB_2ResetSUTostime.clicked.connect(self.reset_os_datetime)
        self.pB_clear.clicked.connect(self.clear_sut)
        self.pB_exit.clicked.connect(self.exit_tool)
        self.pB_logupload.clicked.connect(self.log_upload)
        self.pB_monitor.clicked.connect(self.monitor_status)
        #self.pB_dataAnylysis.clicked.connect(self.data_analysis)
        self.pB_help.clicked.connect(self.help_tool)
        
        
        self.progressBar.setValue(0)
        cpldver = get_configFile_set_ver(self.sutbasicinfo_file,'set SUT_CPLD_Ver')
        self.L_cpldver.setText(cpldver)
        biosver = get_configFile_set_ver(self.sutbasicinfo_file,'set SUT_BIOS_Ver')
        self.L_biosver.setText(biosver)
        bmcver = get_configFile_set_ver(self.sutbasicinfo_file,'set SUT_BMC_Ver')
        self.L_bmcver.setText(bmcver)
        cputype = get_configFile_set_ver(self.sutbasicinfo_file,'set SUT_CPU_Type')
        self.L_cputype.setText(cputype)
        memtype = get_configFile_set_ver(self.sutbasicinfo_file,'set SUT_Memory_Type')
        self.L_memtype.setText(memtype)
        ssdtype = get_configFile_set_ver(self.sutbasicinfo_file,'set SUT_SSD_Type')
        self.L_ssdtype.setText(ssdtype)
        nvmetype = get_configFile_set_ver(self.sutbasicinfo_file,'set SUT_M2_Type')
        self.L_nvmetype.setText(nvmetype)
        cmip = get_configFile_set_ver(self.cmbasicinfo_file,'set cmip')
        self.L_cmip.setText(cmip)    
        cmbiosver = get_configFile_set_ver(self.cmbasicinfo_file,'set BIOSVersion')
        self.L_cm_biosver.setText(cmbiosver)
        cmpsufw = get_configFile_set_ver(self.cmbasicinfo_file,'set FirmwareRevision')
        self.L_cm_psufw.setText(cmpsufw)
        ccsip = get_configFile_set_ver(self.ccsip_file,'set serverip')
        self.L_ccsip.setText(ccsip)
        self.L_logPath.setText('Default')
#        self.L_reportpath.setText('Default')
#        self.lE_1checkresult.setStyleSheet("color:red") #setting lineedit color method
#        self.lE_1checkresult.setText('No Check')
#        self.L_1checkcfg.setText('No Check')
#        self.L_2setostime.setText('No Check')
        self.pB_start.clicked.connect(self.bt_start)
        self.sut_tablewidget_update()
        print('')
        print('----------------------------')
        print('Lenovo SpecPower Test Tool')
        print('Version: V1.0.0.0')
        print('Author:  Ivan Gu')
        print('Release date:2018-09-20')
        print('----------------------------')
#        print ('1234'+'\\'+'2345')

#        self.tW_SUT.setPalette(QPalette(Qt.red))
        #self.tW_SUT.item(1, 0).setBackground(Qt.green)   ### Set BackGround Color
        #self.tW_SUT.item(2, 0).setForeground(Qt.green)  ###Set Font Color
         
         
         
    def judge_radiobt_checked(self):
        
        self.check_status = ''
        tt_status = ''
        tt_temp_status = ''
        tm= ''
        
        if not self.rB_TT_sepc.isChecked() and not self.rB_TT_ptu.isChecked():  
            #print ('No module rdbt checked!')
            self.func_show_test_failinfo('No Test type mode button checked!!!' , 'Select one mode of test type')
            return False
        else:
            #print ('at least one module checked!')
            if self.rB_TT_ptu.isChecked():
                tt_status = 'p'
            #self.rB_TT_sepc.setChecked(False)
            #self.rB_TT_ptu.setChecked(True)
        if not self.rB_TT_25c.isChecked() and not self.rB_TT_30c.isChecked() and not self.rB_TT_35c.isChecked():
            #print ('No temp rdbt checked!')
            self.func_show_test_failinfo('No Test temperature mode button checked!!!' , 'Select one mode of test temperature')
            return False
        else:
            #print ('at least one temp checked!')
            if self.rB_TT_25c.isChecked():
                tt_temp_status = '25'
            if self.rB_TT_30c.isChecked():
                tt_temp_status = '30'
            if self.rB_TT_35c.isChecked():
                tt_temp_status = '35'
            #self.rB_TT_sepc.setChecked(False)
            #self.rB_TT_ptu.setChecked(True)
            
        if not self.rB_TM_highperf.isChecked() and not self.rB_TM_balance.isChecked(): 
            #print ('No perf rdbt checked!')
            self.func_show_test_failinfo('No Test performance button checked!!!' , 'Select one mode of test performance')
            return False
        else:
            #print ('at least one perf checked!')
            if self.rB_TM_highperf.isChecked():
                tm = 'h'
            if self.rB_TM_balance.isChecked(): 
                tm = 'b'
            #self.rB_TT_sepc.setChecked(False)
            #self.rB_TT_ptu.setChecked(True)   
        
        if tt_status == 'p':
            self.check_status = tm+tt_status
        else:
            self.check_status = tm+tt_temp_status 
            
#        print (tt_status)
#        print (tt_temp_status)
#        print (tm)
            
        return self.check_status
        
        
    
    
    def judge_lineed_content(self):
#        if self.L_1checkcfg.text() == 'Pass' and self.L_2setostime.text() == 'Pass' :
#            #print ('Line edit all Pass')
#            self.func_show_test_process('SUT config and os datetime reset' , 'Pass')
#			#return True
#        if not self.L_1checkcfg.text() == 'Pass':
#            #print ('1check not pass')
#            self.func_show_test_failinfo('Check SUT Configuration Not All Pass!!!' , 'Restart Check config program by click---1.Check SUT Config')
#            #return False
#        if not self.L_2setostime.text() == 'Pass':
#            #print ('2check not pass')
#            self.func_show_test_failinfo('Reset SUT Os date time Not All Pass!!!' , 'Restart reset os datetime program by click---2.Reset SUT OS Time')
            #return False
        #self.func_show_test_process('judge lineed content', 'Pass')
        pass
    
    def func_ccs_call_batscript(self, mainscript_path , mainscript):
        a= os.getcwd()
        #print (a)
        os.chdir(mainscript_path) #mainscript_path    'C:\Auto_script\SUT'
        self.func_show_test_process("Change Directory to %s"%mainscript_path , "Pass" )
        b = os.system(mainscript)   #mainscript  'a.bat'
        #print (b)
        if b == 0:
            #print ("excute main program script %s succussfully!!!"%mainscript)
            self.func_show_test_process("Execute Scirpt - %s - Successfully!"%mainscript, "Pass" )
        else:
            self.func_show_test_failinfo('Execute Scirpt - %s - Fail!!!'%mainscript , 'Please make sure path correctly')
#        self.func_show_test_process("ccs_call_batscript: %s"%mainscript , "Pass")   

###############    Set Table widget item color and backgroud color Fail  ####################
    def monitor_allsut_status(self):
#        newItem = QTableWidgetItem("松鼠")  
#        newItem.setBackgroundColor(QColor(0,60,10))  
#        newItem.setTextColor(QColor(200,111,100))          ######Don;t successfully by verifing to set tablewidget's item color and background color
#        self.tW_CCS.setItem(0, 0, newItem)        
#        if os.path.exists('a.bat') == True:
#            newItem = QTableWidgetItem("Pass")
#            self.tW_CCS.setItem(0, 0, newItem)
#            newItem = QTableWidgetItem("Pass")
#            self.tW_CCS.setItem(0, 1, newItem)
        pass
#############################################################################


####  Show Test Progress Info To ccs_test_log_file Variable ####
    def func_show_test_process(self, content , result):
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') #现在
        allinfo = "["+time+"]"+"   ["+content+"]   "+"["+result+"]"
        self.tB_testresult.append(allinfo)
#        if os.path.exists(self.ccs_test_log_path) == False:
#            os.mkdir(self.ccs_test_log_path)
        fp = open(self.ccs_test_log_file, "a")
        fp.write(allinfo+"\n")
        fp.close()
            
    
        
    def func_show_test_failinfo(self, content , resolution):
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') #现在
        allinfo = "["+time+"]"+"   ["+content+"]   "+"["+resolution+"]"
        self.tB_failinfo.append(allinfo)    
        
    
    def bt_start(self):
        # first judge if select radio button 
        self.tB_failinfo.setText("")
        
        question = QuestionInterface(self)
        if question.exec_():
            pass
        else:
            #print ('cancle exit')
            return 1
        #print (mode)
        mode = self.judge_radiobt_checked()
        if mode == False:
            #self.func_show_test_process('Test Mode Selection Fail', 'Fail')
            self.func_show_test_failinfo('Test Mode Selection Fail', 'Each Mode should select one')
            return 1
        if self.pB_start.text() == 'Start':
            self.pB_start.setText('Stop')
            self.ccs_logpath_setting(mode)
            if self.judge_lineed_content() == False:
                return 1
            self.start_count_time()
            if 'p' in mode:
                self.func_ccs_call_batscript( self.ccs_test_path, self.ccs_runptu_script) 
                self.func_show_test_process('CCS Run --- PTU --- Test', 'Running')
                self.func_show_test_process('PTU Test Running Please Waiting 1200s', 'Running')
                self.func_show_progressbar(1200)
            else:
                self.func_ccs_call_batscript(self.ccs_test_path, self.ccs_runspecpower_script) 
                self.func_show_test_process('CCS Run --- Specpower --- Test', 'Running')
                self.func_setbutton_status(self.pB_start, 0)
                self.func_show_test_process('CCS Connect SUT Java program Please Waiting 120s', 'Running')
                self.func_show_test_process('After 120s and check Java Program command interface make sure connect successfully', 'Running')
                self.func_show_test_process('Then Click --- Stop --- and --- Monitor --- for checking test result', 'Running')
                self.func_show_progressbar(120)
            
            
        elif self.pB_start.text() == 'Stop':
            #print ('Stop')
            self.pB_start.setText('Start')
            self.timer.stop()
            self.count_timer.stop()
            self.func_setbutton_status(self.pB_start, 1)
            #self.func_ccs_call_batscript( 'C:\Auto_script\SUT', 'run_specpower.bat') 
            # call shutdown progress script

        #run main script 
        #call back test status
#        print ('pass')
#        self.monitor_allsut_status()  #####################  put it in monitor function
        #self.set_sut_ostime()
        #self.judge_ccs_teststauts()  #####################  put it in monitor function
#        self.monitor_ccs_testresult('C:\Auto_script\TestResult', '\Run_Specpower_CCS_runccs.pass')

    def start_count_time(self):
        self.lcdN_testtime.display('0')
        self.timer = QTimer(self)
        #设置计时间隔并启动(1000ms == 1s)
        self.timer.start(1000)  
        #计时结束调用timeout_slot()方法,注意不要加（）
        self.timer.timeout.connect(self.timeout_slot) 
        self.hh = 0
        self.mm = 0
        self.ss = 0
    
        
    def timeout_slot(self):
#### Each gap 10s to get SUT Test Status ####
#        # 获取当前系统时间
#        time = QDateTime.currentDateTime()
#        # 时间显示格式
#        str = time.toString("hh:mm");
#        self.lcdN_testtime.display(str);
        self.ss += 1
        if self.ss > 59:
            self.mm += 1
            self.ss = 0
        if self.mm > 59:
            self.hh += 1
            self.mm = 0
        
        str1 = str(self.hh)+':'+str(self.mm)+':'+str(self.ss)
        
        self.lcdN_testtime.display(str1)
#
#    def set_sut_ostime(self):
#        time = self.dateTimeEdit.time()
#        timestr = time.toString("hh:mm")
#        print (timestr)
        
    def fresh_test_status(self):
        self.timer_status = QTimer(self)
        #设置计时间隔并启动(1000ms == 1s)
        self.timer_status.start(10000)  
        #计时结束调用timeout_slot()方法,注意不要加（）
        self.timer_status.timeout.connect(self.timeout_slot_status) 

######  Judge all SUT test Status by flag files ( need add ptu test flag file judgement)#################################
    def timeout_slot_status(self):
        ### func( path, flagfile, tablewidget line number)
        mode = self.judge_radiobt_checked()
        if mode == False:
            self.func_show_test_failinfo('Test Mode Selection Fail', 'Each Mode should select one')
            return 1
        if 'p' not in mode: 
            self.judge_ccs_teststauts()
            self.func_judge_allsut_configflag(self.ccs_result_config_path, self.flag_sut_basicinfo, 1)
            self.func_judge_allsut_configflag(self.ccs_result_path, self.flag_sut_runssjnodec, 2)
            self.func_judge_allsut_configflag(self.ccs_result_path, self.flag_sut_fpga, 3)
            self.func_judge_allsut_configflag(self.ccs_result_path, self.flag_sut_iometer, 4)
            self.func_judge_allsut_configflag(self.ccs_result_path, self.flag_sut_del, 5)
            self.func_judge_allsut_configflag(self.ccs_result_path, self.flag_ccs_autobaiscall , 6)
            self.func_judge_allsut_configflag(self.ccs_result_path, self.flag_ccs_autoiometercall, 7)
            self.func_judge_allsut_configflag(self.ccs_result_path, self.flag_ccs_autofpgacall, 8)
        else:
            #tw_ccs_horizontalHeader = ["PTU Main Program", "Call_Wcs_Get_Fan.bat","Call_Wcs_Get_temp.bat","Call_Wcs_Get_Psu.bat"," "," "," "]
            #tw_sut_horizontalHeader = ["IP Address","Basic Config Check","Call SSJ Script","FPGA Test","Io Meter Test","Call Pre-del","Call Basic Check Script","Call Io Meter Script","Call FPGA Script" ]
            #tw_sut_horizontalHeader = ["IP Address","PTU Test","FPGA Test","Io Meter Test","Call Pre-del","Call Io Meter Script","Call FPGA Script" ]
            #self.flag_ccs_runptu = 'Run_PTU'
#            self.flag_ccs_ptu_callpredel = '_autoSpecPower_PTU_SUT_predel'
#            self.flag_ccs_ptu_autocallptu = '_autoSpecPower_PTU_SUT_PTU'
#            self.flag_ccs_setcmfan_100= '\CM_fan_100'       ###CM Script Path
#            self.flag_ccs_setcmfan_auto = '\CM_fan_auto'   ###CM Script Path
#            self.flag_ccs_setcmfan_auto_overtest = '\CM_fan_auto_aftertest'   ###CM Script Path
#            self.flag_ccs_wcsgetfancall = '\Run_Specpower_CCS_Wcs_Get_Fan'
#            self.flag_ccs_wcsgettempcall = '\Run_Specpower_CCS_Wcs_Get_Temp_ALL'
#            self.flag_ccs_wcsgetpowercall = '\Run_Specpower_CCS_Wcs_Get_PSU'
#            
#            self.flag_ptu_sut_callPTUscript = '_autoSpecPower_PTU_SUT_PTU'
#            self.flag_ptu_sut_callfpga = '_autoSpecPower_PTU_SUT_fpga'
#            self.flag_ptu_sut_calliometer = '_autoSpecPower_PTU_SUT_iometer'
#            self.flag_ptu_sut_calldel = '_autoSpecPower_PTU_SUT_predel'
#            self.flag_ptu_sut_PTUscript = '_T_run_PTU'
#            self.flag_ptu_sut_fpga = '_T_fpga_runptu'
#            self.flag_ptu_sut_iometer = '_T_run_io_meter_ptu'
#            self.flag_ptu_sut_del = '_autoSpecPower_PTU_SUT_predel'
            self.judge_ccs_teststauts()
            self.func_judge_allsut_configflag(self.ccs_result_config_path, self.flag_ptu_sut_PTUscript, 1)
            self.func_judge_allsut_configflag(self.ccs_result_path, self.flag_ptu_sut_fpga, 2)
            self.func_judge_allsut_configflag(self.ccs_result_path, self.flag_ptu_sut_iometer, 3)
            self.func_judge_allsut_configflag(self.ccs_result_path, self.flag_ptu_sut_calldel, 4)
            self.func_judge_allsut_configflag(self.ccs_result_path, self.flag_ptu_sut_calliometer, 5)
            self.func_judge_allsut_configflag(self.ccs_result_path, self.flag_ptu_sut_callfpga , 6)
#            self.func_judge_allsut_configflag(self.ccs_result_path, self.flag_ptu_sut_callfpga, 7)
#            self.func_judge_allsut_configflag(self.ccs_result_path, self.flag_ccs_autofpgacall, 8)

#        self.func_judge_allsut_configflag('C:\Auto_script\TestResult\\', '_T_runssj_node_call_runssjnodec', 2)
#################################################################
        
######      Judge CCS test Status by flag files  ( need add ptu test flag file judgement)#################################
    def judge_ccs_teststauts(self):
        mode = self.judge_radiobt_checked()
        if mode == False:
            self.func_show_test_failinfo('Test Mode Selection Fail', 'Each Mode should select one')
            return 1
        if 'p' not in mode: 
            self.func_monitor_ccs_testresult(self.ccs_result_path, self.flag_ccs_runccscall, 0, 0)
            self.func_monitor_ccs_testresult(self.ccs_result_path, self.flag_ccs_rundirectorcall, 0, 1 )
            self.func_monitor_ccs_testresult(self.ccs_result_path, self.flag_ccs_runpowecall, 0, 2 )
            self.func_monitor_ccs_testresult(self.ccs_result_path, self.flag_ccs_runtempcall, 0, 3 )
            self.func_monitor_ccs_testresult(self.ccs_result_path, self.flag_ccs_wcsgetfancall, 0, 4 )
            self.func_monitor_ccs_testresult(self.ccs_result_path, self.flag_ccs_wcsgettempcall, 0, 5 )
            self.func_monitor_ccs_testresult(self.ccs_result_path, self.flag_ccs_wcsgetpowercall, 0, 6 )
            
        else:
#            self.flag_ccs_runptu = 'Run_PTU'
#            self.flag_ccs_ptu_callpredel = '_autoSpecPower_PTU_SUT_predel'
#            self.flag_ccs_ptu_autocallptu = '_autoSpecPower_PTU_SUT_PTU'
#            self.flag_ccs_setcmfan_100= '\CM_fan_100'       ###CM Script Path
#            self.flag_ccs_setcmfan_auto = '\CM_fan_auto'   ###CM Script Path
#            self.flag_ccs_setcmfan_auto_overtest = '\CM_fan_auto_aftertest'   ###CM Script Path
#            self.flag_ccs_wcsgetfancall = '\Run_Specpower_CCS_Wcs_Get_Fan'
#            self.flag_ccs_wcsgettempcall = '\Run_Specpower_CCS_Wcs_Get_Temp_ALL'
#            self.flag_ccs_wcsgetpowercall = '\Run_Specpower_CCS_Wcs_Get_PSU'
#            
#            self.flag_ptu_sut_callPTUscript = '_autoSpecPower_PTU_SUT_PTU'
#            self.flag_ptu_sut_callfpga = '_autoSpecPower_PTU_SUT_fpga'
#            self.flag_ptu_sut_calliometer = '_autoSpecPower_PTU_SUT_iometer'
#            self.flag_ptu_sut_calldel = '_autoSpecPower_PTU_SUT_predel'
#            self.flag_ptu_sut_PTUscript = '_T_run_PTU'
#            self.flag_ptu_sut_fpga = '_T_fpga_runptu'
#            self.flag_ptu_sut_iometer = '_T_run_io_meter_ptu'
#            self.flag_ptu_sut_del = '_autoSpecPower_PTU_SUT_predel'
            #tw_ccs_horizontalHeader = ["PTU Main Program", "Call_Wcs_Get_Fan.bat","Call_Wcs_Get_temp.bat","Call_Wcs_Get_Psu.bat"," "," "," "]
            self.func_monitor_ccs_testresult(self.ccs_result_path, self.flag_ccs_runptu, 0, 0)
            self.func_monitor_ccs_testresult(self.ccs_result_path, self.flag_ccs_wcsgetfancall, 0, 1 )
            self.func_monitor_ccs_testresult(self.ccs_result_path, self.flag_ccs_wcsgettempcall, 0, 2 )
            self.func_monitor_ccs_testresult(self.ccs_result_path, self.flag_ccs_wcsgetpowercall, 0, 3 )
            self.func_monitor_ccs_testresult(self.ccs_result_path, self.flag_ccs_wcsgetfancall, 0, 4 )
#################################################################        
        
        
        
    def func_monitor_ccs_testresult(self, path, flag, row, column):
        try:
            if os.path.exists(path) == True:
                if os.path.exists(path+'\\'+flag+".pass" ):
                    tw_item = QTableWidgetItem("Pass")
                    self.tW_CCS.setItem(row, column, tw_item)
                    self.tW_CCS.item(row, column).setBackground(Qt.green)
                elif os.path.exists(path+'\\'+flag+".fail"):
                    tw_item = QTableWidgetItem("Fail")
                    self.func_show_test_failinfo('CCS Test Item ---%s Fail'%flag, 'Check Script and Restart test program')
                    self.tW_CCS.setItem(row, column, tw_item)
                    self.tW_CCS.item(row, column).setBackground(Qt.red)
                else:
                    tw_item = QTableWidgetItem("Running")
                    self.tW_CCS.setItem(row, column, tw_item)
                    self.tW_CCS.item(row, column).setForeground(Qt.white)
                    self.tW_CCS.item(row, column).setBackground(Qt.blue)
                    
            else:
                    self.func_show_test_process('Cant not access info %s, please check path if is right'%path, 'Fail')
                    self.func_show_test_failinfo('Cant not access info %s, please check path if is right'%path, 'Check Script and Restart test program')
        except Exception as e :
            #print (e)
            self.func_show_test_process('Main Program Occur Exception error', 'Fail')
            self.func_show_test_failinfo('Error info --- %s --- , '%e, 'According to error info to fix')
            
            
    
            
            
    def func_get_allsut_ip(self):
        try:
            path = self.iplist_file
            if os.path.exists(path) == True:
                count = 0
                fp = open(path, "r", encoding='utf-8')
                while 1:
                    buffer = fp.read(8*1024*1024)
                    if not buffer:
                        break
                    count += buffer.count('\n')
                #print(count)
#                lines = fp.readlines()
                ip_array = []
                blade_ip_dict = {}
                for line in range(count):
                    
                    content = linecache.getline(path, (line+2))
                    if content == '':
                        continue
                    ip_array.append(content)
                    key = content.split('\t')[0]
                    value = content.split('\t')[1]
                    #print (key)
                    #print (value)
                    dict = {key : value}
                    blade_ip_dict.update(dict)
                    
                    
                #print (ip_array)
                #print ('over')
                #print (blade_ip_dict)
                fp.close()
                return blade_ip_dict

            else:
                self.func_show_test_process('Cant not access info %s, please check path if is right'%path, 'Fail')
                self.func_show_test_failinfo('Cant not access info %s, please check path if is right'%path, 'Check Script and Restart test program')
        except Exception as e :
            print (e)
            self.func_show_test_process('func_get_allsut_ip', 'Fail')
            self.func_show_test_failinfo('Error info --- %s --- , '%e, 'According to error info to fix')
            
            
            
            
            
    def sut_tablewidget_update(self):
        bladeip_dict = self.func_get_allsut_ip()
#        self.tW_SUT.setHorizontalHeaderLabels(['姓名','身高','体重'])  
        self.tW_SUT.setVerticalHeaderLabels(bladeip_dict.keys()) 
        iplist = [] 
        for ip in bladeip_dict.values():
            iplist.append(ip) 
            
        for i in range(len(iplist)):
            item = QTableWidgetItem(iplist[i])  
            self.tW_SUT.setItem(i, 0, item)
#            if item == 'Pass':
#                self.tW_SUT.item(i, 0).setBackground(Qt.green)
#                self.tW_SUT.setItem(i, 0, item)  
#            elif item == 'Fail':
#                self.tW_SUT.item(i, 0).setBackground(Qt.red)
#                self.tW_SUT.setItem(i, 0, item)
#            else:
#                self.tW_SUT.setItem(i, 0, item)
#                self.tW_SUT.item(i, 0).setBackground(Qt.yellow)
                
#            item.setTextAlignment(Qt.AlignHCenter |  Qt.AlignVCenter)

            
            

                
    def ccs_logpath_setting(self, mode):
        prepath = self.ccs_logset_prepath
        testmode_h = self.ccs_logset_testmode_highperf
        testmode_b = self.ccs_logset_testmode_balance
        testtemp_25 = self.ccs_logset_testtemp_1
        testtemp_30 = self.ccs_logset_testtemp_2
        testtemp_35 = self.ccs_logset_testtemp_3
        testtype_ptu = self.ccs_logset_ptu
        allpath = ''
        
        if mode == 'h25':
            allpath = prepath+'\\'+testmode_h+'\\'+testtemp_25+'\\'
        if mode == 'h30':
            allpath = prepath+'\\'+testmode_h+'\\'+testtemp_30+'\\'
        if mode == 'h35':
            allpath = prepath+'\\'+testmode_h+'\\'+testtemp_35+'\\'
        if mode == 'hp':
            allpath = prepath+'\\'+testmode_h+'\\'+testtype_ptu+'\\'

        if mode == 'b25':
            allpath = prepath+'\\'+testmode_b+'\\'+testtemp_25+'\\'
        if mode == 'b30':
            allpath = prepath+'\\'+testmode_b+'\\'+testtemp_30+'\\'
        if mode == 'b35':
            allpath = prepath+'\\'+testmode_b+'\\'+testtemp_35+'\\'
        if mode == 'bp':
            allpath = prepath+'\\'+testmode_b+'\\'+testtype_ptu+'\\'
        
        self.L_logPath.setText(allpath)
        
    
    def timer_event(self):
        if self.progress_step >= 100:
            self.count_timer.stop()
            return
        self.progress_step += 1
        self.progressBar.setValue(self.progress_step)
    
    def func_show_progressbar(self, seconds):
        self.count_timer = QTimer(self)
        self.count_timer.start(10*seconds)
        self.progress_step = 0
        self.count_timer.timeout.connect(self.timer_event)
        
    
    
    def check_config(self):
        self.tB_failinfo.setText("")
        self.progressBar.setValue(0)
        if self.pB_1checkSUTconfig.text() == '1.Check SUT Config':
            check_config_obj = CheckConfigInterface(self)
            if check_config_obj.exec_():
                self.func_ccs_call_batscript( self.ccs_test_path, self.ccs_runbasiccheck_script)  ### run_basicinfo.bat  self.ccs_runbasicinfo_script
                #self.progressBar.setValue(25)
                #judge final result and show it in label
                #self.func_judge_allsut_configflag('C:\Auto_script\TestResult\configinfo\\', '_Local_Basicinfo')
                #self.fresh_test_status()
                self.func_setbutton_status(self.pB_1checkSUTconfig, 0)
                self.start_count_time()
                self.pB_1checkSUTconfig.setText('Stop') 
                self.func_show_test_process('Waiting SUT Check Local Configuration Waiting 120s', 'Running')
                self.func_show_progressbar(120)
                # judge label and enable button
                #print ('Check Config Function ok')
                #self.func_show_test_process('SUT Check Local Configuration', 'Pass')
                #Call Check check config successfully flag flie script
            else:
                #self.func_ccs_call_batscript( 'C:\Auto_script\SUT', 'a.bat')
                self.func_show_test_process('CCS Not Execute SUT Check Local Configuration Action!', 'None')
            
        elif self.pB_1checkSUTconfig.text() == 'Stop':
            self.pB_1checkSUTconfig.setText('1.Check SUT Config')
            self.func_setbutton_status(self.pB_1checkSUTconfig, 1)
            self.count_timer.stop()
            self.timer.stop()
            self.func_show_test_process('Stop Check config or check complete!', 'Pass')
            
            #self.progressBar.setValue(0)
            
    def monitor_status(self):
        self.tB_failinfo.setText("")
        self.progressBar.setValue(0)
        if self.change_tw_show() == 1:
            return 1
        if self.pB_monitor.text() == 'Monitor':
            self.func_setbutton_status(self.pB_monitor, 0)
            self.fresh_test_status()
            self.start_count_time()
            self.pB_monitor.setText('Stop') 
            self.func_show_test_process('Monitor Test Result', 'Running')
            
            #self.tW_SUT.horizontalHeader.setStyleSheet("QHeaderView::section{background-color:rgb(40,143,218);font:13pt '宋体';color: white;};");

            # judge label and enable button
            #print ('Check Config Function ok')
            #self.func_show_test_process('SUT Check Local Configuration', 'Pass')
            #Call Check check config successfully flag flie script
        elif self.pB_monitor.text() == 'Stop':
            self.pB_monitor.setText('Monitor')
            self.func_setbutton_status(self.pB_monitor, 1)
            self.func_show_test_process('Stop Monitor Test Result', 'Pass')
            self.timer_status.stop()
            self.timer.stop()



    def func_judge_allsut_configflag(self,path,flag,line):
        sutip_dict = self.func_get_allsut_ip()
        iplist = [] 
        for ip in sutip_dict.values():
            iplist.append(ip.strip('\n')) 
        
        try:
            if os.path.exists(path) == True:
                for i in range(len(iplist)):
#                      print (path+iplist[i]+flag+'.pass')
#                       print (path+'192.168.0.14'+flag+'.pass')
                    if os.path.exists(path+'\\'+iplist[i]+flag+'.pass') == True:
                        item = QTableWidgetItem('Pass')  
    #                           item.setTextAlignment(Qt.AlignHCenter |  Qt.AlignVCenter)
                        self.tW_SUT.setItem(i, line, item)
                        self.tW_SUT.item(i, line).setBackground(Qt.green)
                    elif os.path.exists(path+'\\'+iplist[i]+flag+'.fail')== True:
                        item = QTableWidgetItem('Fail')
                        self.func_show_test_failinfo('SUT IP ---%s test item %s Fail'%(iplist[i], flag), 'Check Script and Restart test program')
                        self.tW_SUT.setItem(i, line, item)   
                        self.tW_SUT.item(i, line).setBackground(Qt.red)
                    else:
                        item = QTableWidgetItem('Running')
                        self.tW_SUT.setItem(i, line, item)  
                        self.tW_SUT.item(i, line).setBackground(Qt.blue)
                        self.tW_SUT.item(i, line).setForeground(Qt.white)    
        except Exception as e:
            #print (e)
            self.func_show_test_process('Main Program check sut config flag pass', 'Fail')
            self.func_show_test_failinfo('Error info --- %s --- , '%e, 'According to error info to fix')




    def reset_os_datetime(self):
        self.tB_failinfo.setText("")
        if self.pB_2ResetSUTostime.text() == "2.Reset SUT OS Time":
            reset_os_dt_obj = ResetOSDateTimeInterface(self)
            if reset_os_dt_obj.exec_():
                self.pB_2ResetSUTostime.setText("Stop")
                settime = reset_os_dt_obj.dateTimeEdit.dateTime().toString(self.ccs_resettimeformat)
                f = open(self.ccs_reset_ostime_file, "w")
                f.write(settime)
                f.close()
                self.start_count_time()
                self.func_setbutton_status(self.pB_2ResetSUTostime, 0)
                self.func_ccs_call_batscript( self.ccs_test_path, self.ccs_runautosetostime_script)  ## Call Run Auto setting os time script    ##self.ccs_runautosetostime_script 
                self.func_show_test_process('Waiting SUT Check Local Configuration Waiting 120s', 'Running')
                self.func_show_progressbar(120)
                #Call Check set os time successfully flag flie script
            else:
                self.func_show_test_process('CCS Cancle Set os datetime', 'None')
                
        elif self.pB_2ResetSUTostime.text() == "Stop":
            self.pB_2ResetSUTostime.setText("2.Reset SUT OS Time")
            self.func_setbutton_status(self.pB_2ResetSUTostime, 1)
            self.count_timer.stop()
            self.timer.stop()
            self.func_show_test_process('Stop excute reset os time script or reset complete!', 'Pass')
            

            
    def log_upload(self):
        self.tB_failinfo.setText("")
        self.progressBar.setValue(0)
        check_status = self.judge_radiobt_checked()
        #print (check_status)
        if check_status == False:
            self.func_show_test_process('No Mode button selected!', 'Fail')
            self.func_show_test_failinfo('No Mode button selected Fail', 'Select one mode in 3 types')
            return 1
        if check_status == "h25" :
            self.func_ccs_call_batscript( self.ccs_upload_path, self.ccs_upload_highper25C_script)
            self.func_show_test_process('Call Upload Log Script a.bat', 'Pass')
        elif check_status == "b25" :
            self.func_ccs_call_batscript( self.ccs_upload_path, self.ccs_upload_balance25C_script)
        elif check_status == "h30" :
            self.func_ccs_call_batscript( self.ccs_upload_path, self.ccs_upload_highper30C_script)
        elif check_status == "b30" :
            self.func_ccs_call_batscript(self.ccs_upload_path, self.ccs_upload_balance30C_script)
        elif check_status == "h35" :
            self.func_ccs_call_batscript( self.ccs_upload_path, self.ccs_upload_highper35C_script)
        elif check_status == "b35" :
            self.func_ccs_call_batscript(self.ccs_upload_path, self.ccs_upload_balance35C_script)
        elif check_status == "hp" :
            self.func_ccs_call_batscript( self.ccs_upload_path, self.ccs_upload_highperPTU_script)
        elif check_status == "bp" :
            self.func_ccs_call_batscript( self.ccs_upload_path, self.ccs_upload_balancePTU_script)
        
    
    
    def data_analysis(self):
        self.tB_failinfo.setText("")
        self.progressBar.setValue(0)
        check_status = self.judge_radiobt_checked()
        #print (check_status)
        if check_status == False:
            self.func_show_test_process('No Mode button selected!', 'Fail')
            self.func_show_test_failinfo('No Mode button selected Fail', 'Select one mode in 3 types')
            return 1
        if check_status == "h25" :
            self.func_ccs_call_batscript( self.ccs_dataanalysis_path, self.ccs_dataanalysis_highper25C_script)
        elif check_status == "b25" :
            self.func_ccs_call_batscript( self.ccs_dataanalysis_path, self.ccs_dataanalysis_balance25C_script)
        elif check_status == "h30" :
            self.func_ccs_call_batscript( self.ccs_dataanalysis_path, self.ccs_dataanalysis_highper30C_script)
        elif check_status == "b30" :
            self.func_ccs_call_batscript(self.ccs_dataanalysis_path, self.ccs_dataanalysis_balance30C_script)
        elif check_status == "h35" :
            self.func_ccs_call_batscript( self.ccs_dataanalysis_path, self.ccs_dataanalysis_highper35C_script)
        elif check_status == "b35" :
            self.func_ccs_call_batscript(self.ccs_dataanalysis_path, self.ccs_dataanalysis_balance35C_script)
        elif check_status == "hp" :
            self.func_ccs_call_batscript(self.ccs_dataanalysis_path, self.ccs_dataanalysis_highperPTU_script)
        elif check_status == "bp" :
            self.func_ccs_call_batscript( self.ccs_dataanalysis_path , self.ccs_dataanalysis_balancePTU_script)
        
    
    
    
    def clear_sut(self):
        self.tB_failinfo.setText("")
        self.progressBar.setValue(0)
        clear_sut_obj = ClearSUTInterface(self)
        if clear_sut_obj.exec_():
            mode = self.judge_radiobt_checked()
            if mode == False:
                self.func_show_test_failinfo('Test Mode Selection Fail', 'Each Mode should select one')
                return 1
            if 'p' in mode:
                self.func_ccs_call_batscript(self.ccs_test_path, self.ccs_runclearPTU_script) 
                self.func_show_test_process('Call clear SUT PTU Process script', 'Running')
                #self.func_show_test_process('PTU Test Running Please Waiting 1200s', 'Running')
            else:
                self.func_ccs_call_batscript( self.ccs_test_path, self.ccs_runclear_script)   # call clear sut all progress script
            #print ('clear ok')
                self.func_show_test_process('Call clear SUT Specpower Process script', 'Pass')
#               self.func_setbutton_status(self.pB_clear, 0)
                #self.timer.stop()
                self.func_show_progressbar(5)
            #self.pB_clear.setEnabled(False)
        else:
            #print ('clear fail')
            self.func_show_test_process('Cancle clear SUT script', 'Pass')
            
            
    def exit_tool(self):
        self.tB_failinfo.setText("")
        exit_obj = ExitInterface(self)
        if exit_obj.exec_():
            self.close()
        else:
            #print ('cancle exit')
            pass
            
            
    def help_tool(self):
        self.tB_failinfo.setText("")
        help_obj = HelpInterface(self)
        #self.ptu_tw_show()
        if help_obj.exec_():
            #print ('yes!')
            pass
        else:
            #print ('cancle exit')
            pass
        
            
            
            

    def func_setbutton_status(self, enablebt, status):
        if status == 0:
            self.pB_1checkSUTconfig.setEnabled(False)
            self.pB_2ResetSUTostime.setEnabled(False)
            self.pB_start.setEnabled(False)
            self.pB_clear.setEnabled(False)
            self.pB_logupload.setEnabled(False)
            self.pB_help.setEnabled(False)
#            self.pB_dataAnylysis.setEnabled(False)
            self.pB_exit.setEnabled(False)
            self.pB_monitor.setEnabled(False)
            enablebt.setEnabled(True)
        elif status == 1:
            self.pB_1checkSUTconfig.setEnabled(True)
            self.pB_2ResetSUTostime.setEnabled(True)
            self.pB_start.setEnabled(True)
            self.pB_clear.setEnabled(True)
            self.pB_logupload.setEnabled(True)
            self.pB_help.setEnabled(True)
#            self.pB_dataAnylysis.setEnabled(True)
            self.pB_exit.setEnabled(True)
            self.pB_monitor.setEnabled(True)
            enablebt.setEnabled(True)
            
    def change_tw_show(self):
        mode = self.judge_radiobt_checked()
        if mode == False:
            self.func_show_test_failinfo('Test Mode Selection Fail', 'Each Mode should select one')
            return 1
        if 'p' in mode:
            tw_ccs_horizontalHeader = ["PTU Main Program", "Call_Wcs_Get_Fan.bat","Call_Wcs_Get_temp.bat","Call_Wcs_Get_Psu.bat"," "," "," "]
            tw_sut_horizontalHeader = ["IP Address","PTU Test","FPGA Test","Io Meter Test","Call Pre-del","Call Io Meter Script","Call FPGA Script", " ", " " ]
            self.func_show_test_process('Select PTU Test Mode', 'Pass')
        else:
            tw_ccs_horizontalHeader = ["Call runccs.bat","Call rundirector.bat","Call runpower.bat","Call runtemp.bat","Call_Wcs_Get_Fan.bat","Call_Wcs_Get_temp.bat","Call_Wcs_Get_Psu.bat"]
            tw_sut_horizontalHeader = ["IP Address","Basic Config Check","Call SSJ Script","FPGA Test","Io Meter Test","Call Pre-del","Call Basic Check Script","Call Io Meter Script","Call FPGA Script" ]
            self.func_show_test_process('Select Spec Power Test Mode', 'Pass')
    
        #horizontalHeader = ["Call_Wcs_Get_Fan.bat","Call_Wcs_Get_temp.bat","Call_Wcs_Get_Psu.bat"," "," "," "," "]
        #self.tW_CCS = QTableWidget()
        self.tW_CCS.setHorizontalHeaderLabels(tw_ccs_horizontalHeader)
        self.tW_SUT.setHorizontalHeaderLabels(tw_sut_horizontalHeader)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg=Form()
    dlg.show()
    sys.exit(app.exec_())
