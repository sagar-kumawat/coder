'''
take a list say  adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
write the program that will do
  i)  print only those numbers greater than 5
  ii)  also print those numbers those are less than or  equals to 2  ( <= 2 )
  iii)  store these answers in in two different list also
'''




#!usr/bin/python3

adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
list1=[]
list2=[]
for i  in  adhoc:
	if int(i)>5:
		list1.append(i)
	
	elif int(i)<=2:
		list2.append(i)

print("Numbers which are greater than 5:"+str(list1))
print("\nNumbers which are less than or equals to 2: "+str(list2))
		

