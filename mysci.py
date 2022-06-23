##Initialize data variable as an emtpy list:
data = {'date':[],
	'time':[],
	'tempout':[]} ## list [0] vs dict['key'] --> data['time']

# Read the data file
filename = "data/wxobs20170821.txt"
datafile = open(filename, 'r')


##METHOD1
#opens datafile
#data = datafile.read()
#datafile.close()

##METHOD2
with open(filename,'r') as datafile:
    for _ in range(3):
        datafile.readline() 

    for line in datafile:
        datum = line.split()
        data['date'].append(datum[0])
        data['time'].append(datum[1])
        data['tempout'].append(datum[2])   


#DEBUG
#print(data['tempout'][9])
#print(type(data['time']))
#print(type(data['tempout'][9]))
 
#this automatically closes datafile for you. indent 4 lines each time

##Ultimately delete this in the final code
#Debug
#print full data
#print(data)
#print string data
#print('data')
#print(type(data)

#DEBUG
#primary_colors = ['red', 'yellow','blue']
#print(primary_colors[0])
#print(primary_colors[-1])

#number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#print(number_list[0:10:1])
#num_list = [1:10]

##DEBUG
#for datum in data:
#    print(datum)
#    print(type(datum))
#print 10th index of data
#print(data[9])
#print last index
#print(data[-1])
#print every other line of data
#print(data[::2])
#print(data[0][0])


