
from readdata import read_data
from printing import print_comparison 

###Column names and column indices
columns = {'date': 0, 'time': 1, 'tempout': 2, 'windspeed': 7, 'windchill': 12}

##Datatypes for each column(if non-string)
types = {'tempout':float, 'windspeed': float, 'windchill':float}

# Read the data file
data = read_data(columns, types=types)
   
def estimate_windchill(t,v):
    wci = t - 0.7 * v 
    return wci

##make empty list
windchill = []
#make tuple, call windspeed function on each pair
for temp, windspeed in zip(data['tempout'], data['windspeed']):
    windchill.append(estimate_windchill(temp, windspeed))
 

##Output comparison of data
print_comparison('WINDCHILL', data['date'], data['time'], data['windchill'], windchill)


##Debug
#print(windchill)


# DEBUG
## zip function

#for i, j in zip([1,2], [3,4,5]):
#    print(i,j)


#DEBUG
#print(float('error'))
#print(int('error'))
#print(int(data['tempout'][9]))


#keys = list(data.keys())
#print(keys)


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


