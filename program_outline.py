from open_sas_log import open_sas_log
from second_counter import second_counter
from find_steps import find_steps
from step_class import StepClass



# 1. Read the SAS log into a python variable. 
# 1.1 Remove lines with no information from the SAS log. 
python_log = open_sas_log('ddoc.txt')


# 2. Identify the structure of the logs - the data steps and procedures 
# 2.1 Develop a 'timeline' of each step 
# 2.2 Find the line numbers marking the beginning (and end?) of each step/proc
# 2.3 Separate each out each block of line number text into their own variables corresponding to the 'timeline' of 2.1

#this is a dictionary
python_structure = find_steps(python_log)
# print(python_structure.keys())
print(python_structure['step_timeline_line_numbers'])


    
    
# 2.4 What libnames were assigned?
# 2.5 What macro variables were created

# for line in python_structure['step_text']:
    # for ind_line in line:
        # print(ind_line)


# 3. Operations on the block of 2.3                
#create a list of stepclass objects 
steps = list()
#IMPORTANT NOTE: the - 1 in range() is to remove the last bit of text after the final step - or not TO BE DECIDED?
for i in range(len(python_structure['step_text']) ):
    #order of variables - index, type, text
    steps.append(StepClass(i, python_structure['step_timeline'][i], python_structure['step_text'][i], python_structure['fullstimer_on']))
    
#why is the last element of the list acting funky? seems to not really be any useful information 
#worth thinking about if it should be deleted or not - will this last part ever have useful information? seems probably not...
#print('text:', steps[28].text)


# 3.1 How long did the step take? (ALL STEPS)
for step in steps:
    step.find_times()
    

    

# 3.2 Did the step create any datasets? 

for step in steps:
    if step.type == 'SQL':
        step.proc_sql_process()
        # print('For step', step.index, ':')
        # print('Input datasets:', step.input_datasets)
        # print('Output datasets:', step.output_dataset_names)
        # print('\n\n')
    
    if step.type == 'DATA STEP':
        step.data_step_process()
        
        
        
    if step.type in ('SORT', 'TRANSPOSE'):
        step.proc_process()

        
    print('Information for step', step.index)
    print('Type:', step.type)
    print('Text:', step.text)
    print('Input datasets:', step.input_datasets)
    print('Output datasets:', step.output_dataset_names)
    print('Obs, vars:', step.output_dataset_obs, step.output_dataset_vars)
    print('Real time:', step.real_time, '\n\n')
    

# 3.2.1 How many datasets were created? 
# 3.2.2 What were their names?
# 3.2.3 How many observations and variables did they have?
# 3.3 Which datasets were read in?
# 3.3.1 What were their relationships with the datasets created (3.2?)



# 4. Basic information to spit out
# 4.1 Timeline of steps
# 4.2 Amount of time each step took 

# 5. Intermediate information to spit out 
# 5.1 Sortable representation of the data steps 
# 5.1.1 Which data steps took the most time?
# 5.1.2 Which data steps created output with the most variables?

# 6. Advanced information to spit out 
# 6.1 Visual representation of the program 
