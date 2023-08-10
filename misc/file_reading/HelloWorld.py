from itertools import takewhile

f = open('filetest.txt', 'r')
# import gzip

# f = gzip.open('data.gz')


key = '/'
used_zip = False

def if_new_line(raw_line):
    line = raw_line.decode("utf-8") if used_zip else raw_line
    return line.strip()


lines = list(takewhile(lambda line: key not in if_new_line(line), f))

for line in f:
    print(line)
