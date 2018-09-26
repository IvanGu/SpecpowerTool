# -*- coding: utf-8 -*-
import sys
import os


def get_configFile_set_ver(file,key):
    with open(file, 'r', encoding='utf-8') as f:
        line=f.readline()
        while line:
            if key in line:
                result=line.split('=')[1]
                if not line:break
            line=f.readline()
        return result

if __name__ == '__main__':
    filepath = 'C:\AutoScript\SUT\T_Basicinfo.bat'
    biosver = get_configFile_set_ver(filepath,'set SUT_BIOS_Ver')
    print ('BIOS version:',biosver)
    cpldver = get_configFile_set_ver(filepath,'set SUT_CPLD_Ver')
    print ('CPLD version:',cpldver)
    bmcver = get_configFile_set_ver(filepath,'set SUT_BMC_Ver')
    print ('BMC version:',bmcver)
    cputype = get_configFile_set_ver(filepath,'set SUT_CPU_Type')
    print ('CPU type:',cputype)
    memtype = get_configFile_set_ver(filepath,'set SUT_Memory_Type')
    print ('memory type:',memtype)
    ssdtype = get_configFile_set_ver(filepath,'set SUT_SSD_Type')
    print ('SSD type:',ssdtype)
    nvmetype = get_configFile_set_ver(filepath,'set SUT_M2_Type')
    print ('Nvme type:',nvmetype)
    





# s="SUT_BIOS_Ver"
# f=open("C:\AutoScript\SUT\T_Basicinfo.bat")
# line=f.readline()
# while line:
    # if s in line:
        # print (line)
        # if not line:break
    # line=f.readline()


