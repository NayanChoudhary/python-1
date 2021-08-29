l=list(map(int,input().split()))
slicedlist=l[0:3]
print("sliced list =",slicedlist)
l[0]=0
l[4]=0
slicedlist[0]=0
slicedlist[2]=0
print("replaced list-1",l)
print("replaced list-2",slicedlist)
