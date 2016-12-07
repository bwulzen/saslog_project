def open_sas_log(sas_log):
    #give this function the sas log to open
    #it will create a variable which has the modified sas log in a python variable 
    #it will have removed the bullshit lines


    log_handle = open(sas_log)
    python_log_raw = log_handle.readlines()


    python_log = []
    j = -1
    for i, line in enumerate(python_log_raw): 
        #we want to append every line EXCEPT
        #we do not want to append 'the SAS system' lines
        #we do not want to append the lines after them EITHER 
        
        if ('The SAS System' not in line) and (j != i):
            python_log.append(line)
            
        elif 'The SAS System' in line:
            j = i + 1
           
    
    #qa to see the lines we've created

    
    return(python_log)
    