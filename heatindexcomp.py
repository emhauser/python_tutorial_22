###Column names and column indices
columns = {'date': 0, 'time': 1, 'tempout': 2, 'humout': 5, 'heatindex': 13}

##Datatypes for each column(if non-string)
types = {'tempout':float, 'humout':float, 'heatindex':float}



##Initialize data variable as an emtpy list:
data = {}
for column in columns:
    data[column] = []

# Read the data file
filename = "data/wxobs20170821.txt"
datafile = open(filename, 'r')


##METHOD2
with open(filename,'r') as datafile:
    for _ in range(3):
        datafile.readline() 

    for line in datafile:
        datum = line.split()
        for column in columns:
            i = columns[column]
            t = types.get(column,str)
            value = t(datum[i])
            data[column].append(value)
   
# Compute heat index
def compute_heatindex(t,hum):
    a = -42.397 
    b = 2.04901523
    c = 10.14333127
    d = 0.22475541
    e = 0.00683783
    f = 0.05481717
    g = 0.00122874
    h = 0.00085282
    i = 0.00000199

    rh = hum/100

    hi = (a + (b * t) + (c * rh) + (d * t * rh) + \
        (e * t**2) + (f * rh**2) + (g * t**2 * rh) + \
        (h * t * rh**2) + (i * t**2 * rh**2))
    
    return hi

heatindex = []
for temp, hum  in zip(data['tempout'], data['humout']):
    heatindex.append(compute_heatindex(temp, hum))
 

##Output comparison of data
print('                      ORIGINAL    ESTIMATED')
print('   DATE      TIME    HEATINDEX    HEATINDEX    DIFFERENCE')
print('-------    ------    ---------    ---------    ----------')
zip_data = zip(data['date'], data['time'], data['heatindex'], heatindex)
for date, time, hi_data, hi_est in zip_data:
    hi_diff = hi_data - hi_est
    print(f'{date}    {time:>6}    {hi_data:9.6f}    {hi_est:9.6f}    {hi_diff:10.6f}')

#for wc_data, wc_est in zip(data['windchill'], windchill):
    #print(f'{wc_data:.5f}   {wc_est:.5f}    {wc_data - wc_est:.5f}')


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


