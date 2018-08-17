fhand=open('mbox.txt')
for line in fhand:
 line=line.rstrip()
 if not line.startswith('From '): continue # from and space is looked up
 words=line.split()
 print words[2]
 ####