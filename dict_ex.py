#program to count the most frequent word in the file
name=raw_input("Enter file:")
handle= open(name,'r')
#text =handle.read()
  #words is a list ,text is a string
#creates/increments the value
counts=dict()
email={}#dictionary created
for line in handle:
 line=line.rstrip()
 if not line.startswith('From '): continue # from and space is looked up
 words=line.split()
 email= words[1]
 print email
 
 #pieces= email.split('@')
 #print pieces[1]

 counts[email]=counts.get(email,0)+1

bigcount=None#don't know what is the largest count so far
bigword=None#don't know what word that is
for word,count in counts.items():
  if bigcount is None or count>bigcount:#if the count is not seen so far or if it is larger than the last one
   bigword=word #will run through all of the word count key value pairs
   bigcount=count
print bigword,bigcount #prints most common word and how many times