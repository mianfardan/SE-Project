from task import taskboss #code by fardan
import time,datetime

Task = taskboss()
task_list = []

userdetails = []
username = input("Enter username: ")
userdetails = Task.login(username,input("Enter Password: "))

print("Welcome "+username)

if "True" in userdetails[0]:
    user = int(0)
    listOfUser = Task.admin_list()
    
    for i in range(0,len(listOfUser)):
        if listOfUser[i] != username:
            print("Press "+str(i)+": "+listOfUser[i])
        else:
            print("Press "+str(i)+": "+listOfUser[i]+" (You)")

    user = int(input())

    print("Press 1: To add Task\nPress 2: To remove Task ")

    op = int(input())

    if op == 1 :
        name = str(input("Enter Task name "))
        des = str(input("Enter a task description "))
        dates = str(input("Enter the given days and hours in dd/hh "))
        loc = dates.find("/")
        now = datetime.datetime.today()
        due = now + datetime.timedelta(days=int(dates[0:loc]),hours=int(dates[loc+1:len(dates)]))

        Task.add_task(listOfUser[user],username,name,des,due,time.ctime())





else:
    details = Task.get_task(username)
    for detail in details:
        print(detail)

