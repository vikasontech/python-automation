import re
from fbchat import Client
from fbchat.models import *
import datetime

print('hello')

def main():
    now=datetime.datetime.now()
    todayDateMonthk=now.strftime("%d-%m")


    dobList =["Vishal Kumar:14-10"]

    #pattern1=r"([\w]+) ([\w]+):"+k
    #mat = re.search(pattern1,k)

    for per in dobList:
        dataArray=per.split(':')
        if(dataArray[1] == todayDateMonthk):
            print(dataArray)
            #client=Client('c4157022@urhen.com','dummy123')
            print(client.fetchAllUsers())

            #users=client.searchForusers(dataArray[0])
            
main()

