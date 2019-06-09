'''
write a code using  that will take user input from and search on google and store top 10 url in the list.


conditions : 
    i )   URL must be stored permanently as well
    ii)   user can give input using keyboard and  voice both

NOTE: You  may need to install google package 
'''


#!usr/bin/python3

from googlesearch import search 
import webbrowser
web=input("Type your search here:--->")
url=[]
file=open('search.txt',"w")

for i in  search(web,stop=10):
	url.append(i)
	file.write(i+"\n")

#print(url)     ---> to print the list 

webbrowser.open_new_tab('https://www.google.com/search?q='+web)
