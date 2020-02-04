## Define Function for logging

import os

def log_rx_data (data, log_file):
    #open log file
    f = open(log_file, 'a')
    #write data
    f.write(str(data)+"\n")
    #close File
    f.close()
    return

def assign_rx_data(data):
    ## Seperate elements out from the string
    datalist = data.split(',')

    if len(datalist) != 17:
        print('non-status transmission received')
    else:
        ## Seperate individual elements from List
        os.environ['Pump_stat'] = datalist[0]
        os.environ['FM1'] = datalist[1]
        os.environ['PT1'] = datalist[2]
        os.environ['VO1'] = datalist[3]
        os.environ['PT2'] = datalist[4]
        os.environ['FM2'] = datalist[5]
        os.environ['VO2'] = datalist[6]
        os.environ['FM3'] = datalist[7]
        os.environ['PT3'] = datalist[8]
        os.environ['OTI'] = datalist[9]
        os.environ['EIV'] = datalist[10]
        os.environ['Eng_stat'] = datalist[11]
        os.environ['Eng_throt'] = datalist[12]
        os.environ['EOV'] = datalist[13]
        os.environ['Sump_lv'] = datalist[14]
        os.environ['VO3'] = datalist[15]
        os.environ['FM4'] = datalist[16]
    return

