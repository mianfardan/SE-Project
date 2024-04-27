from task import taskboss 
import time,datetime

# Creating an instance of the class taskboss
Task = taskboss()
task_list = []

# Empty list to store user details
userdetails = []

# Prompting the user for username 
username = input("Enter username(Enter 420 to make a new account): ")

# If the user wants to create a new account  they  enter "420"
if username == "420":
    username = input("Enter a username: ")
    passcode = input("Enter a Password: ")

    # Signing up a new user 
    Task.signup(username,passcode)
    # Logging in the newly created user
    userdetails = Task.login(username,passcode)
else:
    userdetails = Task.login(username,input("Enter Password: "))#logging in returns a array

# If login is successfully
print("Welcome "+username)

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

    print("Press 1: To add Task\nPress 2: To remove Task\nPress 3: To veiw Task ")

    op = int(input())

    if op == 1 :
        # Adding a new task
        name = str(input("Enter Task name: "))
        des = str(input("Enter a task description: "))
        dates = str(input("Enter the given days and hours in dd/hh: ")) #error handling needed
        loc = dates.find("/")
        now = datetime.datetime.today()
        due = now + datetime.timedelta(days=int(dates[0:loc]),hours=int(dates[loc+1:len(dates)]))

        Task.add_task(listOfUser[user],username,name,des,due,time.ctime())

        # Viewing tasks 
    elif op == 3:# add code for empty array
        details = Task.get_task(listOfUser[user])
        for detail in details:
            print(detail)
    elif op == 2:
        # Removing a task
        details = Task.get_task(listOfUser[user])
        for detail in details:
            print(detail)
        op = int(input())

        Task.remove_task(details[op],listOfUser[user])


        
else:# if not an admin

     # Viewing tasks for non-admin users
    details = Task.get_task(username)
    for detail in details:
        print(detail)
        
    op = int(input())
    
    #add complete task here

