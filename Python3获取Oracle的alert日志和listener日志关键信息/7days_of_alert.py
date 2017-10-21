import os
import datetime
DayList = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
#KeyWordList = ['ORA-', 'Error', 'Starting ORACLE instance', 'Shutting down instance','TNS-','ALTER']
KeyWordList = ['ORA-', 'Error','TNS-','ALTER']
AlertLogFile = r'alert_orcl.log'
i=0
list_linenum=[]
linenum=0
j=0
INFO_AlertLogFile = r'INFO_alert_orcl.log'

try:
    with open(AlertLogFile,'r') as f:
        list_allline = f.readlines()
        rowcount=len(list_allline)

        while i < rowcount:
            line = list_allline[i]
            if len(line) == 25 and line[0:3] in DayList and (datetime.datetime.now()-datetime.datetime.strptime(line[0:24], "%a %b %d %X %Y")).days < 7:
                linenum = i
                print(line[0:24])
                list_linenum.append(linenum)
            i = i + 1
        #print(list_linenum)
        if os.path.exists(os.getcwd() + '\\'+INFO_AlertLogFile):
            os.remove(os.getcwd() + '\\'+INFO_AlertLogFile)
        with open(INFO_AlertLogFile, 'a') as f1:
            while j < len(list_linenum)-1:
                list_temp = list_allline[list_linenum[j]:list_linenum[j+1]]
                for w in KeyWordList:
                    if w in str(list_temp):
                        #print(list_temp)
                        for t in list_temp:
                            f1.write(t)
                        f1.write('\n')
                j = j + 1

            #最后一条有问题如何处理
            list_temp = list_allline[list_linenum[j]:]
            for w in KeyWordList:
                if w in str(list_temp):
                    # print(list_temp)
                    for t in list_temp:
                        f1.write(t)

except Exception as err:
	print(err)

