import pandas as pd
import sys
import odswriter as ods

n = int(input('how many rows? '))


def get_name(name):
    if name[len(name)-1:] == '}':
        return name.replace('}','')
    else:
        name = name[name.index('(')+1:]
        return name.replace(')', '')
    
first_input_file = sys.argv[1]
# second_input_file = sys.argv[2]

f1 = open(first_input_file, 'r')
# f2 = open(second_input_file, 'r')


ncalls = []
tottime = []
tot_percall = []
cumtime = []
cum_percall = []
function_names = []
runtime = []

# ncalls2 = []
# tottime2 = []
# tot_percall2 = []
# cumtime2 = []
# cum_percall2 = []
# function_names2 = []
# runtime2 = []

def main(f):

    ncalls = []
    tottime = []
    tot_percall = []
    cumtime = []
    cum_percall = []
    function_names = []
    
    runtime = [float(f.readline().split(' ')[-2])]*n

    for _ in range(4):
        next(f)

    for _ in range(n):
        line = f.readline()
        arr = line.split()
        if '/' in arr[0]:
            ncalls.append(arr[0])
        else:
            ncalls.append(float(arr[0]))
        tottime.append(float(arr[1]))
        tot_percall.append(float(arr[2]))
        cumtime.append(float(arr[3]))
        cum_percall.append(float(arr[4]))
        function_names.append(get_name(arr[-1]))
    
    return ncalls, tottime, tot_percall, cumtime, cum_percall, function_names, runtime


ncalls, tottime, tot_percall, cumtime, cum_percall, function_names, runtime = main(f1)

# ncalls.append(None)
# tottime.append(None)
# tot_percall.append(None)
# cumtime.append(None)
# cum_percall.append(None)
# function_names.append(None)
# runtime.append(None)    

# # ncalls2, tottime2, tot_percall2, cumtime2, cum_percall2, function_names2, runtime2 = main(f2)

# ncalls += ncalls2
# tottime += tottime2
# tot_percall += tot_percall2
# cumtime += cumtime2
# cum_percall += cum_percall2
# function_names += function_names2
# runtime += runtime2

data = {'function names': function_names, 'Number of calls': ncalls, 'tottime': tottime, 'total time per call': tot_percall, 
        'cumlative time': cumtime, 'cum_time per call': cum_percall, 'program runtime': runtime}

df = pd.DataFrame(data)

print(df)

filename = first_input_file.replace('.txt', '.csv')
# filename = filename.replace('../', '')

# with pd.ExcelWriter(filename, 'odf') as writer:
#      df.to_excel(writer)

try:
    # Save the DataFrame to a CSV file
    df.to_csv(filename, index=False)
    print(f"CSV file '{filename}' created successfully.")
except Exception as e:
    print(f"Error occurred while creating CSV file: {e}")

