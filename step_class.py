#given a line with a second count in it, return the number of seconds
def second_counter(line):
    second_count = 0
    line_words = line.split()
    for word in line_words:
        #words with a '.' have time
        if word.find('.') > 0:
            #if a colon is found, then the time amount is mm:ss.dd and the minutes need to be counted
            minute_split = word.split(':')
            if len(minute_split) > 1:
                minute_conversion = 60 * (float(minute_split[0]))
                second_count = minute_conversion + float(minute_split[1])
            else: 
                second_count = float(minute_split[0])
    return(second_count)
               
              

class StepClass:
    def __init__(self, index, type, text, fullstimer):
        self.index = index
        self.type = type
        self.text = text
        self.fullstimer = fullstimer
        self.test = 1
        self.user_time = 0
        self.real_time = 0
        self.system_time = 0
        self.cpu_time = 0
        self.cpu_non_fullstimer = 0.0
        
        #self.number_of_output_dataset = 0
        self.output_dataset_names = []
        self.output_dataset_obs = []
        self.output_dataset_vars = []
        self.input_datasets = []
        

    def find_times(self):
        for line in self.text:
            if line.find('real time') > 0:
                self.real_time = second_counter(line)
            elif line.find('user cpu time') > 0:
                self.user_time = second_counter(line)
            elif line.find('system cpu time') > 0:
                self.system_time = second_counter(line)
        return() 
        
        
    def proc_sql_process(self):
        for line in self.text:
            
            #look for the NOTE lines which indicate what datasets were created
            if line.startswith('NOTE:') and line.find('created,') > 0:
                line_split = line.split()
                self.output_dataset_names.append(line_split[2])
                self.output_dataset_obs.append(line_split[5])
                self.output_dataset_vars.append(line_split[8])
            #look for the FROM and JOIN lines to identify input datasets
            #the from line is tricky because it often has 'connection' or 'disconnect'
            if line.lower().find('from') > 0 and line.lower().find('connect') == -1:
                line_split = line.split()
                self.input_datasets.append(line_split[2])
            if line.lower().find('join') > 0:
                #find the position of 'join', take the word after it
                #this is done to help with inner vs outer joins 
                line_split = line.split()
                i = 0
                for word in line_split:
                    if word.lower() == 'join':
                        self.input_datasets.append(line_split[i+1])
                    i += 1

        return()
    
    
    
    
    def data_step_process(self):
        for line in self.text:
            #notes about obsrevations read from the 'set' datasets
            if line.startswith('NOTE:') and line.lower().find('observations read from the') > 0:
                line_split = line.split()
                self.input_datasets.append(line_split[10].strip('.'))
                
            
            #notes with 'total proces time' aint worth shit
            
            #other lines are good with 'observations and variables
            if line.startswith('NOTE:') and line.lower().find('observations and') > 0:
                line_split = line.split()
                self.output_dataset_names.append(line_split[4])
                self.output_dataset_obs.append(line_split[6])
                self.output_dataset_vars.append(line_split[9])
                

        return() 
        
        
    def proc_process(self):
        #seems to work for: sort, transpose
        #does not seem to work for:
        for line in self.text:
            if line.startswith('NOTE:') and line.lower().find('observations read from the') > 0:
                line_split = line.split()
                self.input_datasets.append(line_split[10].strip('.'))  
                
            if line.startswith('NOTE:') and line.lower().find('observations and') > 0:
                line_split = line.split()
                self.output_dataset_names.append(line_split[4])
                self.output_dataset_obs.append(line_split[6])
                self.output_dataset_vars.append(line_split[9])
        
        
        
        return()