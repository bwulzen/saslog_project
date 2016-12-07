def find_procedure_type(line):
    #returns the words between 'PROCEDURE' and 'used'
    procedure_start = line.find('PROCEDURE')
    used_start = line.find('used') - 1
    procedure_end = procedure_start + len('PROCEDURE') + 1
    return(line[procedure_end:used_start])
    

def find_steps(python_log):
    #returns a dictionary with a variety of lists used
    return_dict={
    'step_timeline': [],
    'step_timeline_line_numbers': [], 
    'unique_proc_list': [],
    'step_text': [], 
    'fullstimer_on': False
    }
    line_count = 0
    step_end_check = 999999999
            
    for line in python_log:
        #finding the lines with PROCEDURES
        #find what type is, check if it isn't in unique proc list, if not append
        if ('PROCEDURE' in line and 'used' in line) == True:
            procedure_type = find_procedure_type(line)
            if procedure_type not in return_dict['unique_proc_list']:
                return_dict['unique_proc_list'].append(procedure_type)
                
            return_dict['step_timeline'].append(procedure_type)

            step_end_check = line_count
        
        #finding lines that tell us a data step has finished
        if line.find('DATA statement used') > 0:
            if 'DATA STEP' not in return_dict['unique_proc_list']:
                return_dict['unique_proc_list'].append('DATA STEP')
            return_dict['step_timeline'].append('DATA STEP')

            step_end_check = line_count
        
            
        if line == '\n' and line_count > step_end_check:
            print('we here boys')
            return_dict['step_timeline_line_numbers'].append(line_count)
            step_end_check = 999999999
        line_count += 1 
    
    #following chunk creates return_dict['step_text']
    #needs logic to handle the 1st and last pieces
    for i, num in enumerate (return_dict['step_timeline_line_numbers']):
        if i == 0:
            return_dict['step_text'].append(python_log[0:return_dict['step_timeline_line_numbers'][0]])

        elif i != len(return_dict['step_timeline_line_numbers']) :
            return_dict['step_text'].append(python_log[return_dict['step_timeline_line_numbers'][i-1]:return_dict['step_timeline_line_numbers'][i]])
        else:
            return_dict['step_text'].append(python_log[return_dict['step_timeline_line_numbers'][i]:])
    return(return_dict)
    
    
   