# Read the data file
filename = "data/wxobs20170821.txt"
datafile = open(filename, 'r')

##METHOD1
#opens datafile
#data = datafile.read()
#datafile.close()

##METHOD2
with open(filename,'r') as datafile:
    data = datafile.read()
 
#this automatically closes datafile for you. indent 4 lines on data

##Ultimately delete this in the final code
#Debug
#print full data
#print(data)
#print string data
#print('data')
#print(type(data)
