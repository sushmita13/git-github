#when we do not specify a delimiter,multiple spaces are treated like 'one' delimiter
#we can specify what delimiter character to use in the splitting
line = 'A lot         of spaces'
etc=line.split()
print etc

line='first;second;third' #no space ,therefore considered as one word
thing=line.split()
print thing
print len(thing)

thing=line.split(';')
print thing 
print len(thing)