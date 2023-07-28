import pandas as pd
import sys

# Get how many rows the user wants to store
n = int(input('how many rows? '))

# need a special get_name function because the string for the name of functions isnt always consistent
def get_name(name):
    # If it includes a bracket
    if name[len(name)-1:] == '}':
        # return the name without the bracket
        return name.replace('}','')
    else:
        # if not a bracket its a normal name so we take the name of function from the parenthes and back
        name = name[name.index('(')+1:]
        return name.replace(')', '')

def populate_arrays(f):
    # initialize variables
    ncalls = []
    tottime = []
    tot_percall = []
    cumtime = []
    cum_percall = []
    function_names = []
    
    # get the total runtime from the top line
    runtime = [float(f.readline().split(' ')[-2])]*n

    # skip some lines so we can start reading the data
    for _ in range(4):
        next(f)

    # loop throught the ammount of rows specified
    for _ in range(n):
        # pull the line and split it
        arr = f.readline().split()
        
        # if the first value had a slash we cant take the float value so we just take the normal value
        # read the documentation for cProfile if youre curious about the slash https://docs.python.org/3/library/profile.html
        if '/' in arr[0]:
            ncalls.append(arr[0])
        else:
            ncalls.append(float(arr[0]))
        # add the values for to the list
        tottime.append(float(arr[1]))
        tot_percall.append(float(arr[2]))
        cumtime.append(float(arr[3]))
        cum_percall.append(float(arr[4]))
        function_names.append(get_name(arr[-1]))
    
    return ncalls, tottime, tot_percall, cumtime, cum_percall, function_names, runtime

# load the file inputted into the command line 
f = open(sys.argv[1], 'r')

# call populate_arrays to load the get the info from the file
ncalls, tottime, tot_percall, cumtime, cum_percall, function_names, runtime = populate_arrays(f)

# put all of the data into a dictinary to prepare for it to go into the dataframe
data = {'function names': function_names, 'Number of calls': ncalls, 'tottime': tottime, 'total time per call': tot_percall, 
        'cumlative time': cumtime, 'cum_time per call': cum_percall, 'program runtime': runtime}

# put the data in a dataframe so we can put it into a csv file
df = pd.DataFrame(data)

print(df)

# get the file name
filename = sys.argv[1].replace('.txt', '.ods') # NOTE instead of ods you can put '.xls' for windows

# put it into an Excel/ odf file
try:
    with pd.ExcelWriter(filename, 'odf') as writer:
        df.to_excel(writer)
    print(f"Excel file '{filename}' created successfully.")
except Exception as e:
    print(f"Error occurred while creating Excel file: {e}")
