import cProfile, sys

pr = cProfile.Profile()

pr.enable()

# def main():
#     Your code here

pr.disable()

'''
the way I have cProfile set up it will output 2 files.
a .prof file that can be used by some software to visualise the data. for more info look at "mpi_three.txt" in mpi4py
a .txt file that can be viewed as normal
'''

# Dump results:
# - for binary dump
pr.dump_stats('NAME OF FILE YOU WANT.prof')
# - for text dump
with open( 'NAME OF FILE YOU WANT.txt', 'w') as output_file:
    sys.stdout = output_file
    # sort is what you want the .txt file to be sorted by   
    pr.print_stats( sort='tottime')
    sys.stdout = sys.__stdout__

