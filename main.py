from task import taskboss # Huzaifa and fardan
import time,datetime

# Creating an instance of the class taskboss
Task = taskboss()
task_list = []

# Empty list to store user details
userdetails = []

# Prompting the user for username 9
username = input("Enter username(Enter 'new' to make a new account): ")

# If the user wants to create a new account  they  enter "new"
if username.lower() == "new":
    username = input("Enter a username: ")
    passcode = input("Enter a Password: ")

    # Signing up a new user
    Task.signup(username,passcode)
    # Logging in the newly created user
    userdetails = Task.login(username,passcode)
else:
    userdetails = Task.login(username,input("Enter Password: "))#logging in returns a array

# If login is successfully
print("\nWelcome "+username+"\n")
time.sleep(.5)

if "True" in userdetails[0]:# if admin
    print("Select a User")
    user = int(0)
    listOfUser = Task.admin_list()

   # Displaying list of users for admin to select    
    for i in range(0,len(listOfUser)):
        if listOfUser[i] != username:
            print("Press "+str(i)+": "+listOfUser[i])
        else:
            print("Press "+str(i)+": "+listOfUser[i]+" (You)")

    user = int(input())

    print("\nPress 1: To add Task")
    time.sleep(.1)
    print("Press 2: To remove Task")
    time.sleep(.1)
    print("Press 3: To veiw Task")
    time.sleep(.1)
    print("Press 4: To Genarate Report of all users")
    time.sleep(.1)
    print("Press 5: To Make a admin")
    time.sleep(.1)
    print("Press 6: To mark task as done")
    time.sleep(.1)
    print("Press 7: For Indivual reporting")
    op = int(input())
    print("\n")

    if op == 1 :
        # Adding a new task
        name = str(input("Enter Task name: "))
        des = str(input("Enter a task description: "))
        while True:
            priority = int(input("Enter a priority from 1 to 10 where 10 is high priority "))
            if priority >= 1 and priority <= 10:
                break
            else:
                print("You have enter a invaild entry\nTry Agian")
                time.sleep(1)
        while True:
            dates = str(input("Enter the given days and hours in dd/hh: "))
            if "/" in dates and len(dates) >= 3:
                break
            else:
                print("You have enter a invaild entry\nTry Agian")
                time.sleep(1)
        loc = dates.find("/")
        now = datetime.datetime.today()
        due = now + datetime.timedelta(days=int(dates[0:loc]),hours=int(dates[loc+1:len(dates)]))

        Task.add_task(listOfUser[user],username,name,des,due,time.ctime(),str(priority))

        # Viewing tasks 
    elif op == 3:# add code for empty array
        details = Task.get_task(listOfUser[user])
        if len(details) > 0:
            for detail in details:
                print(detail)
        else:
            print(listOfUser[user]+" has no Task")
    elif op == 2:
        # Removing a task
        details = Task.get_task(listOfUser[user])
        for detail in details:
            print(detail)
        op = int(input())

        Task.remove_task(details[op],listOfUser[user])
    elif op == 4:
        reports = Task.reporting()

        for report in reports:
            print(report)
            time.sleep(1)
    elif op == 5:
        print(Task.make_admin(listOfUser[user]))
    elif op ==6:
        details = Task.get_task(listOfUser[user])
        if len(details) > 0:
            for detail in details:
                print(detail)
            op = int(input())
            print(Task.complete_task(listOfUser[user],details[op]))
        else:
            print("All tasks are done")
    elif op == 7:
        lisOFTask,c,p = Task.Indiviual_reporting(listOfUser[user])
        print(listOfUser[user]+" has "+str(c)+" Task(s) compeleted and "+str(p)+"Tasks pennding(s)")
        for fardan in lisOFTask:
            print(fardan)
    else:
        print("Please open your eyes and enter a valid entry")


        
else:# if not an admin
    print("\nPress 1: To mark task complete or view task\nPress 2: To add Task")
    op2 = int(input())
    print("\n")
    if op2 == 1:
        details = Task.get_task(username)# Viewing tasks for non-admin users
        for detail in details:
            print(detail)
        if len(details) > 0:
            op = int(input())
            print(Task.complete_task(username,details[op]))
        else:
            print("Respected "+username+",\nYou have not been assigned a new task yet.\nHave a great day.")
    elif op2 == 2:
        # Adding a new task
        name = str(input("Enter Task name: "))
        des = str(input("Enter a task description: "))
        while True:
            priority = int(input("Enter a priority from 1 to 10 where 10 is high priority "))
            if priority >= 1 and priority <= 10:
                break
            else:
                print("You have enter a invaild entry\nTry Agian")
                time.sleep(1)
        while True:
            dates = str(input("Enter the given days and hours in dd/hh: "))
            if "/" in dates and len(dates) >= 3:
                break
            else:
                print("You have enter a invaild entry\nTry Agian")
                time.sleep(1)
        loc = dates.find("/")
        now = datetime.datetime.today()
        due = now + datetime.timedelta(days=int(dates[0:loc]),hours=int(dates[loc+1:len(dates)]))

        Task.add_task(username,username,name,des,due,time.ctime(),str(priority))
    else:
        print("please only use the provide options")
        time.sleep(5)                                   