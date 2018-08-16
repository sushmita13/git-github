jjj={'chuck':1,'fred':42,'jan':100}
print list(jjj)#only stores the list of keys and not their values
print jjj.keys()
print jjj.values()#gives values of keys,order of keys and values correspond
print jjj.items()#gives list and it's values in a form of list called tuples

#two iteration variables
jjj={'chuck':1,'fred':42,'jan':100}
for aaa,bbb in jjj.items():# aaa=key,bbb=values
 print aaa,bbb

stuff = dict()
print stuff.get('candy',-1)#-1 is printed